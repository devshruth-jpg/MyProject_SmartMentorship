
"""
GameEngine: owns the player, coins, and obstacles.

Features:
- Bronze, silver, and gold coins.
- Each coin awards points only once.
- Obstacles spawn near coins.
- Three lives and one-second invincibility after a hit.
- 30-second countdown.
- Game over when time expires, lives reach zero,
  or all coins are collected.
"""

import math
import random
import pygame

from game.player import Player
from game.coin import Coin
from game.obstacle import Obstacle
from game.collection import check_collection
from game.renderer import WIDTH, HEIGHT

NUM_COINS = 6
NUM_OBSTACLES = 5

STARTING_LIVES = 3
ROUND_DURATION = 30
INVINCIBILITY_MS = 1000

# Coin types: (point value, RGB color)
BRONZE = (1, (205, 127, 50))
SILVER = (3, (192, 192, 192))
GOLD = (5, (255, 215, 0))


class GameEngine:
    def __init__(self):
        self.reset()

    def reset(self):
        """Initialize a new round."""
        self.player = Player(x=WIDTH / 2, y=HEIGHT / 2)

        self.coins = [
            self._random_coin() for _ in range(NUM_COINS)
        ]

        self.obstacles = self._create_obstacles(NUM_OBSTACLES)

        self.score = 0
        self.lives = STARTING_LIVES

        self.invincible_until = 0
        self.player.invincible = False

        self.start_ticks = pygame.time.get_ticks()
        self.time_remaining = ROUND_DURATION
        self.game_over = False

    def _random_coin(self):
        # Bronze is most common, silver less common, gold rarest.
        value, color = random.choices(
            population=[BRONZE, SILVER, GOLD],
            weights=[6, 3, 1],
            k=1,
        )[0]

        x = random.randint(30, WIDTH - 30)
        y = random.randint(30, HEIGHT - 30)

        return Coin(
            x=x,
            y=y,
            radius=12,
            value=value,
            color=color,
        )

    def _create_obstacles(self, count):
        obstacles = []
        player_rect = self.player.get_rect().inflate(30, 30)

        for i in range(count):
            target_coin = self.coins[i % len(self.coins)]

            for attempt in range(200):
                width = random.randint(40, 60)
                height = random.randint(20, 35)

                offset_x = random.randint(-90, 90)
                offset_y = random.randint(-90, 90)

                x = int(target_coin.x + offset_x - width / 2)
                y = int(target_coin.y + offset_y - height / 2)

                # Keep the complete obstacle inside the play area.
                x = max(10, min(WIDTH - width - 10, x))
                y = max(10, min(HEIGHT - height - 10, y))

                obstacle = Obstacle(
                    x=x,
                    y=y,
                    width=width,
                    height=height,
                )

                rect = obstacle.get_rect()

                # Keep the starting player position clear.
                if rect.colliderect(player_rect):
                    continue

                # Do not overlap coins.
                if any(
                    rect.colliderect(coin.get_rect().inflate(10, 10))
                    for coin in self.coins
                ):
                    continue

                # Do not overlap other obstacles.
                if any(
                    rect.colliderect(
                        existing.get_rect().inflate(10, 10)
                    )
                    for existing in obstacles
                ):
                    continue

                obstacles.append(obstacle)
                break

        return obstacles

    def handle_input(self, keys_pressed):
        # Movement stops after the round ends.
        if self.game_over:
            return

        dx = dy = 0

        if keys_pressed[pygame.K_UP]:
            dy -= self.player.speed
        if keys_pressed[pygame.K_DOWN]:
            dy += self.player.speed
        if keys_pressed[pygame.K_LEFT]:
            dx -= self.player.speed
        if keys_pressed[pygame.K_RIGHT]:
            dx += self.player.speed

        self.player.move(dx, dy, WIDTH, HEIGHT)

    def update(self):
        # Freeze gameplay after game over.
        if self.game_over:
            return

        # Calculate remaining time using real elapsed milliseconds.
        elapsed_ms = pygame.time.get_ticks() - self.start_ticks
        elapsed_seconds = elapsed_ms / 1000.0

        self.time_remaining = max(
            0,
            ROUND_DURATION - elapsed_seconds,
        )

        # End the round if time expires.
        if self.time_remaining <= 0:
            self.game_over = True
            return

        # Collect coins and award each coin only once.
        collected = check_collection(self.player, self.coins)

        for coin in collected:
            if coin in self.coins:
                self.coins.remove(coin)
                self.score += coin.value

        # IMPORTANT: end the round immediately after the last coin.
        if not self.coins:
            self.game_over = True
            return

        # Update invincibility state.
        now = pygame.time.get_ticks()
        self.player.invincible = now < self.invincible_until

        # Handle obstacle collisions only when vulnerable.
        if not self.player.invincible and self.lives > 0:
            player_rect = self.player.get_rect()

            hit_obstacle = any(
                player_rect.colliderect(obstacle.get_rect())
                for obstacle in self.obstacles
            )

            if hit_obstacle:
                self.lives -= 1
                self.invincible_until = now + INVINCIBILITY_MS
                self.player.invincible = True

        # End the round when all lives are lost.
        if self.lives <= 0:
            self.lives = 0
            self.game_over = True

    def draw(self, surface, font):
        from game import renderer

        renderer.draw_scene(
            surface,
            self.player,
            self.coins,
            self.obstacles,
        )

        seconds_left = math.ceil(self.time_remaining)

        renderer.draw_text(
            surface,
            font,
            f"Score: {self.score}   Lives: {self.lives}   "
            f"Time: {seconds_left}s",
            (10, 10),
        )

        if self.game_over:
            # Dark overlay behind the game-over message.
            overlay = pygame.Surface(
                surface.get_size(),
                pygame.SRCALPHA,
            )
            overlay.fill((0, 0, 0, 190))
            surface.blit(overlay, (0, 0))

            title_font = pygame.font.SysFont(
                "consolas", 42, bold=True
            )
            message_font = pygame.font.SysFont("consolas", 25)
            detail_font = pygame.font.SysFont("consolas", 22)

            title = title_font.render(
                "GAME OVER",
                True,
                (255, 100, 100),
            )
            final_score = message_font.render(
                f"Final Score: {self.score}",
                True,
                (255, 255, 255),
            )
            restart_message = detail_font.render(
                "Press R to play again",
                True,
                (255, 220, 80),
            )

            center_x = surface.get_width() // 2
            center_y = surface.get_height() // 2

            surface.blit(
                title,
                title.get_rect(
                    center=(center_x, center_y - 65)
                ),
            )

            surface.blit(
                final_score,
                final_score.get_rect(
                    center=(center_x, center_y)
                ),
            )

            surface.blit(
                restart_message,
                restart_message.get_rect(
                    center=(center_x, center_y + 50)
                ),
            )

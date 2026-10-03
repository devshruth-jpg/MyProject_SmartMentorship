# Architecture Description

## Style

A four-layer **modular monolith** (presentation, API, application, data) with external integrations behind adapters. A monolith was chosen over microservices because the team is small, the domain is cohesive, and the main correctness need (no double-booking) is far easier with a single transactional database.

## Components

| Component | Responsibility | Requirements |
|---|---|---|
| Student / Mentor Web App | UI for searching, booking, managing availability, scorecards and dashboards | FR-001 to FR-005 |
| REST API Gateway | Single entry point, JWT authentication, role-based access (student vs mentor) | NFR-001 |
| Auth & Profile Service | Accounts, profiles, declared domains, privacy controls, soft-delete | NFR-001 |
| Mentor Matching Service | Domain-based ranked mentor recommendations | FR-001 |
| Availability Manager | Create, update, block recurring/one-off slots; pushes changes to cache | FR-002 |
| Booking Engine | Slot re-validation, atomic booking, reschedule, cancel, policy window | FR-001, FR-005, NFR-002 |
| Scorecard Service | Structured scorecard submission and retrieval, linked to sessions | FR-004 |
| Notification Scheduler | Confirmations and timed reminders | FR-005 |
| Integration Adapters | Wrap Video Conferencing, Calendar and Email APIs so providers can be swapped | FR-003 |
| PostgreSQL | System of record for users, slots, sessions, scorecards | All |
| Redis | Caches availability for fast real-time views; short-lived slot locks | FR-002, NFR-002 |
| Audit & Soft-Delete store | Records deletion requests and ensures completion within 24 hours | NFR-001 |

## Key Design Decisions

1. **Double-booking prevention (NFR-002):** the Booking Engine runs the confirm step in one database transaction with a row-level lock (`SELECT ... FOR UPDATE`) on the slot, plus a unique constraint on (mentor, slot). If the slot is already taken, the transaction aborts and use-case alternate flow A1 informs the student.
2. **Real-time availability (FR-002):** slot changes invalidate the Redis cache and the client refreshes, meeting the 5-second criterion.
3. **Provider independence (FR-003):** meeting links and calendar invites go through adapters, so a failure or provider change does not touch core booking logic.
4. **Privacy (NFR-001):** records are soft-deleted (flagged, hidden from all queries) immediately, with a scheduled job completing removal within 24 hours of the request.
5. **Reliability (NFR-002):** stateless application instances behind a load balancer, with health checks, support the 99.5% uptime target during peak windows.

## Main Booking Flow (UC-01)

1. Student Web App calls the API Gateway, which authenticates the request.
2. Matching Service returns ranked mentors; Availability Manager returns slots from cache.
3. On confirm, Booking Engine locks the slot, re-validates, and creates the session in PostgreSQL.
4. Integration Adapters request a meeting link and send calendar invites.
5. Notification Scheduler sends confirmations and schedules reminders.

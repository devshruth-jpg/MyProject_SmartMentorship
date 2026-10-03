# Alumni Mentorship & Mock Interview Platform

**Individual Project | Requirements Engineering & Software Engineering Lab**
PES University, Department of Computer Science and Engineering

| | |
|---|---|
| **Student** | Devashruth |
| **SRN** | PES1UG24CS251 |
| **Section** | E |
| **Repository** | `MyProject_AlumniMentorship` |

## Overview

A platform that connects students with alumni working in specialised domains (Embedded Systems, Cloud Computing, ML, etc.). It combines intelligent domain-based mentor matching, a real-time availability calendar with conflict-free booking, automatic meeting-link generation, and structured post-interview scorecards.

## Stakeholders / Actors

- **Student Mentee** (primary): searches mentors, books sessions, views feedback.
- **Alumni Mentor**: publishes availability, conducts mock interviews, submits scorecards.
- **Video Conferencing System** (external): generates meeting links.
- **Notification Service** (external): delivers confirmations and reminders.

## Core Use Case

**Book Mentorship Session (UC-01):** a student filters mentors by domain, views real-time availability, and books a slot. The system re-validates the slot at confirmation (preventing double-booking), generates a meeting link, updates both calendars and notifies both parties. Alternate flow A1 handles a slot taken by another student mid-confirmation.

## Repository Structure

| Folder | Contents |
|---|---|
| [`1_Requirements_Engineering`](1_Requirements_Engineering) | Functional & non-functional requirements, Requirements Traceability Matrix (RTM), use-case diagram and flow specification |
| [`2_Architectural_Diagram`](2_Architectural_Diagram) | System architecture diagram (PNG + Mermaid source) and design rationale |
| [`3_Project_Creation_Screenshots`](3_Project_Creation_Screenshots) | Screenshots of GitHub repository creation and Jira project setup, plus Jira backlog import file |
| [`4_SRS_and_WBS`](4_SRS_and_WBS) | Software Requirements Specification (IEEE 830 style) and Work Breakdown Structure |

Each folder has its own README explaining its contents.

## Planned Tech Stack

React (web client), REST API (modular monolith), PostgreSQL, Redis, external video-conferencing and email/calendar APIs.

## Key Requirements at a Glance

- FR-001 Domain-based mentor recommendation and one-click booking
- FR-002 Mentor availability management with real-time student view
- FR-003 Automatic meeting-link generation
- FR-004 Structured post-session scorecard
- FR-005 Reminders, reschedule and cancel within a policy window
- NFR-001 Privacy compliance and soft-deletion within 24 hours
- NFR-002 Concurrency-safe booking and 99.5% uptime in peak windows

## Status

| Deliverable | Status |
|---|---|
| Requirements (FR/NFR) and use cases | Complete |
| RTM | Complete (design and test columns planned) |
| Architecture diagram | Complete |
| GitHub / Jira setup | Add screenshots in folder 3 |
| SRS and WBS | Complete (draft v1.0) |

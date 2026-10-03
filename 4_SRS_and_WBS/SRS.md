# Software Requirements Specification

**Project:** Alumni Mentorship & Mock Interview Platform
**Author:** Devashruth (PES1UG24CS251, Section E)
**Version:** 1.0 (Draft)
**Institution:** PES University, Department of Computer Science and Engineering

## Revision History

| Version | Description |
|---|---|
| 1.0 | Initial SRS built from Lab 1 requirements and use cases |

---

## 1. Introduction

### 1.1 Purpose
This document specifies the requirements of the Alumni Mentorship & Mock Interview Platform. It is intended for developers, testers, and course evaluators.

### 1.2 Scope
The platform connects students with alumni in specialised domains through domain-based matching, an availability calendar with conflict-free booking, automatic meeting links, reminders, and structured post-interview scorecards. Payments, resume review and group sessions are out of scope.

### 1.3 Definitions

| Term | Meaning |
|---|---|
| Mentee | A student using the platform |
| Mentor | An alumnus offering mock interviews or mentoring |
| Slot | A bookable time window published by a mentor |
| Scorecard | Structured feedback submitted by a mentor after a session |
| RTM | Requirements Traceability Matrix |

### 1.4 References
Requirements Table, Use-Case Flow Specification and Use-Case Diagram (folder 1); Architecture (folder 2). Format follows IEEE 830.

---

## 2. Overall Description

### 2.1 Product Perspective
A standalone web platform that integrates with an external video-conferencing system, a calendar provider and a notification service.

### 2.2 Product Functions
Mentor search and matching; availability management; booking, rescheduling and cancellation; meeting-link generation; notifications and reminders; scorecard submission and viewing.

### 2.3 User Classes

| User | Description |
|---|---|
| Student Mentee | Authenticated student with a declared domain of interest |
| Alumni Mentor | Verified alumnus with one or more domains and published availability |
| Video Conferencing System | External actor, generates meeting links |
| Notification Service | External actor, delivers messages |

### 2.4 Operating Environment
Modern desktop and mobile browsers; server-side REST API with PostgreSQL and Redis.

### 2.5 Constraints
- Cancellation or reschedule only within the policy window (e.g., up to 4 hours before a session).
- Must comply with privacy guidelines for personal data and feedback.
- Depends on third-party API availability for links and notifications.

### 2.6 Assumptions and Dependencies
- Users are authenticated and students have a complete profile.
- At least one mentor per domain has published slots.
- Third-party video and calendar APIs are available.

---

## 3. Specific Requirements

### 3.1 Functional Requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-001 | Recommend mentors by domain matching and allow one-click booking against published availability. | High |
| FR-002 | Mentors create, update and block availability (recurring or one-off); students see changes in real time. | High |
| FR-003 | On booking confirmation, generate a video meeting link and attach it to both calendar invites. | High |
| FR-004 | Mentor submits a structured scorecard (technical skills, communication, problem-solving, overall rating, free text) tied to the session. | Medium |
| FR-005 | Send reminders; allow reschedule or cancel within the policy window. | Medium |

Acceptance criteria for each requirement are in `1_Requirements_Engineering/FR_NFR.md`.

### 3.2 Non-Functional Requirements

| ID | Category | Requirement | Priority |
|---|---|---|---|
| NFR-001 | Performance & Security | Profile data and scorecards follow privacy guidelines and support soft-deletion within 24 hours of request. | High |
| NFR-002 | Reliability & Scalability | Concurrent bookings of the same slot never double-book; 99.5% uptime during peak windows. | High |

### 3.3 Use Cases

| ID | Name | Primary Actor |
|---|---|---|
| UC-01 | Book Mentorship Session | Student Mentee |
| UC-02 | Search & Match Mentor | Student Mentee |
| UC-03 | Generate Meeting Link (include of UC-01) | Video Conferencing System |
| UC-04 | Manage Availability | Alumni Mentor |
| UC-05 | Conduct Mock Interview | Alumni Mentor |
| UC-06 | Submit Scorecard | Alumni Mentor |
| UC-07 | View Feedback / Scorecard | Student Mentee |
| UC-08 | Reschedule Session (extend of UC-01) | Student Mentee |
| UC-09 | Cancel Session | Student / Mentor |
| UC-10 | Send Notification | Notification Service |

**UC-01 summary.** Preconditions: student authenticated with a declared domain; matching mentors have published slots. Main flow: filter by domain, view ranked mentors, view real-time calendar, select slot and confirm, system re-validates the slot, creates the session, generates link, attaches it to both invites, marks slot booked, sends confirmations, student sees the session on the dashboard. Alternate flow A1: slot taken during confirmation, transaction aborts, student is notified and the view refreshes. Full detail in `Use_Case_Flow_Specification.docx`.

### 3.4 External Interface Requirements

| Interface | Requirement |
|---|---|
| User interface | Responsive web UI with separate student and mentor dashboards |
| Video conferencing API | Create a meeting and return a join link |
| Calendar API | Create, update and delete invites for both parties |
| Notification service | Send email or push messages for confirmations and reminders |

### 3.5 Data Requirements
Main entities: User, StudentProfile, MentorProfile, Domain, AvailabilitySlot, Session, MeetingLink, Scorecard, Notification. A slot belongs to one mentor and can have at most one session. A scorecard belongs to exactly one session.

### 3.6 Business Rules
1. A slot can be booked by only one student.
2. Blocked or booked slots are never shown as bookable.
3. Reschedule or cancel is allowed only within the policy window.
4. Only the mentor of a session may submit its scorecard; only the session's student and mentor may view it.

---

## 4. Requirements Traceability
See `1_Requirements_Engineering/RTM.md`.

## 5. Out of Scope / Future Work
Payments, resume review, group sessions, mobile apps, analytics for placement cells.

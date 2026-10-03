# Functional & Non-Functional Requirements

Actors: Student Mentee, Alumni Mentor

## Functional Requirements

| ID | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|
| FR-001 | The system shall recommend alumni mentors to students based on domain matching (e.g., Embedded Systems, Cloud Computing, ML) and allow one-click session booking against the mentor's published availability. | High | Pass: session is added to both calendars with a meeting link. Fail: double-booking of mentor slots. | Core value proposition; manual matching does not scale across a large alumni pool. |
| FR-002 | The system shall allow alumni mentors to create, update and block out their availability calendar (recurring or one-off slots), which students can view in real time before booking. | High | Pass: slot changes reflect in the student view within 5 seconds and blocked slots cannot be booked. Fail: a booked/blocked slot is still shown as bookable. | Booking is only reliable if availability data is accurate and current. |
| FR-003 | Upon successful booking confirmation, the system shall automatically generate a video-conferencing meeting link and attach it to both parties' calendar invites. | High | Pass: link is valid and present in both invites within 1 minute of booking. Fail: booking confirmed without a usable link. | Removes manual coordination between student and mentor. |
| FR-004 | After a mock interview session, the system shall let the alumni mentor submit a structured scorecard (technical skills, communication, problem-solving, overall rating, free-text feedback) tied to that session. | Medium | Pass: scorecard is saved, timestamped and visible to the student on their dashboard. Fail: scorecard data lost or linked to the wrong session. | Structured feedback is the main learning outcome for the student. |
| FR-005 | The system shall send automated reminder notifications before a session and allow either party to reschedule or cancel within a defined policy window (e.g., up to 4 hours before). | Medium | Pass: reschedule/cancel updates both calendars and notifies the other party immediately. Fail: a cancelled session still shows as active on either calendar. | Reduces no-shows and keeps calendars trustworthy. |

## Non-Functional Requirements

| ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| NFR-001 | Performance & Security | All user profile data and feedback scorecards shall adhere to privacy guidelines and support soft-deletion within 24 hours of a deletion request. | High | Pass: benchmarking tests confirm target latency and security standards under simulated peak load. | Sensitive personal and feedback data requires regulatory compliance and user trust. |
| NFR-002 | Reliability & Scalability | The booking subsystem shall handle concurrent booking requests for the same mentor slot without allowing a double-booking, and shall maintain 99.5% uptime during peak registration windows (start of semester, placement season). | High | Pass: concurrency test with simultaneous requests for one slot results in exactly one successful booking. Fail: more than one student confirmed for the same slot. | Booking integrity is the core trust guarantee; downtime in peak periods blocks student access. |

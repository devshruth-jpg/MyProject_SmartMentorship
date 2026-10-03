# Requirements Traceability Matrix (RTM)

Traces each requirement forward to use cases, design components and test cases.

| Req ID | Requirement Summary | Priority | Use Case(s) | Design Component | Test Case ID(s) | Status |
|---|---|---|---|---|---|---|
| FR-001 | Domain-based mentor recommendation and one-click booking | High | UC-01, UC-02 | Matching Service, Booking Engine | TC-001, TC-002 | Designed |
| FR-002 | Mentor availability management with real-time student view | High | UC-04, UC-01 | Availability Manager, Redis cache | TC-003, TC-004 | Designed |
| FR-003 | Automatic meeting-link generation and calendar attach | High | UC-03, UC-01 | Video Conferencing Adapter, Calendar Adapter | TC-005, TC-006 | Designed |
| FR-004 | Structured post-session scorecard | Medium | UC-05, UC-06, UC-07 | Scorecard Service | TC-007, TC-008 | Designed |
| FR-005 | Reminders and reschedule/cancel within policy window | Medium | UC-08, UC-09, UC-10 | Booking Engine, Notification Service | TC-009, TC-010, TC-011 | Designed |
| NFR-001 | Privacy compliance and soft-deletion within 24 hours | High | All | Auth & Profile Service, Data Layer | TC-012, TC-013 | Designed |
| NFR-002 | Concurrency-safe booking and 99.5% uptime in peak windows | High | UC-01 (A1) | Booking Engine (row-level locking), Data Layer | TC-014, TC-015 | Designed |

## Planned Test Cases

| Test ID | Verifies | Description | Expected Result |
|---|---|---|---|
| TC-001 | FR-001 | Filter mentors by domain "Cloud Computing" | Only mentors with that domain returned, ranked |
| TC-002 | FR-001 | Book an open slot with one click | Session created, appears in both calendars |
| TC-003 | FR-002 | Mentor adds a recurring slot | Slot visible to students within 5 seconds |
| TC-004 | FR-002 | Mentor blocks a slot | Blocked slot cannot be booked |
| TC-005 | FR-003 | Confirm a booking | Valid meeting link generated within 1 minute |
| TC-006 | FR-003 | Open both calendar invites | Same link present in both |
| TC-007 | FR-004 | Mentor submits complete scorecard | Saved, timestamped, linked to correct session |
| TC-008 | FR-004 | Student opens dashboard | Scorecard visible to student |
| TC-009 | FR-005 | Session due in the reminder window | Reminder sent to both parties |
| TC-010 | FR-005 | Cancel more than 4 hours before | Both calendars updated, other party notified |
| TC-011 | FR-005 | Cancel less than 4 hours before | Request rejected per policy |
| TC-012 | NFR-001 | Request account deletion | Data soft-deleted within 24 hours |
| TC-013 | NFR-001 | Access another user's scorecard | Access denied |
| TC-014 | NFR-002 | Two simultaneous bookings for one slot | Exactly one succeeds, the other gets A1 message |
| TC-015 | NFR-002 | Load test in simulated peak window | Availability meets 99.5% target |

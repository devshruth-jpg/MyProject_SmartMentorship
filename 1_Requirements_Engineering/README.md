# 1 - Requirements Engineering

This folder holds the requirements artefacts for the Alumni Mentorship & Mock Interview Platform.

| File | Description |
|---|---|
| `FR_NFR.md` | All functional (FR-001 to FR-005) and non-functional (NFR-001, NFR-002) requirements |
| `RTM.md` / `RTM.csv` | Requirements Traceability Matrix linking requirements to use cases, design components and test cases |
| `Requirements_Table.docx` | Original requirements table (Word) |
| `Use_Case_Flow_Specification.docx` | Flow specification for UC-01 Book Mentorship Session |
| `Use_Case_Diagram.pdf` | UML use-case diagram (includes one `<<include>>` and one `<<extend>>`) |

## Use Case Index

| ID | Use Case | Primary Actor |
|---|---|---|
| UC-01 | Book Mentorship Session | Student Mentee |
| UC-02 | Search & Match Mentor | Student Mentee |
| UC-03 | Generate Meeting Link (`<<include>>` of UC-01) | Video Conferencing System |
| UC-04 | Manage Availability | Alumni Mentor |
| UC-05 | Conduct Mock Interview | Alumni Mentor |
| UC-06 | Submit Scorecard | Alumni Mentor |
| UC-07 | View Feedback / Scorecard | Student Mentee |
| UC-08 | Reschedule Session (`<<extend>>` of UC-01) | Student Mentee |
| UC-09 | Cancel Session | Alumni Mentor / Student Mentee |
| UC-10 | Send Notification | Notification Service |

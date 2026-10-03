# Work Breakdown Structure (WBS)

**Project:** Alumni Mentorship & Mock Interview Platform
**Owner:** Devashruth

## Hierarchy

```
Alumni Mentorship Platform
├── 1. Requirements Engineering
├── 2. Design
├── 3. Project Setup and Management
├── 4. Documentation
├── 5. Implementation
├── 6. Testing
└── 7. Deployment
```

## Detailed Breakdown

| WBS ID | Task | Deliverable | Effort (hrs) | Depends on | Status |
|---|---|---|---|---|---|
| **1** | **Requirements Engineering** | | **14** | | |
| 1.1 | Identify stakeholders and actors | Actor list | 2 | | Done |
| 1.2 | Write functional and non-functional requirements | FR/NFR table | 4 | 1.1 | Done |
| 1.3 | Model use cases and diagram | Use-case diagram | 3 | 1.2 | Done |
| 1.4 | Write UC-01 flow specification | Flow specification | 3 | 1.3 | Done |
| 1.5 | Build RTM | RTM | 2 | 1.2, 1.3 | Done |
| **2** | **Design** | | **16** | | |
| 2.1 | Choose architecture style | Decision record | 2 | 1 | Done |
| 2.2 | Draw architecture diagram | Diagram | 4 | 2.1 | Done |
| 2.3 | Design database schema | ER diagram | 5 | 2.1 | Planned |
| 2.4 | Design REST API endpoints | API list | 3 | 2.1 | Planned |
| 2.5 | UI wireframes | Wireframes | 2 | 1.3 | Planned |
| **3** | **Project Setup and Management** | | **5** | | |
| 3.1 | Create GitHub repository and folder structure | Repository | 1 | | Done |
| 3.2 | Create Jira project and import backlog | Jira board | 2 | 1.2 | In progress |
| 3.3 | Capture setup screenshots | Folder 3 images | 1 | 3.1, 3.2 | In progress |
| 3.4 | Plan sprints | Sprint plan | 1 | 3.2 | Planned |
| **4** | **Documentation** | | **8** | | |
| 4.1 | Write SRS | SRS v1.0 | 5 | 1, 2.2 | Done |
| 4.2 | Write WBS | WBS | 1 | 4.1 | Done |
| 4.3 | Write READMEs | READMEs | 2 | | Done |
| **5** | **Implementation** | | **60** | | |
| 5.1 | Auth and profile module | Module | 10 | 2.3 | Planned |
| 5.2 | Mentor matching module | Module | 8 | 5.1 | Planned |
| 5.3 | Availability manager and cache | Module | 12 | 5.1 | Planned |
| 5.4 | Booking engine with locking | Module | 14 | 5.3 | Planned |
| 5.5 | Meeting-link and calendar adapters | Adapters | 6 | 5.4 | Planned |
| 5.6 | Scorecard module | Module | 5 | 5.4 | Planned |
| 5.7 | Notifications and reminders | Module | 5 | 5.4 | Planned |
| **6** | **Testing** | | **20** | | |
| 6.1 | Write test plan and cases (TC-001 to TC-015) | Test plan | 4 | 1.5 | Planned |
| 6.2 | Unit tests | Test suite | 6 | 5 | Planned |
| 6.3 | Concurrency test (NFR-002) | Test report | 4 | 5.4 | Planned |
| 6.4 | Integration and acceptance tests | Test report | 6 | 5 | Planned |
| **7** | **Deployment** | | **8** | | |
| 7.1 | Environment and infrastructure setup | Setup notes | 4 | 5 | Planned |
| 7.2 | Deploy and smoke test | Live build | 4 | 7.1, 6 | Planned |

**Total estimated effort: 131 hours**

## Milestones

| Milestone | Includes |
|---|---|
| M1 - Requirements complete | WBS 1 |
| M2 - Design and SRS complete | WBS 2.1, 2.2, 4 |
| M3 - Project tracking in place | WBS 3 |
| M4 - Core booking working | WBS 5.1 to 5.5 |
| M5 - Release | WBS 6, 7 |

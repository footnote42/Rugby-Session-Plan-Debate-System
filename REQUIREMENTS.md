# Requirements

## High-Level Aims
- Provide a lightweight web application for coaches and teams to propose, discuss, and debate rugby session plans.
- Focus on modularity and testability to allow incremental improvements.
- Ensure clear UX for proposing plans, reading debates, and casting votes.

## Problem Statement
Many coaches maintain session plans locally or in disparate files. This project aims to centralize proposals and provide a transparent debate mechanism to help teams make evidence-based decisions on session changes.

## Functional Requirements
- Create and edit session plans (title, objectives, steps/drills, duration, tags).
- Attach debate threads to a plan with comments and votes.
- Query session plans (list, filter by tags, search by title/objectives).
- Basic admin/moderator features (delete or archive plans).

## Non-Functional Constraints
- Keep the initial system small and hostable locally.
- Use in-memory or file-based persistence for Stage 1; plan for database integration in Stage 2.
- Implement API tests and simple UI tests.
- Keep dependencies minimal and permissive licenses.

## Security and Privacy
- No personally identifiable information in Stage 1 beyond display names.
- Provide roles for future authorization design (owner, contributor, moderator, viewer).

## Acceptance Criteria
- Users can propose a plan, add comments, and vote in a testable flow.
- The app is understandable and extensible (clean APIs and README).
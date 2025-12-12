# Domain Notes: Rugby Session Plan Debate System

## Actors
- Coach: Proposes, edits session plans.
- Player/Support Staff: Comments and votes on plans.
- Moderator: Removes or archives plans and moderates debate.

## Session Plan Structure (conceptually)
- Title
- Objectives (1-3 short lines)
- Duration (minutes)
- Steps/Drills: list of segments with duration and instructions
- Tags: e.g., "attack", "defence", "lineout", "set-piece"
- CreatedBy, UpdatedBy, createdAt, updatedAt

## Debate
- Each plan may have multiple comment threads
- Votes are simple up/down on plans and optionally on comments
- Comments have timestamps, author (display name), and optional tags

## UX Considerations
- Keep list view simple with filterable tags
- Plan detail page should show steps and an inline debate panel
- Voting counts should be shown alongside comments and plans

## Initial Scope
- No authentication for Stage 1; store a displayName with each action
- Use file-storage when necessary for MVP (or in-memory)

## Useful Patterns
- Use short, composable endpoints: `/plans`, `/plans/:id`, `/plans/:id/comments`
- Keep frontend logic small; make components stateless where possible

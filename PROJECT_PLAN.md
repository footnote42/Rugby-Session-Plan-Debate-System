# Project Plan (Machine-Readable + Human)

---
# Machine-readable YAML block for parsers and automation
version: 1.0
project: Rugby Session Plan Debate System
owner: "Team"
milestones:
  - id: stage-0
    name: "Scaffold & discovery"
    summary: "Repository scaffold and artifact collection"
    start: 2025-12-01
    end: 2025-12-12
    tasks:
      - name: "Repo layout"
        done: true
      - name: "Project plan + requirements"
        done: true
  - id: stage-1
    name: "Minimal Viable Product (MVP)"
    summary: "Backend API + Frontend UI for proposing, debating, and voting on session plans"
    start: 2025-12-13
    end: 2026-01-15
    tasks:
      - name: "Session plan schema + API"
        done: false
      - name: "Frontend list and details UI"
        done: false
      - name: "Debate (comments + votes)"
        done: false
  - id: stage-2
    name: "Feature & scale"
    summary: "Persistence, auth, and collaboration features"
    start: 2026-01-16
    end: 2026-02-28
    tasks:
      - name: "Add database persistence"
        done: false
      - name: "Auth and permissions"
        done: false
      - name: "Real-time debate (optional)"
        done: false

acceptance_criteria:
  - id: ac-01
    text: "Create/Edit proposal and view a debate attached to a plan"
  - id: ac-02
    text: "Vote up/down and comment threads with timestamps"
  - id: ac-03
    text: "Automated tests for API endpoints and main UI flows"

---

## Human Guide

- Purpose: Implement a small, extendable debate system for rugby session plans.
- Stages: Use the YAML milestones above for tracking progress.
- Owner: Team will use this file as the single source-of-truth for the project plan.

## How to read this file
- The YAML block on top is machine-readable for CI, bots or task trackers.
- The human-readable section explains purpose and ownership. Please update both when schedule or scope change.
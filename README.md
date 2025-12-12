# Rugby Session Plan Debate System

A lightweight full-stack project to propose, discuss, and debate rugby session plans. This scaffold includes a simple Node.js backend and a Vite + React frontend.

Getting started

1. Install dependencies (root will install concurrently):

```bash
cd "c:/Coding Projects/Rugby-Session-Plan-Debate-System"
# If you use npm
npm install
npm run dev

# Or with pnpm
pnpm install
pnpm run dev
```

2. Open http://localhost:5173 for the frontend and http://localhost:3000 for the backend API.

Structure

- `backend/` - Express server that serves a simple in-memory API for session plans and debates.
- `frontend/` - Vite + React app for UI.

Next steps

- Add a database or persistence
- Add user auth and permissions
- Add collaborative editing or real-time debate features (WebSockets)

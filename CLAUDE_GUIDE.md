# Claude Code Behavioural Guide

This file documents behavioural instructions for Claude-style agents used to assist with this repository.

## Purpose
- Provide consistent assistant behavior for development and code generation.
- Keep changes minimal and documented; respect existing styles and tests.

## Behavioural Rules
- Keep changes small and single-purpose. Provide tests alongside code changes.
- Prefer explicit, simple solutions over clever, fragile ones.
- Explain design decisions in PR descriptions or commit messages.
- Maintainable commit messages: `feat`, `fix`, `docs`, `chore`, `test`.

## Security and Safety
- Do not add secrets or credentials to source files.
- Escalate design changes that meaningfully increase attack surface or PII handling.

## Testing and Verification
- Unit tests required for all APIs and utilities.
- Prefer code that is both deterministic and well-documented.

## When to Ask for Human Input
- Changes to high-level architecture (persistency model, auth requirements).
- When the requested change is ambiguous or conflicts with project goals.

## Example Prompt for Clarifying Changes
- "I plan to add feature X which adds Y endpoints and two tests. Do we want to: A) add a db dependency now, or B) keep file-based storage for MVP?"
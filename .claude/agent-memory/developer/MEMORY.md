# Developer Dave — Project Memory

## Repo Overview
- Minimal test repo for agentic workflow (developer + reviewer agents)
- No configured test/lint/build commands — use Node.js (v22) for JS code
- Branch naming: `issue/<number>-<slug>`

## Stack
- Node.js v22 available; no npm packages pre-installed (pytest not available)
- Use plain `node` with `assert` module for lightweight tests when no test runner is installed
- `require`-style CommonJS modules work fine

## Patterns
- Conventional commits: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`
- Commit message focuses on "why", not "what"

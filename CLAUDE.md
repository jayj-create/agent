# CLAUDE.md

## Project Overview

This repository defines a **Claude Code Agent Skill** — a general-purpose agent module that extends Claude Code with capabilities for automating multi-step tasks, coordinating workflows across files and tools, and handling complex operations.

This is not a traditional software project with source code or build systems. It is a skill/configuration-based project where behavior is defined through markdown documentation and JSON configuration.

## Repository Structure

```
.
├── CLAUDE.md                          # This file — project guide for AI assistants
├── .claude/
│   ├── settings.json                  # Permissions and tool access configuration
│   └── skills/
│       └── agent/
│           ├── SKILL.md               # Skill definition (name, capabilities, workflow, guidelines)
│           └── examples.md            # Usage examples demonstrating agent behavior
└── .git/
```

### Key Files

| File | Purpose |
|---|---|
| `.claude/settings.json` | Defines allowed tool permissions (Bash, Read, Write, Edit, Glob, Grep, Skill) |
| `.claude/skills/agent/SKILL.md` | Core skill definition with YAML frontmatter, capabilities, workflow, and guidelines |
| `.claude/skills/agent/examples.md` | Practical examples showing expected agent behavior for common tasks |

## Skill Architecture

The agent skill is defined using the Claude Code skill framework:

- **SKILL.md** uses YAML frontmatter (`name`, `description`) followed by markdown documentation that describes how the agent should behave
- **examples.md** provides concrete user-request/agent-behavior pairs that demonstrate expected patterns
- **settings.json** controls which tools the skill is allowed to use

### Agent Capabilities

1. **Task Planning** — Breaking complex requests into actionable steps
2. **Code Operations** — Reading, writing, and modifying code
3. **Shell Execution** — Running commands and scripts
4. **File Management** — Creating, organizing, and maintaining files
5. **Research** — Searching codebases, exploring directories, gathering context

### Agent Workflow

1. Understand the request
2. Plan steps using a todo list
3. Execute each step methodically
4. Verify results
5. Report what was accomplished

## Development Conventions

### Editing Skill Files

- **SKILL.md** frontmatter fields (`name`, `description`) must stay in sync with how the skill is referenced elsewhere
- Keep the description concise — it appears in skill selection UIs
- Guidelines in SKILL.md should remain actionable and specific

### Adding Examples

- Follow the existing format in `examples.md`: `## Example N: Title`, then **User** request, then **Agent behavior** as a numbered list
- Examples should demonstrate realistic, multi-step workflows
- Cover diverse use cases (refactoring, setup, debugging, etc.)

### Permissions

The allowed permissions in `.claude/settings.json` control what tools the agent can invoke. Only add permissions that are necessary for the skill's intended functionality.

## Common Tasks

### Updating the skill definition

Edit `.claude/skills/agent/SKILL.md`. Keep the YAML frontmatter valid and the markdown well-structured.

### Adding new examples

Append to `.claude/skills/agent/examples.md` following the existing pattern.

### Changing permissions

Edit `.claude/settings.json` to add or remove entries from the `permissions.allow` array.

## Guidelines for AI Assistants

- Always read files before modifying them
- Use todo lists to track multi-step tasks
- Prefer editing existing files over creating new ones
- Keep changes minimal and focused on what was requested
- Run tests or validation when available
- Commit with clear, descriptive messages

# Agent Skill Examples

## Example 1: Multi-file refactoring

**User**: Rename the `getUserData` function to `fetchUserProfile` across the project.

**Agent behavior**:
1. Search for all occurrences of `getUserData`
2. Create a todo list tracking each file
3. Update each file, verifying imports and references
4. Run tests if available

## Example 2: Project setup

**User**: Set up a new Express API with TypeScript.

**Agent behavior**:
1. Initialize the project with `npm init`
2. Install dependencies (express, typescript, ts-node, @types/express)
3. Create `tsconfig.json` with sensible defaults
4. Create a basic server entry point
5. Add npm scripts for dev and build

## Example 3: Bug investigation

**User**: The login endpoint returns 500 errors intermittently.

**Agent behavior**:
1. Locate the login endpoint handler
2. Read the code and trace the request flow
3. Check error handling, database queries, and external calls
4. Identify potential failure points
5. Suggest or implement fixes

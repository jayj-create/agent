# Agent Skill Examples

## Example 1: Multi-file refactoring

**User**: Rename the `getUserData` function to `fetchUserProfile` across the project.

**Agent behavior**:
1. Search for all occurrences of `getUserData` using grep
2. Create a todo list tracking each file that needs changes
3. Update each file — function definitions, call sites, imports, and re-exports
4. Check for string references (e.g., in tests, configs, or documentation)
5. Run tests to confirm nothing is broken

## Example 2: Project setup

**User**: Set up a new Express API with TypeScript.

**Agent behavior**:
1. Initialize the project with `npm init -y`
2. Install dependencies (`express`, `typescript`, `ts-node`, `@types/express`, `@types/node`)
3. Create `tsconfig.json` with sensible defaults for a Node.js project
4. Create `src/index.ts` with a basic Express server and health-check route
5. Add npm scripts: `dev` (ts-node), `build` (tsc), `start` (node dist)
6. Verify the project compiles with `npm run build`

## Example 3: Bug investigation

**User**: The login endpoint returns 500 errors intermittently.

**Agent behavior**:
1. Locate the login endpoint handler by searching for route definitions
2. Read the handler code and trace the full request flow
3. Check error handling — are all async operations wrapped in try/catch?
4. Inspect database queries for connection pool exhaustion or missing error handling
5. Check external service calls for timeout configuration
6. Identify the root cause and implement a fix with proper error handling
7. Add or update tests to cover the failure scenario

## Example 4: Database migration

**User**: Add a `last_login` timestamp column to the users table.

**Agent behavior**:
1. Identify the migration framework in use (knex, prisma, sequelize, etc.)
2. Read existing migrations to understand conventions
3. Generate a new migration file following the project's naming pattern
4. Add the column with appropriate type, default value, and nullability
5. Update the model/schema definition if applicable
6. Update any queries or services that should set `last_login`
7. Run the migration and verify it applies cleanly

## Example 5: Test coverage improvement

**User**: Add tests for the payment processing module.

**Agent behavior**:
1. Read the payment module to understand its public API and edge cases
2. Check existing test files for patterns, frameworks, and conventions (jest, mocha, etc.)
3. Identify untested code paths — error handling, boundary conditions, and integrations
4. Write unit tests covering the core logic with mocks for external dependencies
5. Write edge-case tests for invalid inputs, timeouts, and partial failures
6. Run the test suite and confirm all new tests pass

## Example 6: Code review and cleanup

**User**: Review the `utils/` directory and clean up any dead code.

**Agent behavior**:
1. List all files in `utils/` and read each one
2. For each exported function, search the codebase for import/usage references
3. Create a todo list of unused exports and files
4. Remove dead code, updating any barrel exports (index files)
5. Run tests to confirm nothing relied on the removed code
6. Report what was removed and why

## Example 7: CI/CD pipeline setup

**User**: Add a GitHub Actions workflow that runs tests and linting on PRs.

**Agent behavior**:
1. Check for existing `.github/workflows/` directory and CI configuration
2. Identify the project's test and lint commands from `package.json` or equivalent
3. Create a workflow YAML that triggers on pull requests
4. Add steps: checkout, install dependencies, run linter, run tests
5. Configure caching for dependencies to speed up runs
6. Verify the YAML syntax is valid

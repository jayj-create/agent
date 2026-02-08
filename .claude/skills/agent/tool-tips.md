# Tool Tips & Common Patterns

Practical patterns for accomplishing common tasks efficiently.

## Searching Code

### Find all files matching a pattern
Use `Glob` to find files by name or extension:
- `**/*.ts` — all TypeScript files
- `src/**/*.test.js` — all test files under `src/`
- `**/config.*` — any config file at any depth

### Find code by content
Use `Grep` to search for patterns inside files:
- Search for function definitions: `function handleSubmit` or `def process_payment`
- Search for imports: `from.*module_name` or `require\(.*module_name`
- Search for TODO/FIXME comments: `TODO|FIXME|HACK`

### Trace a symbol through the codebase
1. Grep for the symbol name to find all references
2. Read the definition file to understand the interface
3. Read each call site to understand how it's used
4. Check test files for expected behavior

## Making Safe Changes

### Edit a function
1. Read the file to see current implementation
2. Find the exact string to replace (include enough context for uniqueness)
3. Use `Edit` with `old_string` / `new_string`
4. Read the file again to verify the edit applied correctly

### Rename a symbol across multiple files
1. Grep for the symbol to get all file paths
2. For each file, read it, then edit the occurrences
3. Use `replace_all: true` when renaming within a single file
4. Run tests after all renames are complete

### Add a new file to an existing project
1. Read similar files to understand conventions (naming, imports, exports)
2. Read any barrel/index files that may need updating
3. Write the new file following existing patterns
4. Update barrel exports if the project uses them

## Running Commands

### Install dependencies
- Node.js: `npm install` or `npm ci` (CI-safe)
- Python: `pip install -r requirements.txt` or `pip install -e .`
- Go: `go mod tidy`

### Run tests
- Check `package.json` scripts, `Makefile`, or `pyproject.toml` for the correct command
- Common patterns: `npm test`, `pytest`, `go test ./...`, `make test`
- Run specific tests: `npm test -- --grep "pattern"`, `pytest -k "test_name"`

### Check for issues
- Linting: `npm run lint`, `flake8`, `golangci-lint run`
- Type checking: `npx tsc --noEmit`, `mypy .`
- Build: `npm run build`, `go build ./...`, `make build`

## Project Structure Discovery

### Understand a new project quickly
1. Read `README.md` for overview and setup instructions
2. Check package manager files (`package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`)
3. Look at the directory structure with `ls` or `Glob`
4. Read configuration files (tsconfig, eslint, docker-compose)
5. Check test directories to understand expected behavior

### Find the entry point
- Node.js: check `main` or `scripts.start` in `package.json`
- Python: look for `__main__.py`, `app.py`, or `manage.py`
- Go: look for `main.go` or `cmd/` directory
- Docker: read `Dockerfile` for `CMD` or `ENTRYPOINT`

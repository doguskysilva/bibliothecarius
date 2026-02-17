# Bibliothecarius

Bibliothecarius is the database builder for Scripturas.

It exists to create and keep a prepopulated SQLite database with:

- books
- canons
- translations
- verses

This database is generated from CSV resources and consumed by the Scripturas app.

## Why this project exists

Scripturas needs a consistent and reproducible Bible dataset.
Bibliothecarius centralizes this process so data can be versioned, validated, and rebuilt in any environment (local or CI) with the same result.

## Architecture

The project follows a simple layered architecture:

1. **Input resources** (`resources/*.csv`, `resources/bibles/*.csv`, `resources/canons/*.csv`)
2. **CLI layer** (`bibliothecarius.main`) exposes sync/check commands
3. **Controller layer** (`bibliothecarius.controller`) orchestrates import flows and validations
4. **Mapper layer** (`bibliothecarius.mappers`) converts CSV rows into internal entities
5. **Repository layer** (`bibliothecarius.repository`) persists/query data with SQLAlchemy
6. **Model layer** (`bibliothecarius.models.*`) defines tables and relationships
7. **Database layer** (SQLite + Alembic migrations)

### Data flow

`CSV resources -> CLI command -> controller -> mappers -> repositories -> SQLite database`

### Database schema

Main tables:

- `books`
- `canons`
- `book_canon`
- `translations`
- `verses`

Schema creation and updates are managed by Alembic migrations in `alembic/versions`.

## Developer setup

Install and sync dependencies:

```bash
uv sync
```

Run commands inside project environment:

```bash
uv run <command>
```

## Build complete database (recommended)

Use the Makefile pipeline:

```bash
make db-build
```

This will reset the database, run migrations, import resources, and run bible consistency checks.

## Useful commands

Restart database schema:

```bash
rm database/scripturas.sqlite && uv run alembic -x data=true upgrade head
```

Load books:

```bash
uv run bibliothecarius books-sync ./resources/books.csv
```

Load canons:

```bash
uv run bibliothecarius canons-sync ./resources/canons.csv
```

Add books to a canon:

```bash
uv run bibliothecarius canon-books-sync  --canon roman_catholics --books ./resources/canons/roman_catholic_canon.csv
```

List a canon:

```bash
uv run bibliothecarius books-list --canon protestant
```

Load translations:

```bash
uv run bibliothecarius translations-sync ./resources/translations.csv
```

List translations:

```bash
uv run bibliothecarius translations-list
```

Load a bible:

```bash
uv run bibliothecarius bible-sync --translation 3001 --bible ./resources/bibles/nvi.csv
```

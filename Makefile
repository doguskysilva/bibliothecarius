UV ?= uv
ALEMBIC ?= $(UV) run alembic
APP ?= $(UV) run bibliothecarius
PYTEST_CMD ?= $(UV) run pytest
INSTALL_CMD ?= $(UV) sync

DB_FILE ?= database/scripturas.sqlite
APP_DB_FILE ?= database/scripturas-app.sqlite
DATABASE_URL ?= sqlite:///$(DB_FILE)
export DATABASE_URL

BOOKS_FILE ?= resources/books.csv
CANONS_FILE ?= resources/canons.csv
TRANSLATIONS_FILE ?= resources/translations.csv

ROMAN_CANON_FILE ?= resources/canons/roman_catholic_canon.csv
PROTESTANT_CANON_FILE ?= resources/canons/protestant_canon.csv

NVI_FILE ?= resources/bibles/nvi.csv
ARA_FILE ?= resources/bibles/ara.csv
AVM_FILE ?= resources/bibles/avm.csv

NVI_ID ?= 3001
ARA_ID ?= 3002
AVM_ID ?= 3003

.PHONY: help install test db-migrate db-reset db-rebuild db-seed db-build db-app-copy \
	books-sync canons-sync canon-books-sync translations-sync bibles-sync \
	bible-check-all translations-list

help:
	@echo "Available commands:"
	@echo "  make install           - Install dependencies"
	@echo "  make test              - Run test suite"
	@echo "  make db-migrate        - Apply Alembic migrations"
	@echo "  make db-reset          - Remove SQLite DB file"
	@echo "  make db-rebuild        - Reset DB and migrate"
	@echo "  make books-sync        - Load books from CSV"
	@echo "  make canons-sync       - Load canons from CSV"
	@echo "  make canon-books-sync  - Attach books to supported canons (roman_catholics, protestant)"
	@echo "  make translations-sync - Load translations from CSV"
	@echo "  make bibles-sync       - Load all bible texts"
	@echo "  make bible-check-all   - Validate loaded bible totals"
	@echo "  make db-seed           - Load all seed resources"
	@echo "  make db-build          - Full rebuild + seed + check"
	@echo "  make db-app-copy       - Duplicate DB and remove alembic_version table"
	@echo "  make translations-list - Show translation ids"

install:
	$(INSTALL_CMD)

test:
	$(PYTEST_CMD)

db-migrate:
	$(ALEMBIC) -x data=true upgrade head

db-reset:
	rm -f $(DB_FILE)

db-rebuild: db-reset db-migrate

books-sync:
	$(APP) books-sync $(BOOKS_FILE)

canons-sync:
	$(APP) canons-sync $(CANONS_FILE)

canon-books-sync:
	$(APP) canon-books-sync --canon roman_catholics --books $(ROMAN_CANON_FILE)
	$(APP) canon-books-sync --canon protestant --books $(PROTESTANT_CANON_FILE)

translations-sync:
	$(APP) translations-sync $(TRANSLATIONS_FILE)

translations-list:
	$(APP) translations-list

bibles-sync:
	$(APP) bible-sync --translation $(NVI_ID) --bible $(NVI_FILE)
	$(APP) bible-sync --translation $(ARA_ID) --bible $(ARA_FILE)
	$(APP) bible-sync --translation $(AVM_ID) --bible $(AVM_FILE)

bible-check-all:
	$(APP) bible-check --translation $(NVI_ID)
	$(APP) bible-check --translation $(ARA_ID)
	$(APP) bible-check --translation $(AVM_ID)

db-seed: books-sync canons-sync canon-books-sync translations-sync bibles-sync

db-build: db-rebuild db-seed bible-check-all

db-app-copy:
	cp $(DB_FILE) $(APP_DB_FILE)
	sqlite3 $(APP_DB_FILE) "DROP TABLE IF EXISTS alembic_version;"

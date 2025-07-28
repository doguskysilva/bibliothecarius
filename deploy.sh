#!/bin/bash

# Activate poetry environment
eval $(poetry env activate)

# Remove existing database if it exists and run migrations
[ -f database/scripturas.sqlite ] && rm database/scripturas.sqlite
alembic -x data=true upgrade head

# Load books
bibliothecarius books-sync ./resources/books.csv

# Load canons
bibliothecarius canons-sync ./resources/canons.csv

# Add books to a canon (example: roman_catholics)
bibliothecarius canon-books-sync --canon roman_catholics --books ./resources/canons/roman_catholic_canon.csv

# Add books to a canon (example: protestant)
bibliothecarius canon-books-sync --canon protestant --books ./resources/canons/protestant_canon.csv

# Load translations
bibliothecarius translations-sync ./resources/translations.csv

# List translations
bibliothecarius translations-list

# Add bibles
bibliothecarius bible-sync --translation 3001 --bible ./resources/bibles/nvi.csv
bibliothecarius bible-sync --translation 3002 --bible ./resources/bibles/ara.csv
bibliothecarius bible-sync --translation 3003 --bible ./resources/bibles/avm.csv
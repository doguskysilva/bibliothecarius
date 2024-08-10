# Bibliothecarius

## Developer

To activate virtual environement use 
```bash
poetry shell
```

To leave
```bash
exit
```

## To restart database
```bash
rm database/scripturas.sqlite &&  alembic -x data=true upgrade head
```

## Load books
```bash
bibliothecarius books-sync ./resources/books.csv
```

## Load canons
```bash
bibliothecarius canons-sync ./resources/canons.csv
```

## Add books to a canon
```bash
bibliothecarius canons-books-sync  --canon roman_catholic --books ./resources/canons/roman_catholic_canon.csv
```

## List a canon
```bash
bibliothecarius books-list --canon protestant
```
## Load translations
```bash
bibliothecarius translations-sync ./resources/translations.csv
```

## List translations
```bash
bibliothecarius translations-list
```

## Add a bible
```bash
bibliothecarius bible-sync --translation 3001 --bible ./resources/bibles/nvi.csv
```
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
bibliothecarius sync-books ./resources/books.csv
```

## Load canons
```bash
bibliothecarius sync-canons ./resources/canons.csv
```

## Add books to a canon
```bash
bibliothecarius relation-canon-books  --canon roman_catholic --books ./resources/canons/roman_catholic_canon.csv
```

## List a canon
```bash
bibliothecarius list-books --canon protestant
```
## Load translations
```bash
bibliothecarius sync-translations ./resources/translations.csv
```

## Add a bible
```bash
bibliothecarius bible-add --translation 3001 --verses ./resources/bibles/nvi.csv
```
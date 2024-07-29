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

## To load books
```bash
bibliothecarius sync-books ./resources/books.csv
```

## To load canons
```bash
bibliothecarius sync-canons ./resources/canons.csv
```

## Add books to a canon
```bash
bibliothecarius relation-canon-books  --canon roman_catholic --books ./resources/canons/roman_catholic_canon.csv
```


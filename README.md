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
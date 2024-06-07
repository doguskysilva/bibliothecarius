import csv

from bibliothecarius.mappers import row_to_book

def sync_books():
    with open(f"resources/books.csv", "r") as text_wrapper:
        csv_reader = csv.DictReader(text_wrapper, delimiter=";")
        for row in csv_reader:
            book = row_to_book(row)
            print(book)


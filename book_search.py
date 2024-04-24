def search_books_by_author(books, author):
    found_books = [book for book in books if book.author == author]
    if found_books:
        print(f"Books by {author}:")
        for book in found_books:
            print(book)
    else:
        print(f"No books found by {author}.")
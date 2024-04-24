class Library:
    def __init__(self, book_name, author, pages, description):
        self.book_name = book_name
        self.author = author
        self.pages = pages
        self.description = description
        self.is_borrowed = False

    def __str__(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"Title: {self.book_name}\nAuthor: {self.author}\nPages: {self.pages}\nDescription: {self.description}\nStatus: {status}"

    def borrow_book(self, duration):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"{self.book_name} has been borrowed for {duration} days.")
            print("Terima kasih telah meminjam.")
        else:
            print(f"{self.book_name} is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"{self.book_name} has been returned.")
            print("Terima kasih telah mengembalikan.")
        else:
            print(f"{self.book_name} is not borrowed.")


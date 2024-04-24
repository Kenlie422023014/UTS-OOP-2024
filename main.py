from library import Library
from book_search import search_books_by_author

if __name__ == "__main__":
    # List array buku untuk E-Library
    books_data = [
        {"book_name": "Python Programming", "author": "Sandhika Galih", "pages": 300, "description": "A comprehensive guide to Python programming language."},
        {"book_name": "Machine Learning Basics", "author": "Dea Afrizal", "pages": 250, "description": "Introduction to basic concepts of machine learning."},
        {"book_name": "Data Structures and Algorithms", "author": "Syahar Alamsyiah", "pages": 500, "description": "Explains various data structures and algorithms."},
        {"book_name": "Deep Learning Fundamentals", "author": "Kenneth", "pages": 350, "description": "Introduction to deep learning concepts."},
        {"book_name": "Web Development with Laravel and PHP", "author": "Felixius", "pages": 180, "description": "Learn web development using Laravel and PHP."},
        {"book_name": "Game Development With Unity Engine", "author": "Bambang", "pages": 270, "description": "Learn web development using Django framework."},
        {"book_name": "How to Program in C", "author": "Tanaka", "pages": 300, "description": "Learn Game Development With Unity Engine"},
        {"book_name": "Data Science Basic", "author": "Kelvin W.W", "pages": 280, "description": "Learn the fundamental of Data Science."},
        {"book_name": "Basic 3D in Blender", "author": "Yasuo", "pages": 200, "description": "Learn the basic of 3d."},
        {"book_name": "IOT and Its benefits", "author": "Darius", "pages": 250, "description": "Learn IOT and many more."},

    ]

    # Create an array of Library objects
    lib = [Library(book['book_name'], book['author'], book['pages'], book['description']) for book in books_data]

    # Keep track of the number of books available in the library
    count = len(lib)

    # Iterate the loop
    while True:
        print("\n\n----------WELCOME TO UKRIDA E-LIBRARY ---------\n")
        print("1. Display book information\n2. Search books by author\n",
              "3. Borrow a book\n4. Return a book\n5. List the count of books in the library\n6. Exit\n")

        # Enter the user choice
        input_choice = input("Enter one of the above: ")

        # Process the input
        if input_choice == '1':
            print("You have entered the following information:")
            for book in lib:
                print(book)
        elif input_choice == '2':
            ar_nm = input("Enter author name : ")
            search_books_by_author(lib, ar_nm)
        elif input_choice == '3':
            book_name = input("Enter the book name you want to borrow: ")
            duration = int(input("Enter the duration (in days) you want to borrow the book: "))
            for book in lib:
                if book.book_name == book_name:
                    book.borrow_book(duration)
                    break
            else:
                print(f"No book found with the name '{book_name}'")
        elif input_choice == '4':
            book_name = input("Enter the book name you want to return: ")
            for book in lib:
                if book.book_name == book_name:
                    book.return_book()
                    break
            else:
                print(f"No book found with the name '{book_name}'")
        elif input_choice == '5':
            print(f"\nNo of books in library : {count}\n")
        elif input_choice == '6':
            exit(0)

class Book:
    def __init__(self): (self, title, author, year)
        self.title = title
        self.author = author
        self.year = year
    
     def __str__(self):
        return f"(title) by (author) published in (year)"
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
     def __del__(self):
        print(f"Deleting {self.title}")

    from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()

#Expected Output
1984 by George Orwell, published in 1949
Book('1984', 'George Orwell', 1949)
Deleting 1984

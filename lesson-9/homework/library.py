class BookNotFoundException(BaseException):
    def __init__(self, message:str, *args, **kwargs):
        self.message = message
        super(). __init__(self.message, *args, **kwargs)

class BookAlreadyBorrowedException(Exception):
    def __init__(self, message: str, *args, **kwargs):
        self.message = message
        super(). __init__(self.message, *args, **kwargs)

class NumberLimitExceededException(Exception):
    def __init__(self, message:str, *args, **kwargs):
        self.message =message
        super(). __init__(self.message, *args, **kwargs)


        


class Book:
    def __init__(self, author:str, title:str, is_borrowed : bool = False):
        self.author = author
        self.title = title
        self.is_borrowed = is_borrowed
        
class Member:
    def __init__(self, member: str):
        self.member = member
        self.borrowed_books = []

    def can_borrow(self)-> bool:
        return len(self.borrowed_books) < 3
    
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_books(self, book :Book):
        self.books.append(book)

    def add_members(self, member: Member):
        self.members.append(member)

    def borrow_book(self, member:Member, book_title: str):
        book = next((b for b in self.books if b.title == book_title), None)
        if not book:
            raise BookNotFoundException(f"Book: '{book_title}' not found in the library")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"Book: '{book_title} is already borrowed")
        if not member.can_borrow():
            raise NumberLimitExceededException(f"You cannot borrow more than 3 books")
        book.is_borrowed = True
        member.borrowed_books.append(book)

    def return_book(self, member: Member, book_title: str):
        book = next((b for b in self.books if b.title == book_title), None)
        if not book:
            raise BookNotFoundException(f"Book '{book_title}' not found in the library.")
        if book not in member.borrowed_books:
            raise BookNotFoundException(f"Member '{member.member}' did not borrow '{book_title}'.")

      
        book.is_borrowed = False
        member.borrowed_books.remove(book)


library = Library()


library.add_books(Book("1984", "George Orwell"))
library.add_books(Book("To Kill a Mockingbird", "Harper Lee"))


member1 = Member("Alice")
library.add_members(member1)


try:
    library.borrow_book(member1, "1984")
    print(f"{member1.name} borrowed '1984'")
    library.borrow_book(member1, "To Kill a Mockingbird")
    print(f"{member1.name} borrowed 'To Kill a Mockingbird'")
    library.return_book(member1, "1984")
    print(f"{member1.name} returned '1984'")
except (BookNotFoundException, BookAlreadyBorrowedException, NumberLimitExceededException) as e:
    print(f"Error: {e}")

try:
    library.borrow_book(member1, "Nonexistent Book")
except BookNotFoundException as e:
    print(f"Error: {e}")

try:
    library.borrow_book(member1, "To Kill a Mockingbird")
except BookAlreadyBorrowedException as e:
    print(f"Error: {e}")

try:
    library.borrow_book(member1, "1984")
    library.borrow_book(member1, "To Kill a Mockingbird")
    library.borrow_book(member1, "1984") 
except NumberLimitExceededException as e:
    print(f"Error: {e}")
    

        







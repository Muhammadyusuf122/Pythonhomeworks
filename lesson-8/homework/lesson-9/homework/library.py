class BookNotFoundException(BaseException):
    def __init__(self, message:str, *args, **kwargs):
        self.message = message
        super(). __init__(*args, **kwargs)


try:
    raise BookNotFoundException("the book you are searching isnot found")
except BookNotFoundException as f:
    print(f)
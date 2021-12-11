"""
Represents a student enrolled in the college
"""

class Book:

    def __init__(self, bookID, title, author, genre):
        self._bookID = bookID
        self._title = title
        self._author = author
        self._genre = genre

    def getBookID(self):
        return self._bookID

    def getTitle(self):
        return self._title

    def getAuthor(self):
        return self._author

    def getGenre(self):
        return self._genre

    # override object.__str__
    def __str__(self):
        return f"{self.getBookID()},{self.getTitle()},{self.getAuthor()},{self.getGenre()}"

    
    @staticmethod
    def parse(studentAsString):
        fields = studentAsString.split(',')
        bookID = int(fields[0])
        title = fields[1]
        author = fields[2]
        genre = fields[3]
        return Book(bookID, title, author,genre)

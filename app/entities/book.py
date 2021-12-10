"""
Represents a student enrolled in the college
"""

class Book:

    def __init__(self, bookID, title, author):
        self._bookID = bookID
        self._title = title
        self._author = author

    def getBookID(self):
        return self._bookID

    def getTitle(self):
        return self._title

    def getAuthor(self):
        return self._author

    
"""
Manages a collection of books
"""
from app.entities.book import Book
import pandas as pd
from IPython.display import display
import json
class DuplicatebookError (Exception):
    pass


class BookDataManager:
    # constructor

    def __init__(self):
        self._dict = {}  # using a blank dictionary to hold book records

    def addbookRecord(self, bookID, title, author, genre):
        # add book record to the collection
        if bookID in self._dict:
            raise DuplicatebookError()
        self._dict[bookID] = Book(
            bookID, title, author, genre)

    def removebookRecord(self,bookID):
        # remove book record from collection
        if bookID in self._dict:
            self._dict.pop(bookID)
        else:
            raise Exception

    def searchbookRecord(self,bookID):
        # search for a book record
        if bookID in self._dict:
            temp = self._dict[bookID]
            display(temp)
        else:
            raise Exception

    def displayAllRecord(self):
        for bookID in self._dict:
            temp = self._dict[bookID]
            display(temp)

    def modifybookRecord(self,bookID,title,author, genre):
        # modify a record based on key
        if bookID in self._dict:
            self._dict[bookID] = Book(
            bookID, title, author, genre)
        else :
            raise Exception

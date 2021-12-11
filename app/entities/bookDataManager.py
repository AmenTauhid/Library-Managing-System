"""
Manages a collection of books
"""
from app.dataAccess.bookJsonManager import BookJsonManager
from app.entities.book import Book
import pandas as pd
from IPython.display import display
import json
class DuplicatebookError(Exception):
    pass


class BookDataManager:
    # constructor

    def __init__(self):
        self._dict = {}  # using a blank dictionary to hold book records


    def addbookRecord(self, bookID, title, author, genre):
        # add book record to the collection
        self._dict[bookID] = Book(
            bookID, title, author, genre)

    def preAddCheck(self,bookId):
        if bookId in self._dict:
            return True
        else: 
            return False

    def removebookRecord(self,bookID):
        # remove book record from collection
        if bookID in self._dict:
            self._dict.pop(bookID)
        else:
            raise Exception

    def searchbookID(self,bookID):
        # search for a book record
        if bookID in self._dict:
            temp = self._dict[bookID]
            display(temp)
        else:
            raise Exception

    '''
    def displayAllRecord(self):
        for bookID in self._dict:
            temp = self._dict[bookID]
            display(temp)
    '''
    def displayAllRecord(self):
        fd = open("books.json",'r')
        txt = fd.read()
        data = json.loads(txt)

        table = pd.DataFrame(
			columns=['BookID', 'title', 'author','genre'])
        for i in data.keys():
            temp = pd.DataFrame(columns=["BookID"])
            temp["BookID"] = [i]
            for j in data[i].keys():
                temp[j] = [data[i][j]]
            table = table.append(temp)
        table = table.reset_index(drop=True)
        display(table)

    def modifybookRecord(self,bookID,title,author, genre):
        # modify a record based on key
        if bookID in self._dict:
            self._dict[bookID] = Book(
            bookID, title, author, genre)
            return True
        else:
            return False

            
            
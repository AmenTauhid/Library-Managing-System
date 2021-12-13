"""
Manages a collection of books
"""
from app.dataAccess.bookJsonManager import BookJsonManager
from app.entities.book import Book
import pandas as pd
from IPython.display import display 
import json

class BookDataManager:

    def __init__(self):
        self._dict = {}  

    def addBookRecord(self, bookID, title, author, genre):
        self._dict[bookID] = Book(
            bookID, title, author, genre)

    def preCheck(self,bookId):
        if bookId in self._dict:
            return True
        else: 
            return False

    def removeBookRecord(self,bookID):
        self._dict.pop(bookID)

    def searchBookID(self,bookID):
        temp = self._dict[bookID]
        display(temp)

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

    def modifyBookRecord(self,bookID,title,author, genre):
        # modify a record based on key
        self._dict[bookID] = Book(
        bookID, title, author, genre)



            
            
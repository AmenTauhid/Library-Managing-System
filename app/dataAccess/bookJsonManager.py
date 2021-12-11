#with open(r"D:\College resources\PROG10004\Source Files\Assignment 4\books.json", "w") as f:
 #   pass

"""
Responsible for saving/reading book records as JSON
"""
from app.entities.book import Book
import json


class BookJsonManager:

    def __init__(self, fileName):
        self._fileName = fileName

    @staticmethod
    def toJson(obj):
        result = {}
        for key in obj.__dict__:
            if key[0] == '_':
                result[key[1:]] = obj.__dict__[key]
            else:
                result[key] = obj.__dict__[key]
        return result

    def writeToFile(self, bookDict):
        """
        Args:
        bookDict: the dictionary containing studnet records to be saved
        """
        with open(self._fileName, "w") as fileRef:
            json.dump(bookDict, fileRef, default=BookJsonManager.toJson)

    def readFromFile(self):
        # start with a blank dictionary
        result = {}  # holds the final results
        bookJsonRecs = {}  # holds the data read from the file
        # open the file to get a dictionary of dictionaries
        with open(self._fileName, "r") as fileRef:
            # gives a dictionary of dictionaries
            bookJsonRecs = json.load(fileRef)

        # iterate through the top dictionary to get one book dictionary
        for bookID in bookJsonRecs:  # the key is the book number
            bookJson = bookJsonRecs[bookID]
            # convert the book dictionary to a book object
            # unpacks the JSON into parameters for the function
            bookObj = Book(**bookJson)
            # add the book object to the result
            result[int(bookID)] = bookObj
        return result

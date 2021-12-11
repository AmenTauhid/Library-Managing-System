
import os
import sys
import time
from app.entities.bookDataManager import BookDataManager
from app.dataAccess.bookJsonManager import BookJsonManager
class MainUI:
    dataManager = BookDataManager()
    jsonManager = BookJsonManager("books.json")
    @classmethod
    def run(cls):
        cls.dataManager._dict = cls.jsonManager.readFromFile()
        os.system("cls")
        print("========= Welcome to the Library =========")
        print("1)Display all books with there details")
        print("2)Display a specific book with its details")
        print("3)Add new book the library")
        print("4)Update a book in the library")
        print("5)Delete a book in the library")
        print("6)Exit")
        print("=========================================")
        while True:
            n = str(input("Enter Your Choice :"))
            l1 = ["1","2","3","4","5","6"]
            while n != l1:
                if (n == "1"):
                    cls.dataManager.displayAllRecord()
                    break
                elif (n == "2"):
                    bookID = int(input('Enter the ID of the book: '))
                    cls.dataManager.searchbookRecord(bookID)
                    break
                elif (n == "3"):
                    bookID = int(input('Enter the student no: '))
                    title = input('Enter the title: ')
                    author = input('Enter the name of the author: ')
                    genre = input('Enter the genre:')
                    cls.dataManager.addbookRecord(bookID,title,author,genre)
                    break
                elif (n == "4"):
                    bookID = int(input('Enter the ID: '))
                    title = input('Enter the  title: ')
                    author = input('Enter the author name: ')
                    genre = input('Enter the genre:')
                    cls.dataManager.modifybookRecord(bookID,title,author,genre)
                    break
                elif (n == "5"):
                    bookID = int(input('Enter the ID of the book you wish to remove:'))
                    cls.dataManager.removebookRecord(bookID)
                    break
                elif (n == "6"):
                    print("Thank you for using the libray system")
                    time.sleep(1.5)
                    sys.exit()
                else:
                    n = str(input("Invalid Choice...!!!\nPlease enter a valid option:")) 
            cls.jsonManager.writeToFile(cls.dataManager._dict)
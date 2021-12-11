
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
                    print("\nPreparing the list...\n")
                    time.sleep(2)
                    print("Fetching the list...\n")
                    time.sleep(1.5)
                    cls.dataManager.displayAllRecord()
                    print("")
                    break
                elif (n == "2"):
                    MainUI.searchingBook()
                elif (n == "3"):
                    MainUI.addABook()
                elif (n == "4"):
                    bookID = int(input('Enter the ID of the book you wish to modify: '))
                    title = input('Enter the  title: ')
                    author = input('Enter the author name: ')
                    genre = input('Enter the genre:')
                    cls.dataManager.modifybookRecord(bookID,title,author,genre)
                    if cls.dataManager.modifybookRecord(bookID,title,author,genre) is True:
                        print("Book with ID",bookID,"modified successfully!\n")
                        break
                    elif cls.dataManager.modifybookRecord(bookID,title,author,genre) is False:
                        print("Given ID of the book does not exist in the library!")
                elif (n == "5"):
                    MainUI.deleteBook()
                elif (n == "6"):
                    print(" ")
                    print("Thank you for using the libray system\n")
                    time.sleep(1.5)
                    sys.exit()
                else:
                    n = str(input("Invalid Choice...!!!\nPlease enter a valid option:")) 
            cls.jsonManager.writeToFile(cls.dataManager._dict)

    @classmethod
    def searchingBook(cls):
        cls.dataManager._dict = cls.jsonManager.readFromFile()
        choice = str(input("\nHow do you wish to search for the book?\n1)ID of the book\n2)Genre of the book\n3)Go Back\n>"))
        l2 = ["1","2","3"]
        while choice != l2:
            if (choice == "1"):
                bookID = int(input('\nEnter the ID of the book\n>'))
                print('')
                cls.dataManager.searchbookID(bookID)
                break
            elif choice=="2":
                #genre = str(input("\nEnter the genre of the book you wish to search for\n>"))
                #print('')
                #cls.dataManager.searchbookGenre(genre)
                #break
                pass
            elif choice=="3":
                MainUI.run()
            else:
                choice = str(input("\nInvalid Choice...!!!\nPlease enter a valid option\n>"))
    
    @classmethod
    def deleteBook(cls):
        cls.dataManager._dict = cls.jsonManager.readFromFile()
        bookID = int(input('Enter the ID of the book you wish to remove or if you want to go back enter 0\n>'))
        while True:
            if bookID != 0:
                cls.dataManager.removebookRecord(bookID)
                print("Book with ID",bookID,"removed from the library successfully!\n")
                time.sleep(1.5)
                break
            elif bookID == 0: 
                MainUI.run()
            else:
                bookID = int(input("Invalid ID/option...!!!\nPlease enter a valid option\n>"))
        cls.jsonManager.writeToFile(cls.dataManager._dict)
        
    @classmethod
    def addABook(cls):
        cls.dataManager._dict = cls.jsonManager.readFromFile()
        while True:
            bookID = int(input('Enter a new ID for the book or enter 0 if you want to go back\n>'))
            if bookID > 0:
                if cls.dataManager.preAddCheck(bookID) is False:
                    title = input('Enter the title: ')
                    author = input('Enter the name of the author: ')
                    genre = input('Enter the genre:')
                    cls.dataManager.addbookRecord(bookID,title,author,genre)
                    print("\nNew book with ID",bookID,"added to the library successfully!\n")
                    time.sleep(1.5)
                    break
                elif cls.dataManager.preAddCheck(bookID) is True:
                    print("Entered ID of the book already exists!\nPlease choose a new one\n>")
                    break
            elif bookID == 0:
                MainUI.run()
            else:
                bookID = int(input('Please enter a valid ID/option: '))
        cls.jsonManager.writeToFile(cls.dataManager._dict)
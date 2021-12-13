
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
                    MainUI.updateBook()
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
            try:
                if (choice == "1"):
                    bookID = int(input('\nEnter the ID of the book\n>'))
                    if cls.dataManager.preCheck(bookID) is True:
                        print('')
                        print("Fetching the list...\n")
                        time.sleep(1)
                        cls.dataManager.searchBookID(bookID)
                        time.sleep(1)
                        break
                    elif cls.dataManager.preCheck(bookID) is False:
                        print("\nEntered ID of the book does not exist!\nPlease enter a valid one\n")
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
                    raise ValueError
            except ValueError as e:
                e = ValueError("\nInvalid input/Inavlid ID")
                print(e)
                time.sleep(1)
                break
    @classmethod
    def deleteBook(cls):
        cls.dataManager._dict = cls.jsonManager.readFromFile()
        while True:
            try:
                bookID = int(input('Enter the ID of the book you wish to remove or if you want to go back enter 0\n>'))
                if bookID > 0:
                    if cls.dataManager.preCheck(bookID) is True:
                        cls.dataManager.removeBookRecord(bookID)
                        print("Book with ID",bookID,"removed from the library successfully!\n")
                        time.sleep(1.5)
                        break
                    else:
                        raise ValueError
                elif bookID == 0: 
                    MainUI.run()
            except ValueError as e:
                e = ValueError("\nInvalid input/Invalid ID\n")
                time.sleep(1)
                print(e)
        cls.jsonManager.writeToFile(cls.dataManager._dict)
        
    @classmethod
    def addABook(cls):
        cls.dataManager._dict = cls.jsonManager.readFromFile()
        while True:
            try:
                bookID = int(input('Enter a new ID for the book or enter 0 if you want to go back\n>'))
                if bookID > 0:
                    if cls.dataManager.preCheck(bookID) is False:
                        title = input('Enter the title: ')
                        author = input('Enter the name of the author: ')
                        genre = input('Enter the genre:')
                        cls.dataManager.addBookRecord(bookID,title,author,genre.lower())
                        print("\nNew book with ID",bookID,"added to the library successfully!\n")
                        time.sleep(1.5)
                        break
                    elif cls.dataManager.preCheck(bookID) is True:
                        print("\nEntered ID of the book already exists!\nPlease choose a new one\n")
                        break
                    else:
                        raise ValueError
                elif bookID == 0:
                    MainUI.run()
            except ValueError as e:
                e = ValueError("\nInvalid input/Inavlid ID\n")
                print(e)
                time.sleep(1)
                break
        cls.jsonManager.writeToFile(cls.dataManager._dict)
    
    @classmethod
    def updateBook(cls):
        cls.dataManager._dict = cls.jsonManager.readFromFile()
        while True:
            try:
                bookID = int(input('Enter a the ID for the book you wish to update or enter 0 if you want to go back\n>'))
                if bookID > 0:
                    if cls.dataManager.preCheck(bookID) is True:
                        title = input('Enter the 1title: ')
                        author = input('Enter the author name: ')
                        genre = input('Enter the genre:')
                        cls.dataManager.modifyBookRecord(bookID,title,author,genre.lower())
                        print("Book with ID",bookID,"modified successfully!\n")
                        break
                    elif cls.dataManager.preCheck(bookID) is False:
                        print("Given ID of the book does not exist in the library!\nPlease enter a valid one\n")
                        break
                    else:
                        raise ValueError
                elif bookID == 0:
                    MainUI.run()
            except ValueError as e:
                e = ValueError("\nInvalid input/Inavlid ID\n")
                print(e)
                time.sleep(1)
                break
        cls.jsonManager.writeToFile(cls.dataManager._dict)
        
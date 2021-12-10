
import os
import sys
import time
class MainUI:

    @classmethod
    def run(cls):

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
                    pass
                    break
                elif (n == "2"):
                    bookID = int(input('Enter the ID of the book: '))
                    pass
                    break
                elif (n == "3"):
                    bookID = int(input('Enter the student no: '))
                    title = input('Enter the title: ')
                    author = input('Enter the name of the author: ')
                    pass
                    break
                elif (n == "4"):
                    bookID = int(input('Enter the ID: '))
                    title = input('Enter the  title: ')
                    author = input('Enter the author name: ')
                    pass
                    break
                elif (n == "5"):
                    bookID = int(input('Enter the ID of the book you wish to remove:'))
                    pass
                    break
                elif (n == "6"):
                    print("Thank you for using the libray system")
                    time.sleep(1.5)
                    sys.exit()
                else:
                    n = str(input("Invalid Choice...!!!\nPlease enter a valid option:")) 

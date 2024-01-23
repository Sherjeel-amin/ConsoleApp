from member import SpecialCredit, NormalCredit
from library import Library
from DataManager import JsonManager
import os
library = Library("Universe")

def intro():
    while True:
        print(
        """
         ~~~~~~~~~~< Welcome To Libra- A book rental store >~~~~~~~~~~
        | a. Register for Special credit                              |
        | b. Register for Normal credit                               | 
        | c. Login                                                    |
        | d. Exit                                                     |
         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)
        chose = input(">>> ").lower()

        # clear console
        os.system("cls")

        if chose == "a":
            feature = SpecialCredit.feature()
            print("---------------< Description >-------------------")
            print("Note: With Special credit, you can rent {} books.".format(feature["RentLimit"]))
            print("Rent time for every book: {} days".format(feature["ReturnTime"]))
            print("For delay in return book: you will block {} days".format(feature["BlockTime"]))
            print("-------------------------------------------------")
            input("Click Enter....")
            print("\n\n")

            print("~~~~~~~~~~~< Register >~~~~~~~~~~~")
            userName = input("Name:").strip()
            userId =   input("Id:").strip()
            userPass = input("Password:").strip()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
            # clear console
            os.system("cls")

            creditType = "Special"
            library.register(userId, userName, userPass, creditType)

        elif chose == "b":
            feature = NormalCredit.feature()
            print("~~~~~~~~~~~~~~~~~~~< Description >~~~~~~~~~~~~~~~~~~")
            print("| Note: With Special credit, you can rent {} books.".format(feature["RentLimit"]))
            print("| Rent time for every book: {} days".format(feature["ReturnTime"]))
            print("| For delay in return book: you will block for {} days".format(feature["BlockTime"]))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            input("Click Enter....")
            print("\n\n")

            print("~~~~~~~~~~~< Register >~~~~~~~~~~~")
            userName = input("Name:").strip()
            userId =   input("Id:").strip()
            userPass = input("Your Password :").strip()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            # clear console
            os.system("cls")

            creditType = "Normal"
            library.register(userId, userName, userPass, creditType)

        elif chose == "c":
            print("~~~~~~~~~~~< Login >~~~~~~~~~~~")
            userId =   input("Your id:").strip()
            userPass = input("Your password:").strip()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
            # clear console
            os.system("cls")

            respons = library.login(userId, userPass)
            if isinstance(respons, SpecialCredit) or isinstance(respons, NormalCredit):
                main(respons)

        elif chose == "d":
            print("exit...")
            exit()
       
        else:
            print("please select the options with a, b or c")

def accountSection(user):
    while True:
        print(
        """
          ~~~~~~~~~~< Account >~~~~~~~~~~~~~
        | a. Account/User Information       |
        | b. Back to Menu                   |
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)
        chose = input(">> ").lower()

        # clear console
        os.system("cls")

        if chose == "a":
            print("~~~~~~~~~~~~< Info >~~~~~~~~~~~~")
            print("Your Name: {}".format(user.name))
            print("Your Id: {}".format(user.Id))
            print("Credit Type: {}".format(user.creditType))
            print("Rented Books: {}".format(len(user.rentedBooks)))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            input("Click Enter...")

            # clear console
            os.system("cls")
        
        elif chose == "c":
            pass
        
        elif chose == "d":
            pass

        elif chose == "e":
           pass
        
        elif chose == "f":
            pass
        elif chose == "g":
            
            pass
        elif chose == "h":
            pass
                
        elif chose == "b":
            # clear console
            os.system("cls")

            print("Back...")
            break
        
        else:
            print("Please select options with (a or b)")
    
def main(user):
    """ user: an object of SpecialCredit or NormalCredit classes """

    while True:
        print("""
          ~~~~~~~~~~< Menu >~~~~~~~
        | a. Account               |
        | b. Books list            |
        | c. Rent a book           | 
        | d. Return a book         |
        | e. My rented book        |
        | f. Log out               |
        | g. Exit                  |
          ~~~~~~~~~~~~~~~~~~~~~~~~~
        """)
        chose = input(">> ").lower()
        
        # clear console
        os.system("cls")
        
        if chose == "a":
            accountSection(user)
        
        # elif chose == "b":
        #     print("Welcome to Libra")
        #     # print(library)
        
        elif chose == "b":
            books = user.libraryBooks
            print("~~~~~~~~~~~~~~~< Books >~~~~~~~~~~~~~~~")
            for bookId, info in books.items():
                print("{} :: {} - {}; Rented: {}".format(
                    bookId,
                    info["Name"],
                    info["Autor"],
                    "Yes" if info["Rented"] else "No"
                ))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            input("Click Enter...")

            # clear console
            os.system("cls")



        elif chose == "c":
            print("Note: For find your book's id, first go to 'Book list'.")
            print("~~~~~~~~~~~~< Rent A Book >~~~~~~~~~~~~")
            bookId = input("Book id: ").strip()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            # clear console
            os.system("cls")
            
            user.rentABook(bookId)
        
        elif chose == "d":
            print("Note: For find the book's id, first go to 'My rented book'")
            print("~~~~~~~~~~~~< Return A Book >~~~~~~~~~~~~")
            bookId = input("Book Id: ").strip()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            # clear console
            os.system("cls")

            user.returnABook(bookId)
        
        elif chose == "e":
            
            rentedBooks = user.rentedBooks
            if rentedBooks == {}:
                print("You have not rented any book.")
            
            else:
                bookslist = user.libraryBooks
                print("~~~~~~~~~~~~~~~~< Your Rented Books >~~~~~~~~~~~~~~~~")
                for bookId, rentedDate in rentedBooks.items():
                    print("ID: {} -- Name: {}; Rented on: {}".format(
                        bookId,
                        bookslist[bookId]["Name"],
                        rentedDate
                    ))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                input("Click Enter...")
                
                # clear console
                os.system("cls")

        elif chose == "f":
            print("log out...")
            break

        elif chose == "g":
            print("Have a Good Day!")
            exit()
            
        else:
            print("Please select options with (a, b, c, d, e, f, g)")


if __name__ == "__main__":
    intro()
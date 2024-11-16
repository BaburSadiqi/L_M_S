
# user registration
def re():
    username = str(input("Please enter your username: "))
    password = str((input("Please enter your password: ")))
    
    with open("logins.info.txt", "a") as f:
        f.write(f"\n{username},{password}")
        print("User Create Successfully")


    # printing all books        
def all_bookss():
    with open("books.txt") as file:
        print(" ")
        print("| Book Name           Author Name |")
        print(file.read())
        print(" ")


# loading fils into dic
def load_books():
    books = {}
    with open("books.txt", "r") as f:
        for line in f:
            if " -> " in line:
                book, author = line.strip().split(" -> ")
                books[author] = book
    return books


# serach a book by name or author
def search_book_by_name_or_authr(search_keyword):
    books = load_books()
    for author, book in books.items():
        if search_keyword.lower() in book.lower() or search_keyword.lower() in author.lower():
            print(f"Book: {book}, Author: {author}")
            return
    print("Book Not found")      


# loading file into the list
def read_logins():
    with open("logins.info.txt", "r") as f:
        c = f.readlines()

        
        new_sa = []
        
        for line in c:
            fields = line.split(",")
            fields[1] = fields[1].rstrip()
            new_sa.append(fields)

        return new_sa


# delete a book by name
def delete_book(book_name_to_delete):
    books = []

    with open("books.txt", "r") as f:
        for line in f:
            if "->" in line:
                book, author = line.strip().split(" -> ")
                books.append((book, author))
    

    book_found = False
    for book, author in books:
        if book.lower() == book_name_to_delete.lower():
            books.remove((book, author))
            book_found = True
            print(f"Book '{book_name_to_delete}' has been deleted.")
            break


    if not book_found:
        print("Book not found.")


    with open("books.txt", "w") as f:
        for book, author in books:
            f.write(f"{book} -> {author}\n")


#add book
def add_book():
    book_name = str(input("Please Write Book Name: "))
    author_name = str(input("Please Write Author Name: "))

    with open("books.txt", "a") as f:
        f.write(f"\n{book_name} -> {author_name}")
        print("Book added successfully")

 
# login method
def login(logins):
    ask_username = str(input("Username: "))
    ask_password = str(input("Password: "))

    logged_in = False

    for line in logins:
        if line[0] == ask_username and logged_in == False:
            if line[1] == ask_password:
                logged_in = True

    if logged_in == True:
        print("\nlogged in successfully")
        print("1: Add New Book")
        print("2: Delete Book")
        print("3: All Book")
        add_n_book = str(input("Enter your choice: "))
        if add_n_book == "1":
            add_book()
        elif add_n_book == "2":
            l_delete_book = str(input("Please enter the book name to be delete: "))
            delete_book(l_delete_book)
            
        elif add_n_book == "3":
            all_bookss()
        return True
        
    else:
        print("Username or password is incorrect")
        return False


# main function 
def main():
    print("Welcome to the Library Management System!")
    
    is_true = True
    
    while is_true:
        print("\nOptions")
        print("1: Registeration")
        print("2: Login")
        print("3: View all books")
        print("4: Search book by Name or Author")
        print("5: Add New Book (Admin Only)")
        print("6: Exit")

        user_input = str(input("Please enter your choices: "))

        if user_input == "1":
            re()
        elif user_input == "2":
            l = read_logins()
            x = login(l)
            
        elif user_input == "3":
            all_bookss()
            c = str(input("Exit the page: Yes or Not..? ")).lower()
            if c == "not":
                print(" ")
            if c == "yes":
                is_true = False
                break
        elif user_input == "4":
            s = str(input("Serach: "))
            search_book_by_name_or_authr(s)
        elif user_input == "5":
            print("Only available after login.")
        elif user_input == "6":
            print("Goodbye!")
            is_true = False
            break
        else:
            print("Invalid choice, please try again")



main()
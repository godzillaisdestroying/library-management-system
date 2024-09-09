class Library:

    books = []

    def __init__(self,booklist):
        self.books = booklist

    def display(self):
        for i in self.books:
            print(i)
    

booklist = ["the great gasby", "1984", "pride and prejeduice"]
library = Library(booklist)

while True:
    print("\n--- Library Menu ---")
    print("1. Display books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")
    choice = input("Enter the choice 1/2/3/4")

    if choice == "1":
        library.display()
    elif choice == "4":
        break
    else:
        print("Please chose a valid option")
        
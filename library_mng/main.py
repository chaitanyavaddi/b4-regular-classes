from books import add_book, get_books
from members import add_member, borrow_a_book, get_all_members

def show_menu():
    print(''' 
            1. Add New Book
            2. Register Member
            3. Issue Book
            4. Return Book
            5. Calculate Fine
            6. Add Member to Waitlist
            7. View Member Summary
            8. View Popular Books
            9. View All Books in Library
            10. All members
            11. Exit
    ''')

def main():
    while True:
        show_menu()
        choice = input('Enter your choice:')
        if choice == '1':
            iden = int(input('Enter Id:'))
            name = input('Enter Book Name:')
            author = input('Enter Author Name:')
            stock = int(input('Enter Stock:'))
            add_book(iden, name, author, stock)
        elif choice == '2':
            iden = int(input('Enter Id:'))
            name = input('Enter your name:')
            add_member(iden, name)
        elif choice == '3':
            user_id = int(input('Enter user id:'))
            book_id = int(input('Enter book id:'))
            borrow_a_book(user_id, book_id)
        elif choice == '9':
           books = get_books()
           print(books)
        elif choice == '10':
            members = get_all_members()
            print(members)
        else:
            print('feature not implemented')

    


if __name__ == '__main__':
    main()
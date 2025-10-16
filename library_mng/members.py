from books import deduct_stock


members = [
    {
        'id': 1,
        'name': 'Aravind',
        'borrowed_books': [1] #represents Ids of books
    }
]


def add_member(iden, name):
    members.append({
        'id': iden,
        'name': name,
        'borrowed_books': []
    })
    print('Successfully registered member')


def borrow_a_book(user_id, book_id):
    for member in members:
        if member['id'] == user_id:
            member['borrowed_books'].append(book_id)
            deduct_stock(book_id)



def get_all_members():
    return members
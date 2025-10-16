
books = [
    {
        'id': 1,
        'name': 'Harry Poter',
        'author': 'Harry',
        'stock': 8
    },
    {
        'id': 2,
        'name': 'Iron Man',
        'author': 'Iron',
        'stock': 2
    }
]


def add_book(iden, name, author, stock):
    books.append({
        'id': iden,
        'name': name,
        'author': author,
        'stock': stock
    })
    print('Successfully added book')

def get_books():
    return books

def deduct_stock(book_id):
    for book in books:
        if book['id'] == book_id:
             book['stock'] -= 1
cart = []

count = 0
while count < 6:
    choice = int(input('Enter 1 to add, 2 to remove: '))
    if choice == 1:
        product = input('Enter product to add:')
        cart.append(product)
    elif choice == 2:
        product = input('Enter product to remove:')
        cart.remove(product)
    count+=1

print(cart)
flights = {
   "AI101": {
         "route": "Delhi → Mumbai",
         "seats": 5, 
         "price": 4500
      },
   "AI102": {
       "route": "Delhi → Bangalore", 
       "seats": 3, 
       "price": 6500
       },
   "AI103": {
       "route": "Mumbai → Chennai",
         "seats": 2, 
         "price": 7000
         },
}

bookings = []

def book_flight(user_choice):
   selected_flight = flights.get(user_choice)
   if selected_flight['seats'] > 0:
      selected_flight['seats'] = selected_flight['seats'] - 1
      bookings.append(selected_flight)
      print(f'Booking is successful for {user_choice}')
   else:
      print('No Seats')

def main():
    
   while True:
      print('-' * 20)
      print('1. Show Flights')
      print('2. Book Flight')
      print('3. View Bookings')
      print('4. Exit')

      choice = input('Choose an option:')
      print('-' * 20)
      
      if choice == '1':
         print(flights)
      elif choice == '2':
         fn = input('Enter flight number:')
         book_flight(fn)
      elif choice == '3':
         print(bookings)
      elif choice == '4':
         print('Bye')
         break
      else:
         print('Invalid option')



if __name__ == '__main__':
    main()
    
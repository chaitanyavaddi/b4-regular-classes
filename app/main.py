import streamlit as st
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
    "AI104": {
       "route": "Goa → Hyderabad",
         "seats": 12, 
         "price": 3000
         },
         
}

bookings = []

def book_flight(user_choice):
   selected_flight = flights.get(user_choice)
   if selected_flight['seats'] > 0:
      selected_flight['seats'] = selected_flight['seats'] - 1
      bookings.append(selected_flight)
      st.toast(f'Booking is successful for {user_choice}')
      st.write(flights)
   else:
      st.toast('No Seats')


st.title('Aeroplane Booking Service')

tabs = st.tabs(['Show Flights', 'Book Flights', 'View Bookings'])


with tabs[0]:
    st.write(flights)
       
    
with tabs[1]:
   fn = st.text_input('Flight Number')
   sn = 1
   button = st.button('Book Now', type='primary')
   if button:
    book_flight(fn)


with tabs[2]:
   st.write(bookings)

def send_loan_reminder(a, b):
    msg = f'''
    Dear {a},

    Kindly clear your pending dues of Rs.{b}!

    Thanks
    HDFC 
    '''
    print(msg)
names = {'Arun': 20000, 'veera':40000, 'Charan':25000, 'Praneeth':30000}
for i in names: #i=Arun
   name = i
   amount = names[i]
   send_loan_reminder(name, amount)
   print('----------')
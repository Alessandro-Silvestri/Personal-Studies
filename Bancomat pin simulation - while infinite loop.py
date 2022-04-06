# ATM pin simulation
# I created a function that checks if the pin code, insert by an user, is correct

def atm(pin):
    while True:                                             # I create an INFINITE loop
        user_pin_answer = int(input('insert pin: '))        # I convert in integer value
        if user_pin_answer == pin:
            print('OK! You are inside your Bank account')
            break                                           # I get out from the INFINITE loop
        else:
            print('pin wrong, retry')

# I recall the function and I pass it the secret pin
atm(5678)

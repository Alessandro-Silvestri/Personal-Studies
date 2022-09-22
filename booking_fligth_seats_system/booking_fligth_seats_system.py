'''
BOOKING FLIGHT SEATS SYSTEM

The program asks the User how many and what seats he wants to book.
All is managed and saved in an exeternal json file (if it doesn't exist will be created)
Made by Alessandro Silvestri ©
'''

import json, os

class BookingSeats:
    def __init__(self) -> None:
        # If the external file doesn't exist will be created
        if not 'seats.json' in os.listdir():
            self.reset()

        with open('seats.json', 'r') as f:
            self.seats_dict = json.load(f)

    def double_digit(self, num:int):
        """ 2 digit fixing about the seats numbers """
        if len(str(num)) == 1:
            return f' {int(num)}'
        else:
            return num
    
    def block_or_dot(self, n:int):
        """ tool that replaces the value False with a dot '.' and the True with a block '█' """
        if n == 1:
            return '█'
        else:
            return '.'

    def show_seats(self):
        print()
        for i in range(1, 34):
            string_seat = 'seat' + f'{i}'
            seat_num = self.double_digit(i)
            a = self.block_or_dot(int(self.seats_dict[string_seat]['A']))
            b = self.block_or_dot(int(self.seats_dict[string_seat]['B']))
            c = self.block_or_dot(int(self.seats_dict[string_seat]['C']))
            d = self.block_or_dot(int(self.seats_dict[string_seat]['D']))
            e = self.block_or_dot(int(self.seats_dict[string_seat]['E']))
            f = self.block_or_dot(int(self.seats_dict[string_seat]['F']))
            print('   +-----+-----+-----+      +-----+-----+-----+')
            print('{} | A {} | B {} | C {} |      | D {} | E {} | F {} |'.format(seat_num, a, b, c, d, e, f))
        print('   +-----+-----+-----+      +-----+-----+-----+')

    def user_interface(self):   
        self.show_seats()
        print("\nThe seats with the dots '.' are available, the ones with the block '█' are occupied.")
        self.ask_seats_number()

        while self.ask_num_seats != 0:
            self.ask_which_seats()
            self.ask_num_seats -= 1

        self.show_seats()
        self.save()
    
    def save(self):
        """ save the seats in the file """
        with open('seats.json', 'w') as f:
            json.dump(self.seats_dict, f, indent = 4)
    
    def reset(self):
        """ tool for resetting all the seats in the file or creating if it doesn't exist """
        self.seats_dict = {}
        for i in range(1, 34):
            self.seats_dict['seat' + str(i)] = {'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False}
        with open('seats.json', 'w') as f:
            json.dump(self.seats_dict, f, indent=4)

    def ask_seats_number(self):
        """ asking the seats, with exeption handling """
        while True:
            try:
                print("press (Q or q) for leaving the program")
                self.ask_num_seats = input('\nHow many seats you want to book? ')
                self.ask_num_seats = int(self.ask_num_seats)
                break
            except:
                if self.ask_num_seats == 'q' or self.ask_num_seats == 'Q':
                    quit()
                print('Input error!!!!')

    def ask_which_seats(self):
        """ asking which seats, with exeption handling """
        while True:
            try:
                print("\npress (Q or q) for leaving the program")
                self.seats = input('insert the seat(s) in this form: example 5/B or 25/F: ')

                if self.seats == 'q' or self.seats == 'Q':
                    quit()

                self.seats = self.seats.upper()
                self.seats2 = self.seats.split('/')
                # if the seat is already occupied
                if not self.seats_dict[str('seat' + self.seats2[0])][str(self.seats2[1])] == False:
                    print('Seat already occupied')
                else:
                # if the seat is available
                    self.seats_dict[str('seat' + self.seats2[0])][str(self.seats2[1])] = True
                    # self.ask_num_seats -= 1
                    break
            except:
                if self.seats == 'q' or self.seats == 'Q':
                    quit()
                print('Input error!')


flight_obj = BookingSeats()
flight_obj.user_interface()


# Rovarspraket translator
# This program convert a fiven word or a phrase in Rovarspraket
# Made by Alessandro Silvestri

class Rovarspraket:
    # I init all the variables
    def __init__(self) -> None:
        self.txt = ''
        self.vowels = ('a', 'e', 'i', 'o', 'u', ' ')
        self.b = ''

    def rovarspraket_translate(self, txt):
        # text converter. It returns the converted text
        for i in txt:
            if i in self.vowels:
                self.b += i
            else:
                self.b += i + 'o' + i
        return self.b

    def ask_user(self):
        # Interface with the user, asking for the text an
        while True:
            a = input('insert a phrase to translate in rovarspraket: > ')
            print(self.rovarspraket_translate(a))
            while True:
                exit = input("do you want translate another one? > (y/n) ")
                if exit.lower() == 'y':
                    self.b = ''
                    break
                elif exit.lower() == 'n':
                    break
                else:
                    print('wrong command')
            if exit.lower() == 'n':
                break


translator = Rovarspraket()
translator.ask_user()

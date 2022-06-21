# PALINDROME CHECK
# This program asks the user a string and verifies if it's palindrome
# By Alessandro Silvestri, assignement solved for Python Institute


# removing the spaces from a string
def nospaces(txt):
     no_space_word = ''
     for i in txt:
          if i == ' ':
               continue
          no_space_word += i
     return no_space_word


# reversing the string
def reverse_string_nospaces(txt):
     txt = nospaces(txt)
     reversed_string = ''
     for i in range(1, len(txt)+1):
          reversed_string += txt[-i]
     return reversed_string


# final check if it's a palindrome (here I use the previous functions)
def ispalindrome(txt):
     txt2 = txt.lower()
     if nospaces(txt2) == reverse_string_nospaces(txt2):
          return True
     else:
          return False


txt = input("insert a sentence and I'll check if it's palindrome: > ")
if ispalindrome(txt):
     print("It's a palindrome")
else:
     print("It's not  palindrome")


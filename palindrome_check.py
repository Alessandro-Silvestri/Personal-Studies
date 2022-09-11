# PALINDROME CHECK
# This program asks the user a string and verifies if it's palindrome
# By Alessandro Silvestri, assignement solved for Python Institute

# reversing the string
def reverse_string_nospaces(txt):
     txt = txt.replace(' ', '')
     return txt[::-1]


# final check if it's a palindrome (here I use the previous functions)
def ispalindrome(txt):
     txt2 = txt.lower()
     if txt2.replace(' ', '') == reverse_string_nospaces(txt2):
          return True
     else:
          return False

# user interface
txt = input("insert a sentence and I'll check if it's palindrome: > ")
if ispalindrome(txt):
     print("It's a palindrome")
else:
     print("It's not  palindrome")


# AREA CALCULATOR
# This program asks the user wich area he wants to calculate
# among: circle, square, rectangle and triangle
# Made by Alessandro Silvestri

class Calculator:
     def circle(self, radius):
          return radius * radius * 3.14

     def square(self, side):
          return side ** 2

     def rectangle(self, side1, side2):
          return side1 * side2

     def triangle(self, side, height):
          return side * height / 2

     def area_calculator(self):
          # asking the user what area he wants to calculate
          user_request = input("What area do you want calculate?: (1:circle 2:square 3:rectangle 4:triangle): ")
          if user_request == '1':
               a = int(input("insert the circle radius: "))
               print(self.circle(a))
               self.retry()

          elif user_request == '2':
               a = int(input("insert the square side: "))
               print(self.square(a))
               self.retry()

          elif user_request == '3':
               a = int(input("insert the rectangle side 'a': "))
               b = int(input("insert the rectangle side 'b': "))
               print(self.rectangle(a, b))
               self.retry()
          
          elif user_request == '4':
               a = int(input("insert the triangle side: "))
               b = int(input("insert the triangle height: "))
               print(self.triangle(a, b))
               self.retry()
          
          else:
               print('wrong command')
               self.area_calculator()
     
     def retry(self):
          # internal function for asking the user if he wants to use the program again and checks the answer
          while True:
               retry_quest = input('do you want calculate other areas?: (y/n): ')
               if retry_quest.lower() != 'y' and retry_quest.lower() != 'n':
                    print('wrong command')
               else:
                    break

          if retry_quest == 'y':
               self.area_calculator()  

          if retry_quest == 'n':
               print('bye!')
               
          
area_calculator = Calculator()
area_calculator.area_calculator()


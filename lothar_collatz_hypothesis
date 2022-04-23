# Made by Alessandro Silvestri
# Lothar Collatz hypothesis


def lothar_collatz(num):
    step = 0
    while num != 1:
        step +=1
        if num % 2 == 0:
            num /=2
            print(int(num))
        else:
            num = num * 3 + 1
            print(int(num))
    print('steps: ', step)



lothar_collatz(17)          # you can pass any number. Try it! :)

'''
result:
52
26
13
40
20
10
5
16
8
4
2
1
steps:  12


In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis
(it still remains unproven) which can be described in the following way:

take any non-negative and non-zero integer number and name it c0;
if it's even, evaluate a new c0 as c0 ÷ 2;
otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
if c0 ≠ 1, skip to point 2.
'''

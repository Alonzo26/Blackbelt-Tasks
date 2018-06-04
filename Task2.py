"""
Alonzo A. Alterado    Task 2
"""

import random

x = random.randint(1,10)

while True:
    y = int(input("Please enter a number: "));
    if y == x:
        print("Correct!");   
        break
    elif y!= x:
        print("Wrong number.Try again..."); 
    


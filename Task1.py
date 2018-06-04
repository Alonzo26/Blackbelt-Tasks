"""
Alonzo A. Alterado      Task 1
"""
import random

Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}

x = Sessions_Attended['sessions']
y = x.split(",")
random_num = random.randint(0, 14)
z = random.sample(y, random_num)
w = len(z)

print(z)
print("I have attended", w, "sessions !!")




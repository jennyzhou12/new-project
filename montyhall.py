# import random
# winifs=0
# for i in range(10000):
#     y=random.randrange(1,4)
#     if y==2 or y==3:
#         winifs=winifs+1
# print("if change, chance of win is",winifs/100,"%")
# print("if not change, chance of win is 33.33%)
    

import random
win=0
for i in range(10000):
    y=random.randrange(1,5)
    if y==2 or y==3 or y==4:
        win=win+0.5
print("if change, chance of win is",win/100,"%")
print("if not change, chance of win is 25%")
    
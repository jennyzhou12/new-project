# import random
# a=0
# for i in range(5):
#     x=input("rock,paper or scissors")
#     y=random.randrange(1,4)
#     if y==1:
#         if x=="paper":
#             a-=1
#         elif x=="scissors":
#             a+=1
#         print("computer:rock")
#     if y==2:
#         if x=="rock":
#             a+=1
#         elif x=="scissors":
#             a-=1
#         print("computer:paper")
#     if y==3:
#         if x=="paper":
#             a+=1
#         if x=="rock":
#             a-=1
#         print("computer:scissors")
# if a>0:
#     print("computer wins")
# elif a==0:
#     print("tie")
# else:
#     print("user wins")


import random
a=0
for i in range(5):
    x=input("rock,paper or scissors")
    if x=="rock":
        x=1
    if x=="scissors":
        x=2
    if x=="paper":
        x=3
    y=random.randrange(1,4)
    if y==1:
        print("computer:rock")
    if y==2:
        print("computer:paper")
    if y==3:
        print("computer:scissors")
    a=0
    if x<y:
        a=a+1
    if x>y:
        a=a-1
if a>0:
    print("computer wins")
elif a==0:
    print("tie")
else:
    print("user wins")

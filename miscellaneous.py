# x=int(input("x="))
# y=int(input("y="))
# z=int(input("z="))
# x,y,z=z,x,y
# print(x,y,z)


# count=1000
# for i in range(1001):
#     for a in range(1,i+1):
#         if i==a**2 or i==a**3 or i==a**5:
#             count=count-1
# print(count)


# 10(a)
# a=b=float(input("enter 10 scores"))
# for i in range(9):
#     x=float(input("enter 10 scores"))
#     if x>a:
#         a=x
#     if x<b:
#         b=x
# print("max",a,"min",b)


# # 10(b)
# a=0
# for i in range(10):
#     x=float(input("enter 10 scores"))
#     a=a+x
# print(a/10)


# 10(c)
# a=float(input("enter 10 scores"))
# b=float(input("enter 10 scores"))
# if a<b:
#     a,b=b,a
# for i in range(8):
#     x=float(input("enter 10 scores"))
#     if x>a:
#         a,b,x=x,a,b
#     elif x>b:
#         b,x=x,b
# print("second max",b)


# # 10(d)
# a=b=float(input("enter 10 scores"))
# for i in range(9):
#     x=float(input("enter 10 scores"))
#     if x>a:
#         a=x
# if a>100:
#     print("warning")


# # 10(e)
# a=float(input("enter 10 scores"))
# b=float(input("enter 10 scores"))
# if a>b:
#     a,b=b,a
# sum=0
# for i in range(8):
#     x=float(input("enter 10 scores"))
#     if x<a:
#         a,b,x=x,a,b
#     elif x<b:
#         b,x=x,b                     
#     sum=sum+x   
# print(sum/8)


#10
# lst=[]
# warning=""
# for i in range(10):
#     x=float(input("enter 10 numbers"))
#     if x>100:
#         warning="warning"
#     lst.append(x)
#     lst.sort()
#     avg=sum(lst)/10
#     e=sum(lst[2:10])/8
# print("max=",lst[9],"min=",lst[0],"second largest",lst[8],"avg=",avg,warning,"drop 2lowest,avg=",e)


# #factorial
# x=int(input("n=?"))
# y=1
# for i in range(1,x+1):
#     y=i*y
# print(y)


# import random
# a=0
# for i in range(5):
#     x=int(input("guess a number between 1 and 10"))
#     y=random.randrange(1,11)
#     print(y)
#     if x==y:
#         a=a+10
#     else:
#         a=a-1
# print("total=",a)


# count=0
# import random
# for i in range(1,11):
#     x=random.randrange(1,10)
#     y=random.randrange(1,10)
#     print("Question",i,":",x,"*",y,"=?",end="")
#     z=int(input(""))
#     if z==x*y:
#         print("Right")
#         count=count+1
#     else:
#         print("Wrong.","The answer is ",x*y)
# print("you got",count,"number of questions right")
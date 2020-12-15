x=int(input("Enter hour:"))
s=input("am or pm?")
y=int(input("how many hours more?"))
if s=="am":
    newhour=x
elif s=="pm":
    newhour=x+12

if((newhour+y)//12)%2==1:
    print((newhour+y)%12,"pm")
else:
    print((newhour+y)%12,"am")
    

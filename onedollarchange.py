x=round(float(input("changeamount")),2)

quarter=0.25
dime=0.1
nickel=0.05
penny=0.01


a=x//0.25
b=x-a*0.25
c=b//0.1
d=b-c*0.1
e=d//0.05
f=d-0.05*e
g=f//0.01
print("give quarter=",a,"give dime=",c,"give nickel=",e,"give penny=",g)
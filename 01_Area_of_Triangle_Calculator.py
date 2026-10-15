#Code for calculating area of triangle

a=float(input("enter a first side"))
b=float(input("enter a second size"))
c=float(input("enetr a third side"))
s=(a+b+c)/2
print(s)
area1=s*(s-a)*(s-b)*(s-c)**0.5

print(round(area1,2))
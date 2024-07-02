a=int(input("enter the first side length"))
b=int(input("enter the second side length"))
c=int(input("enter the last side length"))

if(a+b>c and b+c>a and a+c>b):
 print("this forms a triangle.")
else:
   print("this does't form a triangle.")
   
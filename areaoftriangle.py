a=float(input('enter first side of triangle:'))
b=float(input('enter second side of triangle:'))
c=float(input('enter third side of triangle:'))
s=(a+b+c)/2
Area= (s*(s-a)*(s-b)*(s-c))**0.5
print('Area of triangle ' , Area ) 

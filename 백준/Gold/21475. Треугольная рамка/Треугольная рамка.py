a1,b1,c1,d1= map(int,input().split())

s = (a1+b1+c1)/2
A = (s*(s-a1)*(s-b1)*(s-c1))**(0.5)

a = A
b = s*d1
c = s*d1 -A


equation = (-b + (b**2-4*a*c)**0.5)/(2*a)
print(round(A*(1-(equation)**2),5))
def Collatz(n):
   x = [n]
   if (x[0]%2 == 0):
       x.append(x[0]/2)
       print(x)
   else:
       x.append(3*x[0]+1)
       print(x)

Collatz(2)

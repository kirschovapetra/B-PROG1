a=-10
b=10
while b-a>0.0001:
    s=(a+b)/2
    if (s**3+s**2+2*s-1)<0:
        a=s
    else:
        b=s
print(s)

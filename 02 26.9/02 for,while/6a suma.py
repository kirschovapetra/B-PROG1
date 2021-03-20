# sum = 1 + 1/2 + 1/4 + 1/8 + .... + 1/(2^100)
sum = 0
for i in range(101):
    sum = sum+1/(2**i)
print(sum)
    

# sum = 1 + 1/2 + 1/4 + 1/8 + .... + 1/(2^100)
sum = 0
for i in range(100):
    sum = sum+1/(2**i)
    print(sum)


    

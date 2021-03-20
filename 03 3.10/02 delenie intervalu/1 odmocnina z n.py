n = int(input('zadaj b '))
a = 0
b = n
while (b-a>0.01):
    stred = (a+b)/2
    if (stred*stred > n):
        b = stred
    else:
        a = stred
print(stred)

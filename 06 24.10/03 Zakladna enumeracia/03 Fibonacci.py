def Fibonacci(n):
    pole = [0,1]
    for i in range(2,n):
        pole.append(pole[i-2]+pole[i-1])
    print(pole)
Fibonacci(10)

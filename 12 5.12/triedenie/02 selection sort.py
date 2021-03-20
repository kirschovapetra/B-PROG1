a = [0,2,-1,4,6,3,11,-2,4]

for i in range(len(a),0,-1):
    max = 0
    for j in range(i):
        if a[j]>a[max]:
            max = j
    a[i-1],a[max] = a[max],a[i-1]
print(a)

"""
this is a Python file to resolve a problem
minimum absolute difference between elements of arrays
[3,7,0]
"""
arr = list(map(int, input().split()))
dif = abs(arr[0] - arr[1])
for i in range(len(arr)):
    for j in range(len(arr)):
        if abs(arr[i] - arr[j]) < dif and  i!=j:
            dif = arr[i] - arr[j]
print(dif)

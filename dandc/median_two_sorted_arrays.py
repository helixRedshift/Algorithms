a=input("Enter first sorted array: ")
a=[int(x) for x in a.split()]
b=input("Enter second sorted array: ")
b=[int(x) for x in b.split()]

def median(a, b):
    res_arr = []
    j = 0
    i = 0
    n = len(a)
    while len(res_arr) <= n and i < n and j < n:
        if a[i] >= b[j]:
            res_arr.append(b[j])
            j += 1
        else:
            res_arr.append(a[i])
            i += 1
    if i == n and len(res_arr) == n:
        res_arr.append(b[j])
    if j == n and len(res_arr) == n:
        res_arr.append(a[i])
    return (res_arr[-1] + res_arr[-2])/2

res = median(a, b)
print("Median of both arrays is:", res)
a=input("Enter numbers in the array: ")
a=[int(x) for x in a.split()]

def kadane(a, i, res_a):
    res_a = sum_subarray(a[i:], len(a[i:]), *res_a)
    if len(a[i:]) == 1:
        return res_a
    i = i+1
    return kadane(a, i, res_a)

def sum_subarray(a, l, res_array, max):
    sum=0
    for item in a[:l]:
        sum = sum + item
    if sum > max:
        max = sum
        res_array = a[:l]
    
    if l == 1:
        return res_array, max
    l = l-1
    return sum_subarray(a, l, res_array, max)

if len(a) != 0:  
    res_a=([a[0]], a[0])
    i=0
    res=kadane(a, i, res_a)
    print("Max subarray is:", res[0], "with largest sum:", res[1])
else:
    print ("Invalid input")
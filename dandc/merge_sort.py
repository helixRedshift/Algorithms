a=input("Enter numbers in the array: ")
a=[int(x) for x in a.split()]

def divide_array(a):
    mid = int(len(a)/2)
    if (len(a) == 1):
        return a
    return merge_array(divide_array(a[:mid]), divide_array(a[mid:]))

def merge_array(v1, v2):
    i=0
    j=0
    v3=[]

    while i != len(v1) and j != len(v2):
        if v1[i] < v2[j]:
            v3.append(v1[i])
            i+=1
        else:
            v3.append(v2[j])
            j+=1

    if i == len(v1):
        v3 = v3 + v2[j:]
    else:
        v3 = v3 + v1[i:]
    return v3

if len(a) != 0: 
    res = divide_array(a)
    print ("result: ", res, "\n")
else:
    print ("Invalid input")
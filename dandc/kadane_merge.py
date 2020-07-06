a=input("Enter numbers in the array: ")
a=[int(x) for x in a.split()]

def find_max_middle(a1, a2):
    max1=a1[-1]
    max2=a2[0]
    max=0
    cur1=0
    cur2=0
    a=[]

    for i in range(len(a1)-1, -1, -1):
        cur1 += a1[i]

        if cur1 >= max1:
            max1 = cur1
            indx1 = i
    a += a1[indx1:]
    
    for j in range(len(a2)):
        cur2 += a2[j]

        if cur2 >= max2:
            max2 = cur2
            indx2 = j
    a += a2[:indx2+1]
        
    max = max1 + max2
    return max, a

def divide_array(a):
    if (len(a) == 1):
        return a[0], a
    
    mid = int(len(a) / 2)

    return max(*find_max_middle(a[:mid], a[mid:]), *divide_array(a[:mid]), *divide_array(a[mid:]))

def max(max1, res_a1, max2, res_a2, max3, res_a3):
    if max1 >= max2 and max1 >= max3:
        return max1, res_a1
    
    if max2 >= max1 and max2 >= max3:
        return max2, res_a2

    if max3 >= max1 and max3 >= max2:
        return max3, res_a3

if len(a) != 0:  
    res = divide_array(a)
    print("Sum of max subarray is:", res[0], "and subarray is:", res[1])
else:
    print ("Invalid input")


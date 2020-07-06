a=input("Enter numbers in the array: ")
a=[int(x) for x in a.split()]

def insert_pivot(a):
    pivot = a[-1]
    indx_pivot = len(a) - 1
    i = 0
    j = len(a) - 2

    while i <= j:
        
        print("array: ", a)
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        print("i and j :", i, j)
        if (i < j) and a[i] > pivot and a[j] < pivot:
            print("ai and aj: ", a[i], a[j])
            tmp = a[j]
            a[j] = a[i]
            a[i] = tmp
            i += 1
            j -= 1
            print("i and j :", i, j)
        
    #print("array: ", a)
    if i > j:
        tmp = pivot
        a[indx_pivot] = a[i]
        a[i] = tmp
        print("array: ", a)
        return i

def quick_sort(a):
    if len(a) == 1 or len(a) == 0:
        return a
    indx_pivot = insert_pivot(a)
    print("index: ", indx_pivot)
    print("quick sort array full: ", a)
    print("quick sort array: ", a[:indx_pivot])
    quick_sort(a[:indx_pivot])
    quick_sort(a[indx_pivot:]) 

    return a

res = quick_sort(a)
print(res)
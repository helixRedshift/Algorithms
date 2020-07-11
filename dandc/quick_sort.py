a=input("Enter numbers in the array: ")
a=[int(x) for x in a.split()]

def insert_pivot(a, low, high):
    pivot = a[high]
    indx_pivot = high
    i = low
    j = high - 1

    while i<=j:
        if a[i] < pivot:
            i += 1
            continue
        if a[j] > pivot:
            j -= 1
            continue
        if a[i] > pivot and a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
            j -= 1
        
    a[indx_pivot], a[i] = a[i], a[indx_pivot]
    return i

def quick_sort(a, low, high):
    if low < high:
        indx_pivot = insert_pivot(a, low, high)
        quick_sort(a, low, indx_pivot-1)
        quick_sort(a, indx_pivot+1, high) 
    
    return a

low = 0
high = len(a) - 1
res = quick_sort(a, low, high)
print(res)
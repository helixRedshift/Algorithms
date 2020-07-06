a=input("Enter numbers in the array: ")
a=[int(x) for x in a.split()]
cnt=0

def divide_array(a, cnt):
    mid = int(len(a)/2)

    if (len(a) == 1):
        return a,cnt
    return merge_array(*(divide_array(a[:mid], cnt)), *(divide_array(a[mid:], cnt)))

def merge_array(v1, cnt1, v2, cnt2):
    i=0
    j=0
    v3=[]
    cnt=cnt1+cnt2
    while i != len(v1) and j != len(v2):
        if v1[i] < v2[j]:
            v3.append(v1[i])
            i+=1
        else:
            v3.append(v2[j])
            j+=1
            cnt+=len(v1[i:])

    if i == len(v1):
        v3 = v3 + v2[j:]
    else:
        v3 = v3 + v1[i:]
    return v3, cnt

if len(a) != 0:  
    res = divide_array(a, cnt)
    print("result: ", res[1], "\n")
else:
    print ("Invalid input")

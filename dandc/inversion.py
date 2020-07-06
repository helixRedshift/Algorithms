a=input("Enter numbers in the array: ")
a=[int(x) for x in a.split()]
srt=[]
cnt=0

def inversion(a, srt, cnt):
    cnt=bubble(a[-1], srt, 0, cnt)
    a.pop()
    if (len(a) == 0):
        return cnt
    return inversion(a, srt, cnt)

def bubble(num, srt, indx, cnt):
    if (len(srt) == 0):
        srt.append(num)
        return 0
    if (num > srt[indx]):
        cnt+=1
        indx+=1
        if (len(srt) == indx):
            srt.append(num)
            return cnt
    else:
        srt.insert(indx, num)
        return cnt

    return bubble(num, srt, indx, cnt)

if len(a) != 0:
    res=inversion(a, srt, cnt)
    print ("Result: ", res, "\n")
else:
    print ("Invalid input")
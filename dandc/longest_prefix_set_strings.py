a=input("Enter string list: ")
a=[x.lower() for x in a.split()]

def longest_prefix(pref1, pref2):
    s = ""
    for char1, char2 in zip(pref1, pref2):
        if char1 == char2:
            s += char1
        else:
            break
    return s

def divide_list(a):
    mid = int(len(a)/2)
    if len(a) == 1:
        return a[0]
    return (longest_prefix(divide_list(a[:mid]), divide_list(a[mid:])))

res = divide_list(a)
print("longest prefix:", res)
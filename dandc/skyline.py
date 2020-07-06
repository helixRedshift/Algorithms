num = int(input("Enter the number of buildings: "))
print("Enter coordinates(left, reght, height) of the building separated by spaces and hit enter to input for next one")
aob = []
for i in range(num):
    print("Building", i+1)
    a=input()
    a=[int(x) for x in a.split()]
    aob.append(a)

print("Entered array of buildings is:", aob)

def divide_canvas(aob, canvas_range):
    res_aob = []
    res = []
    mid = int(len(canvas_range) / 2)
    if len(canvas_range) == 1:
        max = 0
        for indx in range(len(aob)):
            if (aob[indx][0] <= canvas_range[0]) and (aob[indx][1] >= canvas_range[0]):
                res_aob.append(aob[indx])
        for indx in range(len(res_aob)):
            if res_aob[indx][2] >= max:
                max = res_aob[indx][2]

        res = [max, canvas_range[0]]
        return res

    return merge(divide_canvas(aob, canvas_range[:mid]), divide_canvas(aob, canvas_range[mid:]))

def merge(a1, a2):
    return a1, a2

canvas_len = aob[-1][1]
print(canvas_len)
canvas_range = list(range(1,canvas_len+1))
res1 = divide_canvas(aob, canvas_range)
print(res1)

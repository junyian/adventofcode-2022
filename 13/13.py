from pprint import pprint
from itertools import zip_longest

def compare(left:list, right:list):
    # print(left)
    # print(right)
    for l,r in zip_longest(left, right):
        # print(f"  l: {l}    r: {r}")
        if type(l)==type([]) and type(r)==type([]):
            res = compare(l, r) 
            if res != -1:
                return res
        elif type(l)==type([]) and type(r)==type(1):
            res = compare(l, [r])
            if res != -1:
                return res
        elif type(l)==type(1) and type(r)==type([]):
            res = compare([l], r)
            if res != -1:
                return res
        elif type(l)==type(None):
            return True
        elif type(r)==type(None):
            return False
        elif l==r:
            continue
        elif l<r:
            return True
        elif l>r:
            return False
        else:
            print("unknown")
    return -1

def bubblesort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if compare(arr[j+1], arr[j]) == True:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
        if not swapped:
            return
        
lines = open("input2.txt").readlines()

packets = []

for i in range(0, len(lines), 3):
    left = eval(lines[i].strip())
    right = eval(lines[i+1].strip())
    packets.append((left, right))

# packets.append(([[2]], [[6]]))
# pprint(packets)

part1 = []
for i, packet in enumerate(packets):
    res = compare(packet[0], packet[1])
    if res==True:
        part1.append(i+1)
    print(i+1, ":", res)
print(sum(part1))

packets.append(([[2]], [[6]]))

# Part 2
packets2 = []
for l in lines:
    if len(l.strip()) > 0:
        packets2.append(eval(l.strip()))
packets2.append([[2]])
packets2.append([[6]])

bubblesort(packets2)
print(packets2)

print( (packets2.index([[2]])+1) * (packets2.index([[6]])+1))
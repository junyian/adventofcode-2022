f = open("input2.txt").readlines()

elves = []
c = 0
for i in f:
    calories = i.strip()
    if len(calories) > 0:
        c = c + int(calories)
    else:
        elves.append(c)
        c = 0
elves.append(c)
print(max(elves))

elves.sort(reverse=True)
print(elves[0] + elves[1] + elves[2])
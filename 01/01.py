with open("input2.txt") as f:
    elves = []
    c = 0
    for i in f:
        calories = i.strip()
        if len(calories) > 0:
            c = c + int(calories)
        else:
            elves.append(c)
            c = 0
    elves.append(c) # the last row
    elves.sort(reverse=True)
    print((max(elves), sum(elves[:3])))
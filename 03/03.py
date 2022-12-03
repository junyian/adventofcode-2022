lines = open("input2.txt").readlines() 

score = 0
for l in lines:
    half = int(len(l.strip())/2)
    c1, c2 = l[:half], l[half:]
    for c in c1:
        if c2.count(c) > 0:
            if c.islower():
                score += ord(c) - 96
            else:
                score += ord(c) - 38
            break
print(score)

score = 0
for i in range(0, len(lines), 3):
    for c in lines[i]:
        if lines[i+1].count(c) > 0 and lines[i+2].count(c) > 0:
            if c.islower():
                score += ord(c) - 96
            else:
                score += ord(c) - 38
            break
print(score)

import re

lines = open("input2.txt").readlines() 

score = 0
for l in lines:
    m = re.match(r"(\d+)-(\d+),(\d+)-(\d+)", l.strip())
    pmin1, pmax1, pmin2, pmax2 = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
    if pmin2 >= pmin1 and pmax2 <= pmax1:
        score += 1
    elif pmin1 >= pmin2 and pmax1 <= pmax2:
        score += 1
print(score)

score = len(lines)
for l in lines:
    m = re.match(r"(\d+)-(\d+),(\d+)-(\d+)", l.strip())
    pmin1, pmax1, pmin2, pmax2 = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
    if pmin2 > pmax1:
        score -= 1
    elif pmax2 < pmin1:
        score -= 1
print(score)
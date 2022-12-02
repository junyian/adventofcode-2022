lines = open("input2.txt").readlines() 

score = 0
for l in lines:
    i, o = l.strip().split(' ')
    if i == 'A': # rock
        if o == 'X': # rock (1) + draw (3)
            score += 1 + 3
        elif o == 'Y': # paper (2) + win (6)
            score += 2 + 6
        elif o == 'Z': # scissors (3) + lost (0)
            score += 3 + 0
    elif i == 'B': # paper
        if o == 'X': # rock (1) + lost (0)
            score += 1 + 0
        elif o == 'Y': # paper (2) + draw (3)
            score += 2 + 3
        elif o == 'Z': # scissors (3) + win (6)
            score += 3 + 6
    elif i == 'C': # scissors
        if o == 'X': # rock (1) + win (6)
            score += 1 + 6
        elif o == 'Y': # paper (2) + lost (0)
            score += 2 + 0
        elif o == 'Z': # scissors (3) + draw (3)
            score += 3 + 3
print(score)

score = 0
for l in lines:
    i, o = l.strip().split(' ')
    if i == 'A': # rock
        if o == 'X': # lose (0) + scissors (3)
            score += 0 + 3
        elif o == 'Y': # draw (3) + rock (1)
            score += 3 + 1
        elif o == 'Z': # win (6) + paper (2)
            score += 6 + 2
    elif i == 'B': # paper
        if o == 'X': # lost (0) + rock (1)
            score += 0 + 1
        elif o == 'Y': # draw (3) + paper (2)
            score += 3 + 2
        elif o == 'Z': # win (6) + scissors (3)
            score += 6 + 3
    elif i == 'C': # scissors
        if o == 'X': # lost (0) + paper (2) 
            score += 0 + 2
        elif o == 'Y': # draw (3) + scissors (3)
            score += 3 + 3
        elif o == 'Z': # win (6) + rock (1)
            score += 6 + 1
print(score)
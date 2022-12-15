def solve(input:str):
    part1, part2 = 0, 0
    with open(input) as f:
        for l in f:
            i, o = l.strip().split(' ')
            if i == 'A': # rock
                if o == 'X': # rock (1) + draw (3)
                    part1 += 1 + 3
                    part2 += 0 + 3
                elif o == 'Y': # paper (2) + win (6)
                    part1 += 2 + 6
                    part2 += 3 + 1
                elif o == 'Z': # scissors (3) + lost (0)
                    part1 += 3 + 0
                    part2 += 6 + 2
            elif i == 'B': # paper
                if o == 'X': # rock (1) + lost (0)
                    part1 += 1 + 0
                    part2 += 0 + 1
                elif o == 'Y': # paper (2) + draw (3)
                    part1 += 2 + 3
                    part2 += 3 + 2
                elif o == 'Z': # scissors (3) + win (6)
                    part1 += 3 + 6
                    part2 += 6 + 3
            elif i == 'C': # scissors
                if o == 'X': # rock (1) + win (6)
                    part1 += 1 + 6
                    part2 += 0 + 2
                elif o == 'Y': # paper (2) + lost (0)
                    part1 += 2 + 0
                    part2 += 3 + 3
                elif o == 'Z': # scissors (3) + draw (3)
                    part1 += 3 + 3
                    part2 += 6 + 1
    return (part1, part2)

if __name__ == "__main__":
    print(solve("input1.txt"))
    print(solve("input2.txt"))
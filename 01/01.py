def solve(input:str):
    with open(input) as f:
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
        return (max(elves), sum(elves[:3]))

if __name__ == "__main__":
    print(solve("input1.txt"))
    print(solve("input2.txt"))
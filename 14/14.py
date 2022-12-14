import numpy as np

def getlimits(rocks):
    xlist, ylist = [], []
    for y, x in rocks:
        xlist.append(x)
        ylist.append(y)
    return (min(xlist), max(xlist), min(ylist), max(ylist))
    
def visualize(rocks, sand=[]):
    _, maxx, miny, maxy = getlimits(rocks)
    wall = np.chararray((maxx+1, maxy+1))
    wall[:] = '.'
    for y, x in rocks:
        wall[x][y] = '#'
    for y, x in sand:
        wall[x][y] = 'o'
    wall[0][500] = '+'
    sliced = wall[:,miny:]
    # print(sliced)
    for x in sliced:
        for y in x:
            print(y.decode('ascii'), end='')
        print()

def sandfall(rocks, floor=-1):
    sandcount = 0
    sandrocks = list(rocks)
    sand = list()
    
    # print(floor)
    _, maxx, miny, maxy = getlimits(rocks)

    while True:
        y, x = 500, 0
        isEnd = False
        # print(f"Sand #{sandcount+1}")
        while True:
            # print(y,x)
            if floor == -1 and x == maxx:
                isEnd = True
                break
            elif (x+1)==floor:
                # print("  hit floor")
                rocks.add((y, floor))
                rocks.add((y-1, floor))
                rocks.add((y+1, floor))
                if (y, floor) not in sandrocks:
                    sandrocks.append((y, floor))
                if (y-1, floor) not in sandrocks:
                    sandrocks.append((y-1, floor))
                if (y+1, floor) not in sandrocks:
                    sandrocks.append((y+1, floor))
                sandrocks.append((y,x))
                sand.append((y,x))
                # visualize(rocks, sand)
                break
            if (500, 0) in sand:
                isEnd = True
                break
            if (y, x+1) not in sandrocks:
                x += 1
            else:
                # print("  hit obstacle")
                if (y-1, x+1) not in sandrocks:
                    y -= 1
                    x += 1
                    continue
                else:
                    # print("  can't go left")
                    if (y+1, x+1) not in sandrocks:
                        y += 1
                        x += 1
                        continue
                    else:
                        # print("  can't go right too. stop here.")
                        sandrocks.append((y, x))
                        sand.append((y, x))
                        # visualize(rocks, sand)
                        break
        if isEnd == True:
            break
        sandcount += 1
        # input()
    # visualize(rocks, sand)
    return sandcount

def solve(input:str):
    part1, part2 = 0, 0

    rocks = set()
    with open(input) as f:
        for l in f:
            arr_pathnodes_str= l.strip().split(' -> ')
            for i in range(0, len(arr_pathnodes_str)-1):
                ax, ay = arr_pathnodes_str[i].split(',')
                bx, by = arr_pathnodes_str[i+1].split(',')
                if int(ax)==int(bx):
                    if int(ay) < int(by):
                        for y in range(int(ay), int(by)+1):
                            rocks.add((int(ax), y))
                    elif int(by) < int(ay):
                        for y in range(int(by), int(ay)+1):
                            rocks.add((int(ax), y))
                elif int(ay)==int(by):
                    if int(ax) < int(bx):
                        for x in range(int(ax), int(bx)+1):
                            rocks.add((x, int(ay)))
                    elif int(bx) < int(ax):
                        for x in range(int(bx), int(ax)+1):
                            rocks.add((x, int(ay)))
    part1 = sandfall(rocks)
    _, maxx, _, _ = getlimits(rocks)
    part2 = sandfall(rocks, maxx+2)

    return (part1, part2)

if __name__ == "__main__":
    print(solve("input1.txt"))
    print(solve("input2.txt"))


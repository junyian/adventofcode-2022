import numpy as np
import re
from multiprocessing import Pool

DEBUG = True

def log(log:str):
    if DEBUG==True:
        print(log)


def getlimits(array):
    xlist, ylist = [], []
    for y, x in array:
        xlist.append(x)
        ylist.append(y)
    return (min(xlist), max(xlist), min(ylist), max(ylist))

def visualize(sensors, beacons):
    offsetx, offsety = 0, 0
    miny, maxy, minx, maxx = getlimits(sensors + beacons)
    mapview = np.chararray((maxy-miny+1, maxx-minx+1))
    mapview[:] = '.'

    if minx < 0:
        offsetx += -1 * minx
    if miny < 0:
        offsety += -1 * miny
    
    for s in sensors:
        mapview[s[1]+offsety][s[0]+offsetx] = 'S'
    for b in beacons:
        mapview[b[1]+offsety][b[0]+offsetx] = 'B'

    for r in mapview:
        print(''.join(r.decode('ascii')))

def getdistance(pointa, pointb):
    distance = 0
    if pointa[0] > pointb[0]:
        distance += pointa[0] - pointb[0]
    else:
        distance += pointb[0] - pointa[0]
    if pointa[1] > pointb[1]:
        distance += pointa[1] - pointb[1]
    else:
        distance += pointb[1] - pointa[1]
    return distance
    

def solve(input:str, y, searchsize):
    part1, part2 = 0, 0

    sensors = []
    beacons = []
    with open(input) as f:
        for l in f:
            m = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", l)
            s_x, s_y, b_x, b_y = list(int(x) for x in m.groups())
            log(f"Sensor x={s_x}, y={s_y}, Beacon x={b_x}, y={b_y}")
            sensors.append((s_x, s_y))
            beacons.append((b_x, b_y))
    # visualize(sensors, beacons)

    minx = []
    maxx = []
    beacons_on_row = set()
    for sensor, beacon in zip(sensors, beacons):
        d1 = getdistance(sensor, beacon)
        log(f"Sensor {sensor} to beacon {beacon} with distance of {d1}.")
        d2 = getdistance(sensor, (sensor[0], y))
        log(f"Nearest distance to y={y} is {d2}.")
        if d2 <= d1:
            log(f"y={y} is in range.")
            log(f"x is in range {sensor[0] - (d1 - d2)} to {sensor[0] + (d1 - d2)}")
            minx.append(sensor[0] - (d1 - d2))
            maxx.append(sensor[0] + (d1 - d2))
        if beacon[1] == y:
            beacons_on_row.add(beacon)
    part1 = max(maxx) - min(minx) - len(beacons_on_row) + 1

    cores = 8
    rng =np.random.default_rng()
    arr = np.arange(searchsize+1)
    rng.shuffle(arr)
    arrsplit = np.array_split(arr, cores)

    args = []
    for i in range(cores):
        args.append((searchsize, sensors, beacons, arrsplit[i]))

    with Pool(cores) as p:
        part2 = p.map(bruteforce, args)

    return (part1, part2)

def bruteforce(args):
    part2 = None
    for i, y2 in enumerate(args[3]):
        if i % 1000 == 0:
            log(f"{i}/{len(args[3])}: For y={y2}.")
        # ranges = []
        ranges = np.arange(0, args[0]+1)
        for sensor, beacon in zip(args[1], args[2]):
            d1 = getdistance(sensor, beacon)
            d2 = getdistance(sensor, (sensor[0], y2))
            if d2 <= d1:
                # ranges = np.union1d(ranges, np.arange(sensor[0] - (d1 - d2), sensor[0] + (d1 - d2) + 1))
                ranges = np.setdiff1d(ranges, np.arange(sensor[0] - (d1 - d2), sensor[0] + (d1 - d2) + 1))
                if len(ranges) == 0:
                    break
        if len(ranges) > 0:
            print(ranges)
            part2 = ranges[0] * 4000000 + y2
            print(part2)
            break
    return part2

if __name__ == "__main__":
    print(solve("input1.txt", 10, 20))
    print(solve("input2.txt", 2000000, 4000000))

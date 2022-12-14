import numpy as np
import pandas as pd
import re
import time
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

def distance(point1, point2):
    return sum(abs(value1 - value2) for value1, value2 in zip(point1, point2))
    

def solve(input:str, y, searchsize):
    part1, part2 = 0, 0

    sensors = []
    beacons = []
    distances = []
    minx, maxx, miny, maxy = 0, 0, 0, 0

    with open(input) as f:
        for l in f:
            m = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", l)
            s_x, s_y, b_x, b_y = list(int(x) for x in m.groups())
            log(f"Sensor x={s_x}, y={s_y}, Beacon x={b_x}, y={b_y}")
            sensors.append((s_x, s_y))
            beacons.append((b_x, b_y))
            distances.append(distance((s_x, s_y), (b_x, b_y)))
            if minx > (s_x - distances[-1]):
                minx = s_x - distances[-1]
            if maxx < (s_x + distances[-1]):
                maxx = s_x + distances[-1]
            if miny > (s_y - distances[-1]):
                miny = s_y - distances[-1]
            if maxy < (s_y + distances[-1]):
                maxy = s_y + distances[-1]
    print(minx, maxx, miny, maxy)
    # visualize(sensors, beacons)

    minx = []
    maxx = []
    beacons_on_row = set()
    for sensor, beacon, dist in zip(sensors, beacons, distances):
        log(f"Sensor {sensor} to beacon {beacon} with distance of {dist}.")
        d2 = distance(sensor, (sensor[0], y))
        log(f"Nearest distance to y={y} is {d2}.")
        if d2 <= dist:
            log(f"y={y} is in range.")
            log(f"x is in range {sensor[0] - (dist - d2)} to {sensor[0] + (dist - d2)}")
            minx.append(sensor[0] - (dist - d2))
            maxx.append(sensor[0] + (dist - d2))
        if beacon[1] == y:
            beacons_on_row.add(beacon)
    part1 = max(maxx) - min(minx) - len(beacons_on_row) + 1

    cores = 10
    # rng =np.random.default_rng()
    arr = np.arange(searchsize+1)
    # rng.shuffle(arr)
    arrsplit = np.array_split(arr, cores)

    # arr = np.arange(3800000,4000000)
    arrsplit = np.array_split(arr, cores)

    args = []
    
    for i in range(cores):
        args.append((searchsize, sensors, beacons, distances, arrsplit[i]))

    with Pool(cores) as p:
        part2 = p.map(bruteforce, args)
    # part2 = bruteforce((searchsize, sensors, beacons, distances, arrsplit[0]))

    return (part1, part2)

def bruteforce(args):
    part2 = None
    for i, y2 in enumerate(args[4]):
        if i % 10 == 0:
            log(f"{i}/{len(args[4])}: For y={y2}.")
        xs = set()
        for sensor, dist in zip(args[1], args[3]):
            d2 = distance(sensor, (sensor[0], y2))
            if d2 <= dist:
                lowx = sensor[0] - (dist - d2)
                highx = sensor[0] + (dist - d2) + 1
                x = range(max(0,lowx), min(highx, args[0]+1))
                xs.update(set(x))
                if len(xs) == (args[0]+1):
                    break
        if len(xs) < (args[0]+1):
            full = set(range(0, args[0]+1))
            val = full.difference(xs)
            part2 = val.pop() * 4000000 + y2
            print(part2)
            break
    return part2

if __name__ == "__main__":
    # print(solve("input1.txt", 10, 20))
    print(solve("input2.txt", 2000000, 4000000))

import itertools
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

    df = pd.DataFrame(columns=['sx', 'sy', 'bx', 'by', 'd'])
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
            df.loc[len(df)] = [s_x, s_y, b_x, b_y, distance((s_x, s_y), (b_x, b_y))]
    # visualize(sensors, beacons)
    print(df)

    # df_coords = pd.DataFrame(list(itertools.product(*[np.arange(minx, maxx), np.arange(miny, maxy)])), columns=['x', 'y'])
    xrange = np.arange(0, searchsize+1)
    yrange = np.arange(y)

    print(xrange)
    df_coords = df_coords = pd.DataFrame(itertools.product(*[xrange,yrange]), columns=['x', 'y'])
    print(df_coords)

    df_merged = df.merge(df_coords, how='cross')
    print(df_merged)

    df_merged['d2'] = abs(df_merged['sx'] - df_merged['x']) + abs(df_merged['sy'] - df_merged['y'])
    df_merged['isCovered'] = df_merged['d2'] <= df_merged['d']
    df_merged['isBeacon'] = (df_merged['bx'] == df_merged['x']) & (df_merged['by'] == df_merged['y'])

    # print(df_merged)
    df_filtered = df_merged[(df_merged['isCovered']==True) & (df_merged['y'] == y) & (df_merged['isBeacon'] == False)]
    # print(df_filtered)
    df_grouped = df_filtered.groupby(['x', 'y'])['isCovered'].count()
    # print(df_grouped)
    print(len(df_grouped))
    
    minx = []
    maxx = []
    beacons_on_row = set()
    # for sensor, beacon, dist in zip(sensors, beacons, distances):
    #     log(f"Sensor {sensor} to beacon {beacon} with distance of {dist}.")
    #     d2 = distance(sensor, (sensor[0], y))
    #     log(f"Nearest distance to y={y} is {d2}.")
    #     if d2 <= dist:
    #         log(f"y={y} is in range.")
    #         log(f"x is in range {sensor[0] - (dist - d2)} to {sensor[0] + (dist - d2)}")
    #         minx.append(sensor[0] - (dist - d2))
    #         maxx.append(sensor[0] + (dist - d2))
    #     if beacon[1] == y:
    #         beacons_on_row.add(beacon)
    # part1 = max(maxx) - min(minx) - len(beacons_on_row) + 1

    cores = 8
    rng =np.random.default_rng()
    arr = np.arange(searchsize+1)
    # rng.shuffle(arr)
    arrsplit = np.array_split(arr, cores)

    # arr = np.arange(3000000,3200000)
    # arrsplit = np.array_split(arr, cores)

    args = []
    
    # for i in range(cores):
    #     args.append((searchsize, sensors, beacons, distances, arrsplit[i]))

    # with Pool(cores) as p:
    #     part2 = p.map(bruteforce, args)

    return (part1, part2)

def bruteforce(args):
    part2 = None
    for i, y2 in enumerate(args[4]):
        if i % 1000 == 0:
            log(f"{i}/{len(args[4])}: For y={y2}.")
        # ranges = []
        ranges = np.arange(0, args[0]+1)
        for sensor, dist in zip(args[1], args[3]):
            d2 = distance(sensor, (sensor[0], y2))
            if d2 <= dist:
                ranges = np.setdiff1d(ranges, np.arange(sensor[0] - (dist - d2), sensor[0] + (dist - d2) + 1))
                if len(ranges) == 0:
                    break
        if len(ranges) > 0:
            print(ranges)
            part2 = ranges[0] * 4000000 + y2
            print(part2)
            break
    return part2

if __name__ == "__main__":
    # print(solve("input1.txt", 10, 20))
    print(solve("input2.txt", 2000000, 4000000))

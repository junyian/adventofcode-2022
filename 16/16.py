import re
import copy
from pprint import pprint

DEBUG = True

RATETHRESHOLD = 10
TREE = {}
PATHS = []

def log(log:str):
    if DEBUG==True:
        print(log)

def nextaction(tree, paths):
    pass

def generatePaths(tree):
    global PATHS
    if len(PATHS) == 0:
        if tree['AA']['flow'] < RATETHRESHOLD:
            for child in tree['AA']['child']:
                action = ('AA', 'travel', child, 1)
                path = [action]
                PATHS.append(path)
    else:
        path = PATHS.pop(0)

    pprint(PATHS)

    
def solve(input:str):
    part1, part2 = 0, 0

    with open(input) as f:
        for l in f:
            m = re.match(r"Valve ([A-Z]{2}) has flow rate=(\d+);.*to valve[s]{0,1} (.*)", l.strip())
            valve_src, valve_flow, valve_tgt = list(m.groups())
            TREE[valve_src] = {
                'flow': int(valve_flow),
                'child': valve_tgt.split(', '),
                'isOpen': False
            }
    generatePaths(TREE)
    # pprint(TREE)
    return (part1, part2)

if __name__ == "__main__":
    print(solve("input1.txt"))
    # print(solve("input2.txt"))
import re
from pprint import pprint

DEBUG = True

TREE = {}

def log(log:str):
    if DEBUG==True:
        print(log)

def walk(root, minute):
    if minute == 30:
        return
    else:
        min = minute + 1
        log(f"== Minute {min} ==")
        print(TREE[root]['flow'])
        if TREE[root]['flow'] > 10:
            log(f"You open valve {root}.")
            min = minute + 1
            log(f"== Minute {min} ==")
        for child in TREE[root]['child']:
            if TREE[child]['isOpen'] == False:
                log(f"You move to valve {child}.")
                walk(child, min)
                break

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
    walk('AA', 0)

    pprint(TREE)
    return (part1, part2)

if __name__ == "__main__":
    print(solve("input1.txt"))
    # print(solve("input2.txt"))

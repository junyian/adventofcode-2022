import copy
import numpy

class Monkey:
    def __init__(self):
        self.items = []
        self.operation = ''
        self.test = {
            'divisibleby': 0,
            'true': 0,
            'false': 0
        }
        self.inspected = 0
    
    def __str__(self):
        o = ''
        o += f"Items     : {self.items}\n"
        o += f"Operation : {self.operation}\n"
        o += f"Test      : {self.test}\n"
        return o

monkeys1 = []

lines = open("input2.txt").readlines()

# Parse input
for i in range(len(lines)):
    monkey = None
    if lines[i].strip().startswith("Monkey"):
        monkey = Monkey()
        # Starting items
        startidx = len("Starting items: ")
        str_items = lines[i+1].strip()[startidx:].split(',')
        for v in str_items:
            monkey.items.append(int(v))

        # Operation
        startidx = len("Operation: new = ")
        monkey.operation = lines[i+2].strip()[startidx:]

        # Test
        startidx = len("Test: divisible by ")
        monkey.test['divisibleby'] = int(lines[i+3].strip()[startidx:])

        # True
        startidx = len("If true: throw to monkey ")
        monkey.test['true'] = int(lines[i+4].strip()[startidx:])

        # False
        startidx = len("If false: throw to monkey ")
        monkey.test['false'] = int(lines[i+5].strip()[startidx:])
        i += 6

        monkeys1.append(monkey)

monkeys2 = copy.deepcopy(monkeys1)

# Part 1
for r in range(20):
    # print(f"Round {r+1}")
    for i,m in enumerate(monkeys1):
        # print(f"Monkey {i}:")
        for old in m.items:
            # print(f"  Inspect {old}")
            m.inspected += 1
            new = eval(m.operation)
            worry = int(numpy.floor(new/3))
            if worry % m.test['divisibleby'] == 0:
                monkeys1[m.test['true']].items.append(worry)
            else:
                monkeys1[m.test['false']].items.append(worry)
        m.items.clear()

inspected = []
for i,m in enumerate(monkeys1):
    inspected.append(m.inspected)
inspected.sort(reverse=True)
print(inspected[0] * inspected[1])

# Part 2
divisibility = []
for m in monkeys2:
    divisibility.append(m.test['divisibleby'])
lcmval = numpy.lcm.reduce(divisibility)

for r in range(10000):
    # print(f"Round {r+1}")
    for i,m in enumerate(monkeys2):
        # print(f"Monkey {i}:")
        # print(m.items)
        worries = []
        for old in m.items:
            # print(f"  Inspect {old}")
            m.inspected += 1
            new = eval(m.operation)
            w = int(numpy.floor(new%lcmval))
            worries.append(w)

        for worry in worries:
            # worry = int(worry/divisor)
            if worry % m.test['divisibleby'] == 0:
                monkeys2[m.test['true']].items.append(worry)
            else:
                monkeys2[m.test['false']].items.append(worry)
        m.items.clear()
        # print(f"Monkey {i}: {m.inspected}")

inspected=[]
for i,m in enumerate(monkeys2):
    # print(m.inspected)
    inspected.append(m.inspected)
inspected.sort(reverse=True)
print(inspected[0] * inspected[1])
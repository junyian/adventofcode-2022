import re

lines = open("input1.txt").readlines()

# find bottom of crate
bottom = 0
for l in lines:
    if l.count("[")>0:
        bottom += 1
    else:
        break

crates = lines[bottom].strip().split(" ")
num_of_stacks = len(crates) - crates.count('')

# build the stacks
stacks = [None] * num_of_stacks
for i in range(num_of_stacks):
    stacks[i] = list()

for i in range(bottom-1, -1, -1): # start parsing from bottom of the stack
    for j in range(num_of_stacks):
        c = lines[i][(j*4)+1]
        if c.isalpha():
            stacks[j].append(c)

stacks2 = stacks.deepcopy() # reuse stack for part 2

# move!
for i in range(bottom+2, len(lines)):
    m = re.match(r"move (\d+) from (\d+) to (\d+)", lines[i].strip())
    s_move, s_from, s_to = int(m.group(1)), int(m.group(2)), int(m.group(3))
    for j in range(s_move):
        v = stacks[s_from-1].pop()
        stacks[s_to-1].append(v)

# get top of stacks
o = ''
for i in stacks:
    o += i.pop()
print(o)


# move #2
print(stacks2)
for i in range(bottom+2, len(lines)):
    m = re.match(r"move (\d+) from (\d+) to (\d+)", lines[i].strip())
    s_move, s_from, s_to = int(m.group(1)), int(m.group(2)), int(m.group(3))
    v = []
    for j in range(s_move):
        v.append(stacks2[s_from-1].pop())
    stacks[s_to-1].append(v[::-1])
# get top of stacks
o = ''
for i in stacks2:
    o += i.pop()
print(o)

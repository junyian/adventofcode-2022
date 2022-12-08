import pprint

lines = open("input2.txt").readlines()

paths = {
    '/': {
        'level': 0,
        'files': [],
        'children': [],
        'size': -1
    }
}
cwd = '/'
curlevel = 0
maxlevel = 0

for l in lines:
    if l.startswith("$ cd /"):
        continue
    elif l.startswith("$ ls"):
        continue
    elif l.startswith("dir "):
        path = l.strip()[4:]
        paths[cwd]['children'].append( cwd + path + '/')
    elif l.startswith("$ cd "):
        path = l.strip()[5:]
        if path == "..":
            curlevel -= 1
            loc = cwd.rfind('/', 0, len(cwd)-1)
            cwd = cwd[:loc+1]
        else:
            curlevel += 1
            if maxlevel < curlevel:
                maxlevel = curlevel

            cwd += path + '/'
            paths[cwd] = {
                'level': curlevel,
                'files': [],
                'children': [],
                'size': -1
            }
        # print(cwd)
    elif l[0].isnumeric():
        size = int(l[:l.find(' ')])
        name = l[l.find(' '):].strip()
        paths[cwd]['files'].append((name, size))

for level in range(maxlevel, -1, -1):
    for p in paths:
        if paths[p]['level'] == level:
            size = 0
            if len(paths[p]['children']) == 0:
                for f in paths[p]['files']:
                    size += f[1]
            else:
                for children in paths[p]['children']:
                    size += paths[children]['size']
                for f in paths[p]['files']:
                    size += f[1]
            paths[p]['size'] = size

# pprint.pprint(paths, sort_dicts=False)

# Part 1
score = 0
for p in paths:
    if paths[p]['size'] <= 100000:
        score += paths[p]['size']
print(score)

# Part 2
disksize = 70000000
currentused = paths['/']['size']
requiredspace = 30000000

available = disksize - currentused
remainingneeded = requiredspace - available

# print(remainingneeded)

score = 30000000

for p in paths:
    if paths[p]['size'] > remainingneeded and score > remainingneeded:
        score = paths[p]['size']
print(score)
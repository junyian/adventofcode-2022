import re
import pprint

sizes = []


class Tree():
    root = {
        'path': '',
        'files': [],
        'children': []
    }
    
    def __init__(self, path):
        self.root['path'] = path

    def addFile(self, path, filename, size):
        curpath = self.root
        for p in path:
            if p == '/':
                pass
            else:
                for cp in curpath['children']:
                    if cp['path'] == p:
                        curpath = cp
        curpath['files'].append((filename, size))


    def addPath(self, path):
        curpath = self.root
        # print(f"addPath: {path}")
        for p in path:
            # print(f'loop path {p}')
            if p == '/':
                # print("Root path, skipping.")
                pass
            else:
                # print("Not root path, continue parsing.")
                pathexists = False
                for cp in curpath['children']:
                    if cp['path'] == p:
                        curpath = cp
                        pathexists = True
                        break
                if pathexists == False:
                    # print("\tAdding subpath.")
                    newpath = { 
                        'path': p,
                        'files': [],
                        'children': []
                    }
                    curpath['children'].append(newpath)
                    curpath = newpath
        # pprint.pprint(tree.root, sort_dicts=False)

def main(input):
    tree = Tree('/')

    cpath = ['/']
    for l in open(input).readlines():
        if l.find("$ cd /") == 0 or l.find("$ ls") == 0:
            next
        elif l.find("$ cd ..") == 0:
            cpath.pop()
        elif l.find("$ cd ") == 0:
            cpath.append(l[4:].strip())
            tree.addPath(cpath)
        elif l.find("dir ")>=0:
            pass
        else:
            size = int(l[:l.find(' ')])
            file = l[l.find(' '):].strip()
            tree.addFile(cpath, file, size)
        # print(cpath)

    # print("FINAL TREE")
    pprint.pprint(tree.root, sort_dicts=False)

    def part1(root, limit):
        global sizes

        score = 0
        if len(root['children']) > 0:
            for path in root['children']:
                score += part1(path, limit)
        if len(root['files']) == 0:
            return 0
        else:
            for file in root['files']:
                score += file[1]

        if score > limit:
            score = 0
        else:
            print(root, score)
            sizes.append(score)
        
        return score
        
    # Part 1
    part1(tree.root, 1000000)
    print(sizes)
    print(sum(sizes))

if __name__ == "__main__":
    # main("input1.txt")
    main("input2.txt")
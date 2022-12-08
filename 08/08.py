import numpy

lines = open("input1.txt").readlines()

width = len(lines[0].strip())
height = len(lines)

trees = numpy.zeros((height, width), int)
masks1 = numpy.zeros((height, width), int)
masks2 = numpy.zeros((height, width), int)

for w in range(height):
    for h in range(width):
        trees[w][h] = lines[w][h]

for w in range(height):
    for h in range(width):
        if w==0 or h==0 or w==width-1 or h==width-1:
            masks1[w][h] = 1
        else:
            tree = trees[w][h]

            row = trees[w,]
            col = trees[:,h]

            left = trees[w,:h]
            print(tree, row, left)
            if left.max() < tree:
                masks1[w][h] = 1
            
            score = 0
            if h>1:
                for l in left[::-2]:
                    # print(l)
                    if l >= tree:
                        break
                    else:
                        score += 1
            masks2[w][h] = score+1

            right = trees[w,h+1:]
            # print(tree, row, right)
            if right.max() < tree:
                masks1[w][h] = 1
            
            score = 0
            if h<width-1:
                for l in right[:-1]:
                    if l >= tree:
                        break
                    else:
                        score += 1
            # masks2[i][j] *= score + 1

            top = trees[:w,h]
            # print(tree, col, top)
            if top.max() < tree:
                masks1[w][h] = 1

            score = 0
            if w>1:
                for l in top[::-1]:
                    if l >= tree:
                        break
                    else:
                        score += 1
            # masks2[i][j] *= score + 1

            bottom = trees[w+1:,h]
            # print(tree, col, bottom)
            if bottom.max() < tree:
                masks1[w][h] = 1

            score = 0
            if w<height-1:
                for l in bottom[:-1]:
                    if l >= tree:
                        break
                    else:
                        score += 1
            masks2[w][h] *= score + 1
print(masks1)
print(masks1.sum())

print(masks2[1])
print(masks2.max())
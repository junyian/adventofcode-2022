import numpy
import sys

lines = open("input2.txt").readlines()

width = len(lines[0].strip())
height = len(lines)

trees = numpy.zeros((height, width), int)
masks1 = numpy.zeros((height, width), int)

for w in range(height):
    for h in range(width):
        trees[w][h] = lines[w][h]

for w in range(height):
    for h in range(width):
        if w==0 or h==0 or w==width-1 or h==width-1:
            masks1[h][w] = 1
        else:
            tree = trees[w][h]
            row = trees[w,]
            col = trees[:,h]

            left = trees[w,:h]
            if left.max() < tree:
                masks1[w][h] = 1
            
            right = trees[w,h+1:]
            if right.max() < tree:
                masks1[w][h] = 1

            top = trees[:w,h]
            if top.max() < tree:
                masks1[w][h] = 1

            bottom = trees[w+1:,h]
            if bottom.max() < tree:
                masks1[w][h] = 1

print(masks1.sum())

def countvisible(tree, line):
    retval = 0
    for l in line:
        if l < tree:
            retval += 1
        elif l>=tree:
            retval += 1
            break
    return retval

masks2 = numpy.zeros((height, width), int)

for w in range(height):
    for h in range(width):
        if w>0 and h>0 and w<width-1 and h<height-1:
            tree = trees[w][h]
            row = trees[w,]
            col = trees[:,h]

            left = trees[w,:h]
            masks2[w][h] = countvisible(tree, left[::-1])

            right = trees[w,h+1:]
            masks2[w][h] *= countvisible(tree, right)

            top = trees[:w,h]
            masks2[w][h] *= countvisible(tree, top[::-1])

            bottom = trees[w+1:,h]
            masks2[w][h] *= countvisible(tree, bottom)

print(masks2.max())
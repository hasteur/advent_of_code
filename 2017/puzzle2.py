import itertools
import pdb

def part_1(contents):
    total = 0
    for line in contents:
        minval = -1
        maxval = -1
        for value in line:
            if minval == -1:
                minval = value
            if maxval == -1:
                maxval = value
            if minval > value:
                minval = value
            if maxval < value:
                maxval = value
        total += (maxval - minval)
    return total
                
def part_2(contents):
    total = 0
    for line in contents:
        for i in range(len(line)):
            for j in range(len(line)):
                if i == j: continue
                if line[i] % line[j] == 0:
                    total += (line[i]//line[j])
    return total


fh = open('puzzle2.txt','r')
contents = []
for line in fh.readlines():
    intline = []
    for val in line.split("\t"):
        try:
            intline.append(int(val))
        except:
            pass
    contents.append(intline)
    

print "Part 1: %i" % part_1(contents)
print "Part 2: %i" % part_2(contents)

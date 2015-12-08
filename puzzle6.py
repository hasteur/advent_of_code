import re
light_nums = re.compile("([0-9]+)")
from collections import defaultdict

lights = defaultdict(int)
with open('puzzle6.txt') as fh:
    for line in fh:
        x1, y1, x2, y2 = [int(x) for x in light_nums.findall(line)]
        if line.startswith('toggle'):
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[(x,y)] += 2
        elif line.startswith('turn off'):
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[(x,y)] = max(lights[(x,y)] - 1,0)
        elif line.startswith('turn on'):
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    lights[(x,y)] += 1
print sum(lights.itervalues())

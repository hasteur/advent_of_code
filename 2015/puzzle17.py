import itertools
STORE_AMT=150

containers = []
fh = open('puzzle17.txt', 'r')
for line in fh:
    containers.append(int(line))
found_amt = 0
combinations = [ c for i in xrange(1,len(containers)+1) for c in itertools.combinations(containers,i) if sum(c) == 150]
print len(combinations)
print len([c for c in combinations if len(c) == len(min(combinations, key=lambda x:len(x)))])


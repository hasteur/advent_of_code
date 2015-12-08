
accumulator = 0
with open('puzzle8.txt','r') as fh:
    for line in fh:
        accumulator += (len(line[:-1]) - len(eval(line)))

print "Meta Char length: %i" % accumulator

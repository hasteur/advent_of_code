
accumulator = 0
with open('puzzle8.txt','r') as fh:
    for line in fh:
        accumulator += 2 + line.count('\\') + line.count('"')

print "Meta Char length: %i" % accumulator

def build_key(locX,locY):
    """
        Build the key to string
    """
    return "%s%s" % (locX,locY)
x = y = 0
n = 2
coords = [(0,0)] *n
houses = set([(0,0)])
with open('puzzle3.txt','r') as f:
    chars = f.read()
    chunks = [chars[i:i+n] for i in xrange(0,len(chars),n)]
    for chunk in chunks:
        for i,instruction in enumerate(chunk):
            x,y = coords[i]
            if instruction == '^':
                y -= 1
            elif instruction == '>':
                x += 1
            elif instruction == 'v':
                y += 1
            elif instruction == '<':
                x -= 1
            else:
               print instruction
               print "FAILURE!!!"
               continue
            houses.add((x,y))
            coords[i] = (x,y)

print len(houses)

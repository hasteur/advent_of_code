

# Adapted from https://stackoverflow.com/questions/13673060/

fh = open('puzzle1.txt','r')
contents = fh.read().strip()
fh.close()

potential_lists = [contents[i:i+2] for i in range(0,len(contents)-1,1)]
potential_lists.append(contents[-1]+contents[0])
#print potential_lists
matched_lists = []
for i in potential_lists:
    if i[0] == i[1] and len(i) == 2:
        matched_lists.append(int(i[0]))
print "Part 1: %i" % sum(matched_lists)

p2_pivot = len(contents)/2
p2_list = contents + contents[0:p2_pivot]
p2_potentials = [p2_list[i]+p2_list[i+p2_pivot] for i in range(0,len(contents)-1,1)]
p2_matches = []
for i in p2_potentials:
    if i[0] == i[1] and len(i) == 2:
        p2_matches.append(int(i[0]))
print "Part 2: %i" % sum(p2_matches)


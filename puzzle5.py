import re
# Make sure we have at least 3 vowels somwhere
g1 = re.compile("([a-z][a-z]).*\\1") 
# Make sure there are double eltters somewhere
g2 = re.compile("([a-z])[a-z]\\1") # Has double letter
# Can't have any of these.
with open('puzzle5.txt') as f:
    # Count up the number of lines that match all of our criteria.
    print len([ l for l in f 
              if g1.search(l) and g2.search(l) ])

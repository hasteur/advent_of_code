import hashlib

start_key = 'iwrupvqb'
sequence = input("Sequence #? ")
base_offset = 1000000*sequence
for i in range(base_offset,base_offset+1000000):
    hash_out = hashlib.md5(start_key+str(i)).hexdigest()
    if hash_out.startswith('000000'):
        print "Match on %i" % i
        break


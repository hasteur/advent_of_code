import re
class Aunt:
    name = ''
    def __init__(self, name):
        self.name = name
        self.count = {'children':-1,
                      'cats' : -1,
                      'samoyeds' : -1,
		      'pomeranians' : -1,
                      'akitas' : -1,
                      'vizslas' : -1,
                      'goldfish' : -1,
                      'trees' : -1,
                      'cars' : -1,
                      'perfumes' : -1}
    def setCount(self, key, value):
    	self.count[key.strip()] = value
    def filterKey(self, key, value):
    	if self.count[key] == -1:
	    return True
	else:
	    return self.count[key] == value
    def filterCalib(self, key, value):
        if self.count[key] == -1:
	    return True
	else:
	    if key in ('cats', 'trees'):
	        return self.count[key] > value
	    if key in ('pomeranians','goldfish'):
	        return self.count[key] < value
            return self.count[key] == value

def filterRule(AuList, key, val):
    RetAu = []
    for Aun in AuList:
        if Aun.filterCalib(key, val):
	    RetAu.append(Aun)
    return RetAu

AuntList = []
fh = open('puzzle16.txt','r')
match_rule = re.compile('(?P<Name>Sue [0-9]{1,3}): (?P<attrib>.+)$')
for line in fh:
    matches = match_rule.match(line) 
    a = Aunt(matches.group('Name'))
    attrib_list = matches.group('attrib').split(',')
    for attri in attrib_list:
    	key = attri.split(': ')[0]
	val = int(attri.split(': ')[1])
	a.setCount(key, val)
    AuntList.append(a)
    a = None

print len(AuntList)
F1 = filterRule(AuntList, 'children', 3)
print len(F1)
F2 = filterRule(F1, 'cats', 7)
print len(F2)
F3 = filterRule(F2, 'samoyeds', 2)
print len(F3)
F4 = filterRule(F3, 'pomeranians', 3)
print len(F4)
F5 = filterRule(F4, 'akitas', 0)
print len(F5)
F6 = filterRule(F5, 'vizslas', 0)
print len(F6)
F7 = filterRule(F6, 'goldfish', 5)
print len(F7)
F8 = filterRule(F7, 'trees', 3)
print len(F8)
F9 = filterRule(F8, 'cars', 2)
print len(F9)
F10 = filterRule(F9, 'perfumes', 1)
print len(F10)


import re
stops = []
distances = dict()

parse_re = re.compile('(.*?) to (.*?) = (\d*)')

with open('puzzle9.txt','r') as file_handle:
    for line in file_handle:
        source, destination, distance = parse_re.match(line).groups()
        if source not in stops:
            stops.append(source)
        if destination not in stops:
            stops.append(destination)
        distances.setdefault(source,dict())[destination] = int(distance)
        distances.setdefault(destination,dict())[source] = int(distance)
print distances



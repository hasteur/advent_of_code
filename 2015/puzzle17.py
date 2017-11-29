
STORE_AMT=150

container_list = []
fh = open('puzzle17.txt', 'r')
for line in fh:
    container_list.append(int(line))

container_list.sort()
list_max = container_list[::-1]

base_index = 0

for max_cont_index in range(0,len(list_max)):
    print list_max[max_cont_index]

temp = []
with open("GRE.txt",'r') as hi:
    for line in hi:
        temp.append(line)
temp.sort()
filename = open('SortedGRE.txt','w')
for i in temp:
    filename.write(i)
    #filename.write('\n')

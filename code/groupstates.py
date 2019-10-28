file = open('states', 'r', encoding = 'utf-8')
states = dict()
for line in file:
    line = line.strip()
    line = line.title()
    if line not in states.keys():
        states[line] = 1
    else:
        states[line] += 1
file.close()
file = open('groupstates.txt', 'w', encoding = 'utf-8')
for key, value in states.items():
    file.write(key + ',' + str(value) + '\n')
file.close()


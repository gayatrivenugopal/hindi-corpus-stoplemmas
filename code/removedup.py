final = open('final', 'r', encoding = 'utf-8')
fetched = open('metadata.txt', 'r', encoding = 'utf-8')
todo = open('todo.txt', 'w', encoding = 'utf-8')

lines = list()
for line in fetched:
    print(line)
    lines.append(line.split(',')[0].strip('\n'))


for line in final:
    if line.strip('\n') not in lines:
        todo.write(line)

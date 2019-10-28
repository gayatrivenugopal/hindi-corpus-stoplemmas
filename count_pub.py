file = open('authors.txt', 'r', encoding = 'utf-8')
count = open('author_count.txt', 'w', encoding = 'utf-8')
authors = dict()
for line in file:
    if line.strip('\n').strip() not in authors.keys():
        authors[line.strip('\n').strip()] = 1
    else:
        authors[line.strip('\n').strip()] = authors[line.strip('\n').strip()] + 1

for key, value in authors.items():
    count.write(key + ',' + str(value) + '\n')
    
count.close()
file.close()
    

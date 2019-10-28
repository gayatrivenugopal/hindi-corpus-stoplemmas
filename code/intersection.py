def gen_intersection(files):
    intersection_temp = list()
    intersection = list()
    for item in files:
        temp = dict()
        file = open(item, 'r', encoding = 'utf-8')
        for line in file:
            line = line.strip('\n')
            temp_list = line.split(',')
            temp[temp_list[0]] = int(temp_list[1])
        intersection_temp.append(temp)

    if len(intersection_temp[0]) > len(intersection_temp[1]):
        small = intersection_temp[1]
        large = intersection_temp[0]
    else:
        small = intersection_temp[0]
        large = intersection_temp[1]
    for word, count in small.items():
        if word in large.keys():
            total = int(count) + int(large[word])
            intersection.append(word + "," + str(total))

    file = open('intersection.txt', 'w', encoding = 'utf-8')
    for word in intersection:
        file.write(word + '\n')
    file.close()

gen_intersection(['union_corpora_lemma.txt','union_public_lemma.txt'])

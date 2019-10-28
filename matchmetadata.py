drive = open('metadata from drive', 'r', encoding = 'utf-8')
metadata = open('metadata.txt', 'r', encoding = 'utf-8')
finalmetadata = open('finalmetadata.txt', 'w', encoding = 'utf-8')
extra = open('extra.txt', 'w', encoding = 'utf-8')

drive_set = set()
for line in drive:
    drive_set.add(line.strip())

metadata_dict = dict()
for line in metadata:
    if line.split(',')[0].strip() not in metadata_dict.keys():
        metadata_dict[line.split(',')[0].strip()] = ','.join(line.split(',')[1:])

drive_list = list(drive_set)
for item in drive_list:
    if item in metadata_dict.keys():
        finalmetadata.write(item + ',' + metadata_dict[item] + '\n')
    else:
        extra.write(item + ',' + 'UNK, UNK, UNK, UNK')

drive.close()
metadata.close()
finalmetadata.close()
extra.close()

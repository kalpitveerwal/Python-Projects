import csv
import json

with open("infinity_stones.csv","w"):
    pass
with open('infinity_stones.json') as data_file:
    infi_parsed=json.loads(data_file.read())

infi_data=infi_parsed["Infinity Stones"]
data=open("infinity_stones.csv","w")
csvwriter=csv.writer(data, delimiter='|')
count=0
for dat in infi_data:
    if count == 0:
        header = dat.keys()
        csvwriter.writerow(header)
        count += 1
    csvwriter.writerow(dat.values())

with open('infinity_stones.csv', 'r') as f:
    file_lines = [''.join([x.strip(), '|' , '\n']) for x in f.readlines()]

with open('infinity_stones.csv', 'w') as f:
    f.writelines(file_lines) 
    


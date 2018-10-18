import numpy as np
import csv
import os
from numpy import genfromtxt
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 

data1=list(csv.reader(open('info_day.csv')))
data2=list(csv.reader(open('info_night.csv')))
data=np.column_stack([data1,data2])

np.savetxt("info_combined1.csv", data, delimiter=',', fmt='%s')
with open("info_combined1.csv","rb") as source:
    rdr= csv.reader( source )
    with open("info_combine.csv","wb") as result:
        wtr= csv.writer( result )
        for r in rdr:
            wtr.writerow( (r[0], r[1], r[6], r[2], r[7], r[3], r[8], r[4], r[9]) )

r = csv.reader(open('info_combine.csv')) 
lines = list(r)
lines[0][1]='Temperature(Day)'
lines[0][2]='Temperature(Night)'
lines[0][3]='Humidity(Day)'
lines[0][4]='Humidity(Night)'
lines[0][5]='Light(Day)'
lines[0][6]='Light(Night)'
lines[0][7]='CO2(Day)'
lines[0][8]='CO2(Night)'

writer = csv.writer(open('info_combine.csv', 'w'))
writer.writerows(lines)
os.remove('info_combined1.csv')

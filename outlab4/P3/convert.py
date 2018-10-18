import numpy
import warnings
import csv
warnings.filterwarnings("ignore", category=numpy.VisibleDeprecationWarning) 
def celToFar(cel):
    return (9*cel)/5+32
      
from numpy import genfromtxt
my_data = genfromtxt('info_day.csv', delimiter=',',dtype=None)

for i in range(1,8):
	my_data[i][1]=str(celToFar(float(my_data[i][1])))

data=list(csv.reader(open('info_day.csv')))

numpy.savetxt('transformed.csv', data , delimiter=',',fmt='%s')
r = csv.reader(open('transformed.csv')) 
lines = list(r)
for i in range(1,8):
	lines[i][1]=my_data[i][1]
writer = csv.writer(open('transformed.csv', 'w'))
writer.writerows(lines)





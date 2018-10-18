import numpy
from numpy import genfromtxt
my_data = genfromtxt('info_day.csv', delimiter=',')
mean_array=[]
stddev_array=[]
for i in my_data.T:
   i= i[~numpy.isnan(i)]
   if(i.size!=0):
       mean_array.append(i.mean())
       stddev_array.append(i.std())
       
print('Field           Mean                         Std. Dev.')
print('Temperature    ',mean_array[0], '                    ',stddev_array[0])
print('Humidity       ',mean_array[1], '              ',stddev_array[0])
print('Light          ',mean_array[2], '              ',stddev_array[0])
print('CO2            ',mean_array[3], '                     ',stddev_array[0])
       

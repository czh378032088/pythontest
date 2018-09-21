import csv
import numpy
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
csv_file = numpy.loadtxt('F:\\code\\pythontest\\data\\20180907-15-08-01.dat',delimiter=',')
#print(csv_file)
#print(csv_file[:,0])
#print(csv_file[:,3].mean())
csv_file[:,3] = csv_file[:,3] - csv_file[:,3].mean()
plt.figure(1)
plt.subplot(211);
plt.plot(csv_file[:,0],csv_file[:,1] ,color='r',label='纵轴误差')
plt.plot(csv_file[:,0],csv_file[:,8] ,color='y',label='纵轴相对调整')
plt.plot(csv_file[:,0],csv_file[:,3],color='blue',label='纵轴绝对调整')
plt.legend(loc='upper left')

plt.subplot(212);

plt.plot(csv_file[:,0],csv_file[:,7],color='r',label='横轴误差')
plt.plot(csv_file[:,0],csv_file[:,8],color='y',label='横轴调整')

plt.legend(loc='upper left')
plt.show()

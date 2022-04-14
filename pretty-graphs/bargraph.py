import matplotlib.pylab as plt
import numpy as np

dates = []
registration = []
counterarray = []

counter = 0;
f = open("sample-bar.txt", 'r')
for row in f:
    counterarray.append(counter)
    row = row.split(' ')
    dates.append(row[0])
    registration.append(row[1])
    counter+=1
print(counterarray)
plt.bar(counterarray, registration, align='center')

plt.xticks(counterarray, dates)
#plt.bar(dates, registration, color = 'g', label = 'data')
plt.show()

#different functions
#with open






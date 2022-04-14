import numpy as np
import matplotlib.pyplot as plt

grades=[]
with open("grades.txt") as f:
    for line in f:
        grades.append(float(line))

#sort data
x = np.sort(grades)

#calculate CDF values
y = 1. * np.arange(len(grades)) / (len(grades) - 1)

#plot CDF
plt.plot(x, y)
plt.show()
#plt.xlabel('x')
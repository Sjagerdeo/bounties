import numpy as np
import matplotlib.pyplot as plt

timings=[]
with open("timings.txt") as f:
    for line in f:
        timings.append(float(line))

#sort data
x = np.sort(timings)

#calculate CDF values
y = 1. * np.arange(len(timings)) / (len(timings) - 1)

#plot CDF
plt.plot(x, y)
plt.show()
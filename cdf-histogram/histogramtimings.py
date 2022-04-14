import matplotlib.pyplot as plt
import numpy as np

timings=[]
with open("timings.txt") as f:
    for line in f:
        timings.append(float(line))
num_bins = 72
# the histogram of the data
n, bins, patches = plt.hist(timings, num_bins, range=[0,180], normed = True, histtype='bar',facecolor='magenta')
plt.show()
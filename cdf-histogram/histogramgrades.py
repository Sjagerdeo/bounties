import matplotlib.pyplot as plt
import numpy as np

grades=[]
with open("grades.txt") as f:
    for line in f:
        grades.append(float(line))
num_bins = 72
# the histogram of the data
n, bins, patches = plt.hist(grades, num_bins, range=[0,180], normed = True, histtype='bar',facecolor='magenta')
plt.show()
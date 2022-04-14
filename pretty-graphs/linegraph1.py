from subprocess import list2cmdline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('sample.csv')

df.plot(kind = 'line', x = 'Duration', y = 'Calories')

plt.show()
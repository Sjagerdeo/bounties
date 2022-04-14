from subprocess import list2cmdline
import matplotlib.pyplot as plt
import numpy as np


def parse (newfile,x,y1,y2):
    x = []
    y1 = []
    y2 =[]
    with open(newfile, 'r') as fileread:
        for row in fileread:
         row = row.split(" ")
         x.append(row[0])
         y1.append(row[1])
         y2.append(row[2])
    return x,y1,y2

def xAxis (result):
    #result is a list of x y1 and y2
    return result[0]

def y1Data (result):
    #result is a list of x y1 and y2
    return result[1]

def y2Data (result):
    #result is a list of x y1 and y2
    return result[2]


def plot (x,y1,y2):
    plt.plot(x, y1, label = "line 1")
    plt.plot(x, y2, label = "line 2")
    plt.show()

#Calling function
x = []
y1 = [] 
y2 =[]
result1 = parse("sample.txt",x,y1,y2)
list1 = xAxis(result1)
list2 = y1Data(result1)
list3 = y2Data(result1)
plot(list1,list2,list3)




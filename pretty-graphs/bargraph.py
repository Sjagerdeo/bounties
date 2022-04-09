import matplotlib.pyplot as plt

dates = []
registration = []

f = open('sample-bar.txt', 'r')
for row in f:
    row = row.split(' ')
    dates.append(row[0])
    registration.append(str (row[1]))

plt.bar(dates, registration)
plt.title('Bar Graph')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
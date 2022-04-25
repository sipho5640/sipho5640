import matplotlib.pyplot as plt

# Look at index 4 and 6, which demonstrate overlapping cases.
x1 = [1, 3, 4, 5, 6, 7, 9]
y1 = [4, 7, 2, 4, 7, 8, 3]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 6, 2, 6, 2]


plt.bar(x1, y1, label="Fungi", color='b')
plt.bar(x2, y2, label="Viruses", color='g')
plt.plot()

plt.xlabel("Tests Done")
plt.ylabel("Positive Tests")
plt.title("Health Care Associated Infections")
plt.legend()
plt.show()
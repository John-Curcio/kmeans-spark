import csv
import matplotlib.pyplot as plt 

################
# Cross-Validation Min Cost
x, y = [], []
with open('kmeans-crossval.csv', newline='') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        x.append(int(row[0])) 
        y.append(float(row[1]))


plt.plot(x, y)
plt.title("Cross-Validated Cost as a Function of $k$")
plt.xlabel("Number of Cluster Centers $k$")
plt.ylabel("10-fold Cross-Validated Minimum Cost")
plt.show()

###############
# Sans Cross-Validation
x, y = [], []
with open('kmeans-sans-crossval.csv', newline='') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        x.append(int(row[0])) 
        y.append(float(row[1]))


plt.plot(x, y)
plt.title("Cost as a Function of $k$")
plt.xlabel("Number of Cluster Centers $k$")
plt.ylabel("Minimum Cost, Sans Cross-Validation")
plt.show()


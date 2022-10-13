# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import json

# A custom function to calculate
# probability distribution function
def pdf(x):
	mean = np.mean(x)
	std = np.std(x)
	y_out = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std**2))
	return y_out
	
# To generate an array of x-values
x = []#<class 'numpy.ndarray'>
with open("jsons\simulation\players_1665681834078_2000.json", "r") as f:
    data = json.load(f)
for i in data:
    x.append(i["elo"])


# To generate an array of
# y-values using corresponding x-values
y = pdf(x)

# Plotting the bell-shaped curve
plt.style.use('seaborn')
plt.figure(figsize = (6, 6))
plt.plot(x, y, color = 'black',
		linestyle = 'dashed')

plt.scatter( x, y, marker = 'o', s = 25, color = 'red')
plt.show()
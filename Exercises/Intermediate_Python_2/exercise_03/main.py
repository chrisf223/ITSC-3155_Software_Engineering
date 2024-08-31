## Create a virtual environment (with any name) and activate it. Install the numpy package in this virtual environment (pip install numpy). 
## Numpy is a statistical package used for matrices and linear algebra and is vital for data analysis, data science, machine learning, etc. in Python. 
## Use the internet and online documentation to use numpy to create a numpy list of 10 random floats, each 0 to 1, then print the mean, median, and standard deviation of that list, all using numpy. 
## Remember to add a requirements.txt file to this exercise folder, commit it, but do NOT commit the virtual environment folder.

import numpy as np

random_floats = np.random.rand(10)

print("Random Numbers:", random_floats)

mean_value = np.mean(random_floats)
median_value = np.median(random_floats)
std_deviation = np.std(random_floats)

print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)

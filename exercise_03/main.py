import numpy as np

random_floats = np.random.rand(10)

print("Random Numbers:", random_floats)

mean_value = np.mean(random_floats)
median_value = np.median(random_floats)
std_deviation = np.std(random_floats)

print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)

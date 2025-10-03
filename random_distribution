import numpy as np
import matplotlib.pyplot as plt
import random as rd

# create a 100*10 array of random numbers
arrays = [np.array([rd.random() for _ in range(100)]) for _ in range(10)]

# bubble sort
def bubble_sort(arr):
    arr = arr.copy()           # work on a copy to preserve the original
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:       # optimization: if nothing has been exchanged, it is already sorted
            break
    return arr

# we apply bubble_sort to all 10 sublists
sorted_lists = [bubble_sort(a) for a in arrays]

# Concatenate all values ​​into a single array 1000 values ​​(10*100)
sorted_array = np.concatenate(sorted_lists)
# Frequency in percentage of each value
frequencies, bin_edges = np.histogram(sorted_array, bins=10, range=((0.0, 1.0)))
frequencies = frequencies / len(sorted_array) * 100

# histogram of values
plt.bar(bin_edges[:-1], frequencies, width=0.1, edgecolor='black')
plt.xlabel('Value Range')
plt.ylabel('Frequency (%)')
plt.title('Histogram of Sorted Random Values')
plt.xticks(bin_edges)
plt.show()

# calculation of the mean and standard deviation
mean = np.mean(sorted_array)
std_dev = np.std(sorted_array)
print(f'Mean: {mean},Standard Deviation: {std_dev}')
# Calculate the maximum and minimum values ​​of the array
max_value = np.max(sorted_array)
min_value = np.min(sorted_array)
print(f'Max Value: {max_value}, Min Value: {min_value}')
# Calculation of the time taken by the CPU to sort the array and total time to compile the code
import time
start_time = time.time()
# array sorting
bubble_sort(sorted_array)
end_time = time.time()
cpu_time = end_time - start_time
print(f'CPU Time for sorting the array: {cpu_time} seconds ')
total_time = time.process_time()
print(f'Total CPU Time: {total_time} seconds ')

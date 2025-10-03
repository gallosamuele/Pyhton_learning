# Random Values Histogram

This project generates **1000 random numbers** uniformly distributed in the interval [0,1) and analyzes them using a simple **bubble sort** algorithm (for educational purposes).  

The values are then divided into **10 equal intervals**, and the **relative frequency** (percentage) of each interval is calculated.

## Resulting Plot

The code produces a **histogram of the random numbers distribution**:

- **X-axis:** intervals [0.0–0.1), [0.1–0.2), … [0.9–1.0)  
- **Y-axis:** percentage of values observed in each interval  

Since the numbers are generated according to a uniform distribution, each bar is expected to be approximately **10%**, with slight fluctuations due to the finite number of samples.

## Project Goals

- Visually verify the quality of the random number generator  
- Practice array manipulation and data sorting  
- Create simple and interpretable visualizations with Python

## Technologies Used

- Python  
- NumPy (random number generation, arrays)  
- Matplotlib (plotting)  

---

> This project is part of a collection of mini Python learning experiments.


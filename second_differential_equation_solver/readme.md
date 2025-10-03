# Second-Order ODE Solver

This program solves second-order linear homogeneous differential equations with constant coefficients of the form:

\[
x''(t) + b \, x'(t) + c \, x(t) = 0
\]

---

## Features

- Interactive input of the coefficients \(b\) and \(c\).  
- Handles the three main cases:
  - **Distinct real roots**  
  - **Repeated real root**  
  - **Complex roots**  
- Computes the symbolic solution using **Sympy**.  
- Converts the symbolic solution into a numerical function for the **plot of the solution** with Matplotlib.  
- Allows choosing arbitrary constants \(A\) and \(B\) of the general solution.  

---
## Usage Example

```bash
$ python3 second_order_ode.py
Enter b: 2
Enter c: 1
Constant A (default=1): 1
Constant B (default=1): 1

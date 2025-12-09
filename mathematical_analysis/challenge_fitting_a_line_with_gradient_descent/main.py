import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic dataset (years of experience vs. salary)
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75])

# Initialize slope and intercept
# Start with zero for both
m, b = 0, 0
# Set the learning rate
alpha = 0.01
# Define the number of iterations
iterations = 1000

# Gradient Descent Loop
for i in range(iterations):
    # Compute predicted values using current m and b
    y_pred = m*x+b
    # Compute the difference between predicted and actual
    error = y_pred-y
    # Compute gradient for slope (m)
    grad_m = (2/len(x))*np.sum(error*x)
    # Compute gradient for intercept (b)
    grad_b = (2/len(x))*np.sum(error)
    # Update slope
    m -= alpha*grad_m
    # Update intercept
    b -= alpha*grad_b
    
# Compute final predicted values using trained m and b
y_final = m*x+b

# Plot original data and line of best fit
plt.scatter(x, y, label="Data Points")
plt.plot(x, y_final, color='red', label="Best Fit Line")
plt.xlabel("Years of Experience")
plt.ylabel("Salary ($1000)")
plt.legend()
plt.grid(True)
plt.show()

# Print final slope and intercept
print(f"Final slope (m): {m}")
print(f"Final intercept (b): {b}")

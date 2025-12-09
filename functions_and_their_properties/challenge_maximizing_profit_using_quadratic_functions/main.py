import numpy as np
import matplotlib.pyplot as plt

# Define coefficients
a, b, c = -1,12,-20

# Vertex formula
x_vertex = -b/(2*a)

# Calculate maximum profit
max_profit = a*(x_vertex**2)+b*x_vertex+c

# Compute discriminant for quadratic equation
discriminant = b**2-4*a*c
if discriminant >= 0:
    # Insert first root of quadratic
    x1 = x_vertex+(np.sqrt(discriminant)/(2*a))

    # Insert second root of quadratic
    x2 = x_vertex-(np.sqrt(discriminant)/(2*a))

    # Fill in pertinent x1 and x2
    breakeven_points = (x1,x2)

else:
    breakeven_points = None

# Generate x values for plotting
x = np.linspace(0, 12, 100)

# Compute y.
y = a*(x**2)+b*x+c

# Plot profit function
plt.plot(x, y, label="Profit Function", color='blue')
plt.scatter([x_vertex], [max_profit], color='red', label="Max Profit")
if breakeven_points:
    plt.scatter([x1, x2], [0, 0], color='green', label="Breakeven Points")

# Graph labels and styling
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(x_vertex, color='red', linestyle="dashed", linewidth=0.5)
plt.xlabel("Units Sold")
plt.ylabel("Profit ($1000)")
plt.title("Profit Maximization Analysis")
plt.legend()
plt.grid(True)
plt.show()

# Print results
print(f"Optimal units to sell for max profit: {x_vertex:.2f}")
print(f"Maximum profit: ${max_profit*1000:.2f}")
if breakeven_points:
    print(f"Breakeven Points: {x1:.2f}, {x2:.2f}")
else:
    print("No breakeven points (always profitable or always at a loss).")
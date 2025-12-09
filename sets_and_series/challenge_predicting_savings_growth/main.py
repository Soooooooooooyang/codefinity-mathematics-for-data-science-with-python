import numpy as np
import matplotlib.pyplot as plt

# Given values
P = 10000  
r = 0.08  
n = 12  
t = 20  

# Compute total amount using the compound interest formula
A = P*(1+(r/n))**(n*t)  

# Compute interest earned
interest_earned = A-P

# Simulate savings growth over time
years = np.linspace(0, t, t * n + 1)
amounts = P*(1+(r/n))**(n*years)   

# Plot savings growth
plt.figure(figsize=(8,5))
plt.plot(years, amounts, marker='o', linestyle='-', color='b', label="Total Savings")
plt.xlabel("Years")
plt.ylabel("Amount ($)")
plt.title("Savings Growth Over Time with Compound Interest")
plt.legend()
plt.grid(True)
plt.show()

# Print results
print(f"Total Savings after {t} years: ${A:.2f}")
print(f"Interest Earned: ${interest_earned:.2f}")
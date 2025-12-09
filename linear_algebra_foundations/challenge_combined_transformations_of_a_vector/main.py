import numpy as np
import matplotlib.pyplot as plt

# 1. Define the original vector
v = np.array([[2], [3]])

# 2. Define the scaling matrix
S = np.array([[2, 0],
              [0, 0.5]])  

# 3. Apply scaling
scaled_v = S @ v

# 4. Define the 90° CCW rotation matrix
theta = np.pi / 2
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])  

# 5. Apply rotation
rotated_v = R @ scaled_v

# 6. Plot vectors
origin = np.zeros(2)
fig, ax = plt.subplots(figsize=(6, 6))
ax.quiver(*origin, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Original')
ax.quiver(*origin, scaled_v[0], scaled_v[1], angles='xy', scale_units='xy', scale=1, color='green', label='Scaled')
ax.quiver(*origin, rotated_v[0], rotated_v[1], angles='xy', scale_units='xy', scale=1, color='red', label='Rotated')

# 7. Label tips
ax.text(v[0][0] + 0.2, v[1][0] + 0.2, "(2, 3)", color='blue')
ax.text(scaled_v[0][0] + 0.2, scaled_v[1][0] + 0.2, "(4, 1.5)", color='green')
ax.text(rotated_v[0][0] - 0.6, rotated_v[1][0] + 0.1, "(-1.5, 4)", color='red')
ax.text(0, 0, "(0, 0)", fontsize=10)

# 8. Draw coordinate axes
ax.annotate("", xy=(5, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="->", linewidth=1.5, color='black'))
ax.annotate("", xy=(0, 5), xytext=(0, 0), arrowprops=dict(arrowstyle="->", linewidth=1.5, color='black'))
ax.text(5.2, 0, "X", fontsize=12)
ax.text(0, 5.2, "Y", fontsize=12)

# 9. Final layout
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.grid(True)
ax.legend()
ax.set_title("Intermediate Challenge: Combined Transformations")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
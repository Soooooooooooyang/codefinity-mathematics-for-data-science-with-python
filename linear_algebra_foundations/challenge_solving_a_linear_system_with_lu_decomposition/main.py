import numpy as np

# Define matrix A and vector b
A = np.array([[4, 3, 0],
              [3, 4, -1],
              [0, -1, 4]], dtype=float)

b = np.array([24, 30, -24], dtype=float)

# Initialize L and U matrices
L = np.zeros_like(A)
U = np.zeros_like(A)

# LU Decomposition
n = A.shape[0]

for i in range(n):
    # Compute U's ith row
    for j in range(i, n):
        # Fill in the expression
        U[i, j] = A[i,j]-np.sum(L[i,:i]*U[:i,j])  

    # Compute L's ith column
    for j in range(i, n):
        if i == j:
            # Diagonal of L is 1
            L[i, i] = 1 
            # Fill in the expression
        else:
            L[j, i] = (A[j,i]-np.sum(L[j,:i]*U[:i,i])  )/U[i,i] 

# Forward substitution to solve Ly = b
y = np.zeros_like(b)
for i in range(n):
    # Fill in the expression
    y[i] = b[i]-np.sum(L[i,:i]*y[:i])  

# Backward substitution to solve Ux = y
x = np.zeros_like(b)
for i in reversed(range(n)):
    # Fill in the expression
    x[i] = (y[i]-np.sum(U[i,i+1:]*x[i+1:]))/U[i,i]  

print("Solution from LU Decomposition:", x)

# Verify with NumPy built-in solver
x_np = np.linalg.solve(A, b)
print("Solution from np.linalg.solve:", x_np)
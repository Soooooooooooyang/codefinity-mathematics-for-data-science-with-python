import numpy as np

# --- Given Data ---

# Total rods, defective, long, both defective and long
total_rods = 100
defective = 20
long = 30
defective_and_long = 10

# --- Task 1: Probabilities ---

# Probability a rod is defective or long
D = defective/total_rods
L = long/total_rods
both = defective_and_long/total_rods
P_D_or_L = D+L-both

# Probability a rod is defective given it is long
P_D_given_L = both/L

# --- Task 2: Sampling & Statistics ---

np.random.seed(0)

population_mean = 50
population_std = 0.5
sample_size = 10

# Generate sample of rod lengths
sample_lengths = np.random.normal(loc=population_mean, scale=population_std, size=sample_size)

# Sample mean
sample_mean = np.mean(sample_lengths)

# Sample variance
sample_variance = np.var(sample_lengths,ddof=1)

# Sample standard deviation
sample_std = np.std(sample_lengths,ddof=1)

# --- Output results ---
print(f"P(Defective or Long): {P_D_or_L:.4f}")
print(f"P(Defective | Long): {P_D_given_L:.4f}")
print(f"Sample mean: {sample_mean:.2f}")
print(f"Sample variance: {sample_variance:.4f}")
print(f"Sample standard deviation: {sample_std:.4f}")
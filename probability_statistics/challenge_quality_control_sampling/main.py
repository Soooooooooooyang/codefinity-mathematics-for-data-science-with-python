import random
import math
import matplotlib.pyplot as plt
# Parameters for Normal distribution: mean and variance given
mu = 200           
variance = 25      
# Calculate standard deviation sigma from variance
sigma = math.sqrt(25)     
# Parameters for Binomial distribution: number of trials and success probability
n = 20           
p = 0.05           
# Parameters for Uniform distribution: lower and upper bounds for tolerance
a = 49.5           
b = 50.5           
# Function to generate samples from Normal distribution manually
def sample_normal(mu, sigma, size=1000):
    samples = []
    for _ in range(size):
        # Generate one sample using random.gauss
        sample = random.gauss(mu,sigma)  
        samples.append(sample)
    return samples
# Function to generate samples from Binomial distribution manually
def sample_binomial(n, p, size=1000):
    samples = []
    for _ in range(size):
        successes = 0
        # Simulate n Bernoulli trials for each sample
        for _ in range(n):
            r = random.random()
            # Count a success if random number is less than p
            if r < p:   
                successes += 1
        samples.append(successes)
    return samples
# Function to generate samples from Uniform distribution manually
def sample_uniform(a, b, size=1000):
    samples = []
    for _ in range(size):
        r = random.random()
        # Scale random value to uniform range [a, b]
        val = a+(b-a)*r    
        samples.append(val)
    return samples
# Generate samples for each distribution
normal_samples = sample_normal(mu, sigma)
binomial_samples = sample_binomial(n, p)
uniform_samples = sample_uniform(a, b)
# Plot histogram for Normal distribution samples
fig, axs = plt.subplots(1, 3, figsize=(15,4))
axs[0].hist(normal_samples, bins=30, color='skyblue', edgecolor='black')
axs[0].set_title("Normal Distribution (Weight)")
axs[0].set_xlabel("Weight (grams)")
axs[0].set_ylabel("Frequency")
# Plot histogram for Binomial distribution samples
axs[1].hist(binomial_samples, bins=range(n+2), color='lightgreen', edgecolor='black', align='left')
axs[1].set_title("Binomial Distribution (Defects)")
axs[1].set_xlabel("Number of Defective Rods")
axs[1].set_ylabel("Frequency")
# Plot histogram for Uniform distribution samples
axs[2].hist(uniform_samples, bins=30, color='salmon', edgecolor='black')
axs[2].set_title("Uniform Distribution (Length Tolerance)")
axs[2].set_xlabel("Length (cm)")
axs[2].set_ylabel("Frequency")
plt.tight_layout()
plt.show()
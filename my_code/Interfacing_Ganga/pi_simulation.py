import sys
import random

def monte_carlo_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return (inside_circle / num_samples) * 4  # π approximation

if __name__ == "__main__":
    num_samples = int(sys.argv[1])
    pi_estimate = monte_carlo_pi(num_samples)
    
    # Print result to stdout (Ganga will capture this)
    print(pi_estimate)

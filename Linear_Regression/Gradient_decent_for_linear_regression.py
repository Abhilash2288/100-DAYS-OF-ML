#imports
import numpy as np
import matplotlib.pyplot as pt

X = np.array([1, 2, 3, 4, 5])  # Input features
y = np.array([2, 4, 6, 8, 10])  # Target values

m = 0  # Slope
b = 0  # Intercept
learning_rate = 0.01  # Learning rate
iterations = 10000 # Number of iterations

for _ in range(iterations):
    y_pred = m * X + b
    dm = (-2 / len(X)) * np.sum(X * (y - y_pred))
    db = (-2 / len(X)) * np.sum(y - y_pred)
    
    m -= learning_rate * dm
    b -= learning_rate * db

print("Slope (m):", m)
print("Intercept (b):", b)


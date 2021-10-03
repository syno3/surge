# we test out the neural network
import sys
sys.path.append("..") # for relative imports

from neuralnet import *
import numpy as np
import matplotlib.pyplot as plt

# input and desired output
X = np.reshape([[0, 0], [0, 1], [1, 0], [1, 1]], (4,2,1))
Y = np.reshape([[0], [1], [1], [0]], (4, 1, 1))
# create the network and use the tanget activator after every activator
network = [
    denseLayer(2, 3),
    tanh(),
    denseLayer(3, 1),
    tanh()
]

#loop
epochs = 1000
learning_rate = 0.1

for e in range(epochs):
    error = 0

    for x, y in zip(X, Y):
        # foward
        output = x
        for layer in network:
            output = layer.foward(output)

        error += mse(y, output)
        # BACKPROP
        grad = mse_prime(y, output)
        for layer in reversed(network):
            grad = layer.backward(grad, learning_rate)

    error /= len(X)
    print(f"epoch {e+1} error {error} answer {y} predicted{output}")




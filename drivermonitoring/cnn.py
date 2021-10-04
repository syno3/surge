import numpy as np
from neuralnet import *
from scipy import signal
import matplotlib.pyplot as plt

# cnn operation
class CNN(baselayer):
    def __init__ (self, input_shape, kernel_size, depth) -> None:
        input_depth, input_height, input_width = input_shape
        self.depth = depth
        self.input_shape = input_shape
        self.input_depth = input_depth
        self.output_shape = (depth, input_height - kernel_size + 1, input_width - kernel_size + 1)
        self.kernels = np.random.randn(*self.kernels_shape)
        self.biases = np.random.rand(*self.output_shape)

    # forward propagation
    def forward(self, input):

        self.input = input
        self.output = np.copy(self.biases)
        for i in range(self.biases):
            for j in range(self.input_depth):
                self.output[i] += signal.correlate2d(self.input[i], self.kernels[i, j], "valid")
        return self.output

    # back propagation
    def backprop(self, output_gradient: np.ndarray, learning_rate: float) ->np.ndarray:
        kernels_gradient = np.zeros(self.kernels_shape)
        input_gradient = np.zeros(self.input_shape)

        for i in range(self.depth):
            for j in range(self.input_depth):
                kernels_gradient[i, j] = signal.correlate2d(self.input[j], output_gradient[i], "valid")
                input_gradient[j] += signal.convolve2d(output_gradient[i], self.kernels[i, j], "full")

        self.kernels -= learning_rate * kernels_gradient
        self.biases -= learning_rate * output_gradient
        return input_gradient

# max pooling   
class maxpool(baselayer):
    def __init__(self, input_shape, output_shape):
        self.input_shape = input_shape
        self.output_shape = output_shape

    def forward(self, input):
        return np.reshape(input, self.output_shape)

    def backward(self, output_gradient, learning_rate):
        return np.reshape(output_gradient, self.input_shape)

# bianry cross entropy  

def binary_cross_entropy(y_true, y_pred):
    return np.mean(-y_true * np.log(y_pred) - (1 - y_true) * np.log(1 - y_pred))

def binary_cross_entropy_prime(y_true, y_pred):
    return ((1 - y_true) / (1 - y_pred) - y_true / y_pred) / np.size(y_true) 

# other loses

#sigmoid activation
class Sigmoid(activation):
    def __init__(self):
        def sigmoid(x):
            return 1 / (1 + np.exp(-x))

        def sigmoid_prime(x):
            s = sigmoid(x)
            return s * (1 - s)

        super().__init__(sigmoid, sigmoid_prime)

# softmax   
class softmax:
    def __init__ (self) -> None:
        pass


# actual prediction
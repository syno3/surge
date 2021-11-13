# we build cnn from scratch
# we predict driver attention status
import numpy as np

# this is base layer
class baselayer:
    def __init__(self) ->None:
        self.input = None
        self.output = None

    def forwardd(self, input: np.ndarray):
        # this takes in input and give the output
        pass

    def backward(self, output_gradient, learning_rate):
        # takes in the derivative of error of output
        # update the trainable parameter
        # return th derivative of error of input
        pass

# this is the dense layer
class denseLayer(baselayer):
    def __init__(self, input_size: int, output_size: int) -> None:
        # we check for zero inputs
        assert input_size, output_size != 0
        self.weights = np.random.randn(output_size, input_size) # W = J.I
        self.bias = np.random.randn(output_size, 1) # B = J.1

    def forward(self, input: np.ndarray) -> np.ndarray:
        self.input = input
        return np.dot(self.weights, self.input) + self.bias # Y = W.X+B

    def backward(self, output_gradient: np.ndarray, learning_rate: np.ndarray) -> np.ndarray:

        weight_gradient =np.dot(output_gradient, self.input.T) #
        self.weights -= learning_rate * weight_gradient
        self.bias -= learning_rate * output_gradient
        return np.dot(self.weights.T, output_gradient) # input gradient


# this is the activation functions
class activation(baselayer):
    def __init__(self, activation, activation_prime) -> None:
        self.activation = activation
        self.activation_prime = activation_prime

    def forward(self, input: np.ndarray):
        self.input = input
        return self.activation(self.input)

    def backward(self, output_gradient, learning_rate):
        return np.multiply(output_gradient, self.activation_prime(self.input))

# hyperbolic tangent activation

class tanh(activation):
    def __init__(self) -> None:
        tanh = lambda x: np.tanh(x)
        tanh_prime = lambda x: 1-np.tanh(x)**2
        super().__init__(tanh, tanh_prime)

# MSE LOSS
def mse(y_true, y_pred):
    return np.mean(np.power(y_true - y_pred, 2))

def mse_prime(y_true, y_pred):
    return 2 * (y_pred - y_true) / np.size(y_true)

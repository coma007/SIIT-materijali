from __future__ import print_function

from abc import abstractmethod
import math
import random
import copy
import numpy as np

from matplotlib import pyplot


class ComputationalNode(object):

    @abstractmethod
    def forward(self, x):  # x is an array of scalars
        pass

    @abstractmethod
    def backward(self, dz):  # dz is a scalar
        pass


class MultiplyNode(ComputationalNode):

    def __init__(self):
        self.x = [0., 0.]  # x[0] is input, x[1] is weight

    def forward(self, x):
        self.x = x
        return self.x[0] * self.x[1]

    def backward(self, dz):
        return [dz * self.x[1], dz * self.x[0]]


class SumNode(ComputationalNode):

    def __init__(self):
        self.x = []  # x is in an array of inputs

    def forward(self, x):
        self.x = x
        return sum(self.x)

    def backward(self, dz):
        return [dz for xx in self.x]


class SigmoidNode(ComputationalNode):

    def __init__(self):
        self.x = 0.  # x is an input

    def forward(self, x):
        self.x = x
        return self._sigmoid(self.x)

    def backward(self, dz):
        return dz * self._sigmoid(self.x) * (1. - self._sigmoid(self.x))

    def _sigmoid(self, x):
        return 1. / (1. + np.exp(-x))


class ReluNode(ComputationalNode):

    def __init__(self):
        self.x = 0.  # x is an input

    def forward(self, x):
        self.x = x
        return self._relu(self.x)

    def backward(self, dz):
        return dz * (1. if self.x > 0. else 0.)

    def _relu(self, x):
        return max(0., x)
    
class LinearNode(ComputationalNode):

    def __init__(self):
        self.x = 0.  # x is an input

    def forward(self, x):
        self.x = x
        return self.x

    def backward(self, dz):
        return dz




class NeuronNode(ComputationalNode):

    def __init__(self, n_inputs, activation):
        self.n_inputs = n_inputs
        self.multiply_nodes = []  # for inputs and weights
        self.sum_node = SumNode()  # for sum of inputs*weights

        for n in range(n_inputs):  # collect inputs and corresponding weights
            mn = MultiplyNode()
            mn.x = [1., random.gauss(0., 0.1)]  # init input weights
            self.multiply_nodes.append(mn)

        mn = MultiplyNode()  # init bias node
        mn.x = [1., random.gauss(0., 0.01)]  # init bias weight
        self.multiply_nodes.append(mn)

        if activation == 'sigmoid':
            self.activation_node = SigmoidNode()
        elif activation == 'relu':
            self.activation_node = ReluNode()
        elif activation == 'linear':
            self.activation_node = LinearNode()
        else:
            raise RuntimeError('Unknown activation function "{0}".'.format(activation))

        self.previous_deltas = [0.] * (self.n_inputs + 1)
        self.gradients = []

    def forward(self, x):  # x is a vector of inputs
        x = np.append(np.copy(x), 1.)
        # x = copy.copy(x)
        # x.append(1.)  # for bias
        for_sum = []
        for i, xx in enumerate(x):
            inp = [x[i], self.multiply_nodes[i].x[1]]
            for_sum.append(self.multiply_nodes[i].forward(inp))

        summed = self.sum_node.forward(for_sum)
        summed_act = self.activation_node.forward(summed)
        return summed_act

    def backward(self, dz):
        dw = []
        b = dz[0] if type(dz[0]) == float else sum(dz)
        b = self.activation_node.backward(b)
        b = self.sum_node.backward(b)
        for i, bb in enumerate(b):
            dw.append(self.multiply_nodes[i].backward(bb)[1])

        self.gradients.append(dw)
        return dw

    def update_weights(self, learning_rate, momentum):
        for i, multiply_node in enumerate(self.multiply_nodes):
            mean_gradient = sum([grad[i] for grad in self.gradients]) / len(self.gradients)
            delta = learning_rate*mean_gradient + momentum*self.previous_deltas[i]
            self.previous_deltas[i] = delta
            self.multiply_nodes[i].x[1] -= delta

        self.gradients = []


class NeuralLayer(ComputationalNode):

    def __init__(self, n_inputs, n_neurons, activation):
        self.n_inputs = n_inputs
        self.n_neurons = n_neurons
        self.activation = activation

        self.neurons = []
        # construct layer
        for _ in range(n_neurons):
            neuron = NeuronNode(n_inputs, activation)
            self.neurons.append(neuron)

    def forward(self, x):  # x is a vector of "n_inputs" elements
        layer_output = []
        for neuron in self.neurons:
            neuron_output = neuron.forward(x)
            layer_output.append(neuron_output)

        return layer_output

    def backward(self, dz):  # dz is a vector of "n_neurons" elements
        b = []
        for idx, neuron in enumerate(self.neurons):
            neuron_dz = [d[idx] for d in dz]
            neuron_dz = neuron.backward(neuron_dz)
            b.append(neuron_dz[:-1])

        return b  # b is a vector of "n_neurons" elements

    def update_weights(self, learning_rate, momentum):
        for neuron in self.neurons:
            neuron.update_weights(learning_rate, momentum)


class NeuralNetwork(ComputationalNode):

    def __init__(self):
        # construct neural network
        self.layers = []
        random.seed(42)

    def add(self, layer):
        self.layers.append(layer)

    def forward(self, x):  # x is a vector which is an input for neural net
        prev_layer_output = None
        for idx, layer in enumerate(self.layers):
            if idx == 0:  # input layer
                prev_layer_output = layer.forward(x)
            else:
                prev_layer_output = layer.forward(prev_layer_output)

        return prev_layer_output  # actually an output from last layer

    def backward(self, dz):
        next_layer_dz = None
        for idx, layer in enumerate(self.layers[::-1]):
            if idx == 0:
                next_layer_dz = layer.backward(dz)
            else:
                next_layer_dz = layer.backward(next_layer_dz)

        return next_layer_dz

    def update_weights(self, learning_rate, momentum):
        for layer in self.layers:
            layer.update_weights(learning_rate, momentum)

    def fit(self, X, Y, learning_rate, momentum, nb_epochs, shuffle=False, verbose=0):
        assert len(X) == len(Y)

        hist = []
        for epoch in range(nb_epochs):
            if shuffle:
                random.seed(epoch)
                random.shuffle(X)
                random.seed(epoch)
                random.shuffle(Y)

            total_loss = 0.0
            for x, y in zip(X, Y):
                # forward pass to compute output
                pred = self.forward(x)
                # compute loss
                grad = 0.0
                for o, t in zip(pred, y):
                    total_loss += (t - o) ** 2.
                    grad += -(t - o)
                # backward pass to compute gradients
                self.backward([[grad]])
                # update weights with computed gradients
                self.update_weights(learning_rate, momentum)

            hist.append(total_loss)
            if verbose == 1:
                    print('Epoch {0}: loss {1}'.format(epoch + 1, total_loss))
        print('Loss: {0}'.format(total_loss))
        return hist

    def predict(self, x):
        return self.forward(x)


if __name__ == '__main__':
    nn = NeuralNetwork()
    nn.add(NeuralLayer(2, 2, 'sigmoid'))
    nn.add(NeuralLayer(2, 1, 'sigmoid'))

    # XOR example
    # obucavajuci skup
    X = [[0., 0.],
         [1., 0.],
         [0., 1.],
         [1., 1.]]
    Y = [[0.],
         [1.],
         [1.],
         [0.]]

    # obucavanje neuronske mreze
    history = nn.fit(X, Y, learning_rate=0.1,  momentum=0.3, nb_epochs=10000, shuffle=True, verbose=0)

    # provera da li radi
    print(nn.predict([0., 0.]))
    print(nn.predict([1., 0.]))
    print(nn.predict([0., 1.]))
    print(nn.predict([1., 1.]))

    # plotovanje funkcije greske
    pyplot.plot(history)
    pyplot.show()
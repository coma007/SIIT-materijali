from abc import abstractmethod
import math
import random
import copy

from matplotlib import pyplot


random.seed(1337)


class ComputationalNode(object):

    @abstractmethod
    def forward(self, x):
        pass

    @abstractmethod
    def backward(self, dz):
        pass


class MultiplyNode(ComputationalNode):

    def __init__(self):
        self.x = [0., 0.]  # x[0] je ulaz, x[1] je tezina

    def forward(self, x):
        self.x = x
        # TODO 1: implementirati forward-pass za mnozac
        raise NotImplementedError('TODO 1')
        return None

    def backward(self, dz):
        # TODO 1: implementirati backward-pass za mnozac
        raise NotImplementedError('TODO 1')
        return None


# MultiplyNode tests
mn_test = MultiplyNode()
assert mn_test.forward([2., 3.]) == 6., 'Failed MultiplyNode, forward()'
assert mn_test.backward(-2.) == [-2.*3., -2.*2.], 'Failed MultiplyNode, backward()'
print('MultiplyNode: tests passed')


class SumNode(ComputationalNode):

    def __init__(self):
        self.x = []  # x je vektor, odnosno niz skalara

    def forward(self, x):
        self.x = x
        # TODO 2: implementirati forward-pass za sabirac
        raise NotImplementedError('TODO 2')
        return None

    def backward(self, dz):
        # TODO 2: implementirati backward-pass za sabirac
        raise NotImplementedError('TODO 2')
        return None


# SumNode tests
sn_test = SumNode()
assert sn_test.forward([1., 2., -2, 5.]) == 6., 'Failed SumNode, forward()'
assert sn_test.backward(-2.) == [-2.]*4, 'Failed SumNode, backward()'
print('SumNode: tests passed')


class SigmoidNode(ComputationalNode):

    def __init__(self):
        self.x = 0.  # x je skalar

    def forward(self, x):
        self.x = x
        # TODO 3: implementirati forward-pass za sigmoidalni cvor
        raise NotImplementedError('TODO 3')
        return None

    def backward(self, dz):
        # TODO 3: implementirati backward-pass za sigmoidalni cvor
        raise NotImplementedError('TODO 3')
        return None

    def _sigmoid(self, x):
        # TODO 3: implementirati sigmoidalnu funkciju
        raise NotImplementedError('TODO 3')
        return None


# SigmoidNode tests
sign_test = SigmoidNode()
assert sign_test.forward(1.) == 0.7310585786300049, 'Failed SigmoidNode, forward()'
assert sign_test.backward(-2.) == -2.*0.7310585786300049*(1.-0.7310585786300049), 'Failed SigmoidNode, backward()'
print('SigmoidNode: tests passed')


class NeuronNode(ComputationalNode):

    def __init__(self, n_inputs, activation):
        self.n_inputs = n_inputs  # moramo da znamo kolika ima ulaza da bismo znali koliko nam treba mnozaca
        self.multiply_nodes = []  # lista mnozaca
        self.sum_node = SumNode()  # sabirac

        # TODO 4: napraviti n_inputs mnozaca u listi mnozaca, odnosno mnozac za svaki ulaz i njemu odgovarajucu tezinu
        # za svaki mnozac inicijalizovati tezinu na broj iz normalne (gauss) raspodele sa st. devijacijom 0.1
        raise NotImplementedError('TODO 4')

        # TODO 5: dodati jos jedan mnozac u listi mnozaca, za bias
        # bias ulaz je uvek fiksiran na 1.
        # bias tezinu inicijalizovati na broj iz normalne (gauss) raspodele sa st. devijacijom 0.01
        raise NotImplementedError('TODO 5')

        # TODO 6: ako ulazni parametar funckije 'activation' ima vrednosti 'sigmoid',
        # inicijalizovati da aktivaciona funckija bude sigmoidalni cvor
        self.activation_node = None
        raise NotImplementedError('TODO 6')

        self.gradients = []

    def forward(self, x):  # x je vektor ulaza u neuron, odnosno lista skalara
        x = copy.copy(x)
        x.append(1.)  # uvek implicitino dodajemo bias=1. kao ulaz

        # TODO 7: implementirati forward-pass za vestacki neuron
        # u x se nalaze ulazi i bias neurona
        # iskoristi forward-pass za mnozace, sabirac i aktivacionu funkciju da bi se dobio konacni izlaz iz neurona
        raise NotImplementedError('TODO 7')
        return None

    def backward(self, dz):
        dw = []
        d = dz[0] if type(dz[0]) == float else sum(dz)  # u d se nalazi spoljasnji gradijent izlaza neurona

        # TODO 8: implementirati backward-pass za vestacki neuron
        # iskoristiti backward-pass za aktivacionu funkciju, sabirac i mnozace da bi se dobili gradijenti tezina neurona
        # izracunate gradijente tezina ubaciti u listu dw
        raise NotImplementedError('TODO 8')

        self.gradients = dw
        return dw

    def update_weights(self, learning_rate, momentum):
        # azuriranje tezina vestackog neurona
        # learning_rate je korak gradijenta

        # TODO 11: azurirati tezine neurona (odnosno azurirati drugi parametar svih mnozaca u neuronu)
        # gradijenti tezina se nalaze u list self.gradients
        raise NotImplementedError('TODO 11')

        self.gradients = []  # ciscenje liste gradijenata (da sve bude cisto za sledecu iteraciju)


class NeuralLayer(ComputationalNode):

    def __init__(self, n_inputs, n_neurons, activation):
        self.n_inputs = n_inputs  # broj ulaza u ovaj sloj neurona
        self.n_neurons = n_neurons  # broj neurona u sloju (toliko ce biti i izlaza iz ovog sloja)
        self.activation = activation  # aktivaciona funkcija neurona u ovom sloju

        self.neurons = []
        # konstruisanje sloja nuerona
        for _ in range(n_neurons):
            neuron = NeuronNode(n_inputs, activation)
            self.neurons.append(neuron)

    def forward(self, x):  # x je vektor, odnosno lista "n_inputs" elemenata
        layer_output = []
        # forward-pass za sloj neurona je zapravo forward-pass za svaki neuron u sloju nad zadatim ulazom x
        for neuron in self.neurons:
            neuron_output = neuron.forward(x)
            layer_output.append(neuron_output)

        return layer_output

    def backward(self, dz):  # dz je vektor, odnosno lista "n_neurons" elemenata
        dd = []
        # backward-pass za sloj neurona je zapravo backward-pass za svaki neuron u sloju nad
        # zadatim spoljasnjim gradijentima dz
        for i, neuron in enumerate(self.neurons):
            neuron_dz = [d[i] for d in dz]
            neuron_dz = neuron.backward(neuron_dz)
            dd.append(neuron_dz[:-1])  # izuzimamo gradijent za bias jer se on ne propagira unazad

        return dd

    def update_weights(self, learning_rate, momentum):
        # azuriranje tezina slojeva neurona je azuriranje tezina svakog neurona u tom sloju
        for neuron in self.neurons:
            neuron.update_weights(learning_rate, momentum)


class NeuralNetwork(ComputationalNode):

    def __init__(self):
        self.layers = []  # neuronska mreza se sastoji od slojeva neurona

    def add(self, layer):
        self.layers.append(layer)

    def forward(self, x):  # x je vektor koji predstavlja ulaz u neuronsku mrezu
        # TODO 9: implementirati forward-pass za celu neuronsku mrezu
        # ulaz za prvi sloj neurona je x
        # ulaz za sve ostale slojeve izlaz iz prethodnog sloja
        raise NotImplementedError('TODO 9')
        return None

    def backward(self, dz):
        # TODO 10: implementirati forward-pass za celu neuronsku mrezu
        # spoljasnji gradijent za izlazni sloj neurona je dz
        # spoljasnji gradijenti za ostale slojeve su izracunati gradijenti iz sledeceg sloja
        raise NotImplementedError('TODO 10')
        return None

    def update_weights(self, learning_rate, momentum):
        # azuriranje tezina neuronske mreze je azuriranje tezina slojeva
        for layer in self.layers:
            layer.update_weights(learning_rate, momentum)

    def fit(self, X, Y, learning_rate=0.1, momentum=0.0, nb_epochs=10, shuffle=False, verbose=0):
        assert len(X) == len(Y)

        hist = []  # za plotovanje funkcije greske kroz epohe
        for epoch in range(nb_epochs):

            if shuffle:  # izmesati podatke
                random.seed(epoch)
                random.shuffle(X)
                random.seed(epoch)
                random.shuffle(Y)

            total_loss = 0.0
            for x, y in zip(X, Y):
                y_pred = self.forward(x)  # forward-pass da izracunamo izlaz
                y_target = y  # zeljeni izlaz
                grad = 0.0
                for p, t in zip(y_pred, y_target):
                    total_loss += 0.5 * (t - p) ** 2.  # funkcija greske je kvadratna greska
                    grad += -(t - p)  # gradijent funkcije greske u odnosu na izlaz
                # backward-pass da izracunamo gradijente tezina
                self.backward([[grad]])
                # azuriranje tezina na osnovu izracunatih gradijenata i koraka "learning_rate"
                self.update_weights(learning_rate, momentum)

            if verbose == 1:
                print('Epoch {0}: loss {1}'.format(epoch + 1, total_loss))

            hist.append(total_loss)

        print('Loss: {0}'.format(total_loss))
        return hist

    def predict(self, x):
        return self.forward(x)


if __name__ == '__main__':

    nn = NeuralNetwork()
    # TODO 12: konstruisati neuronsku mrezu za resavanje XOR problema
    raise NotImplementedError('TODO 12')


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
    history = nn.fit(X, Y, learning_rate=0.1, momentum=0.9, nb_epochs=10000, shuffle=True, verbose=0)

    # provera da li radi
    print(nn.predict([0., 0.]))
    print(nn.predict([1., 0.]))
    print(nn.predict([0., 1.]))
    print(nn.predict([1., 1.]))

    # plotovanje funkcije greske
    pyplot.plot(history)
    pyplot.show()

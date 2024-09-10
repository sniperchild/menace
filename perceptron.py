import random
# To Add - argparse

class Neuron:
    '''
    Individual neuron with activatio bis and backprop
    '''
    def __init__(self) -> None:
        # bias
        # weight
        self.bias = random.random()

class Layer:
    def __init__(self,num,size) -> None:
        if num == 0:
            #initial layer - no weights
            self.neurons = [Neuron() for x in size]
            self.input_layer = True
        else:
            self.neurons = [Neuron() for x in size]
            self.input_layer = False


class Perceptron:
    def __init__(self,layers) -> None:
        '''
        layers - list describing the topology of the perceptron
        [x,y,z] = would be a three layer perceptron of sizes x,y,and z
        '''

        # input layer
        # middle layer
        # outer layer
        self.layers = [Layer(num,size) for num,size in enumerate(layers)]



def main():

    # instantiate the structure

    p = Perceptron(9,16,9)



if __name__ == '__main__':
    main()
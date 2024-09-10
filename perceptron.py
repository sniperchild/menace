import random
import numpy as np
# To Add - argparse

class Neuron:
    '''
    Individual neuron with activatio bis and backprop
    '''
    def __init__(self,initial,weight_size) -> None:
        # bias
        # weight
        self.bias = np.random.random()
        self.weights = np.random.random(weight_size)
        self.initial = initial

    def activate(self,inputs):
        print("inputs",inputs)
        if self.initial:
            print("return")
            return inputs
        print("weights",self.weights)
        # multiply weights by inputs and add bias
        output = self.bias + np.dot(self.weights,inputs)
        print(output)
        return output

class Layer:
    def __init__(self,num,size,layers) -> None:
        if num == 0:
            #initial layer - no weights
            self.neurons = [Neuron(True,0) for _ in range(size)]
            self.input_layer = True

        else:
            self.neurons = [Neuron(False,layers[num-1]) for _ in range(size)]
            self.input_layer = False

        self.outputs = np.zeros(size)
        print("init")

    def run(self,inputs):

        self.outputs

        for idx,neuron in enumerate(self.neurons):
            print(idx)
            print(neuron)
            self.outputs[idx] = neuron.activate(inputs)

        return self.outputs


class Perceptron:
    def __init__(self,layers) -> None:
        '''
        layers - list describing the topology of the perceptron
        [x,y,z] = would be a three layer perceptron of sizes x,y,and z
        '''

        # input layer
        # middle layer
        # outer layer
        self.layers = [Layer(num,size,layers) for num,size in enumerate(layers)]


    def run(self,input):
        
        for layer in self.layers:
            input = layer.run(input)

        return input




def main():

    # instantiate the structure

    p = Perceptron([9,16,9])

    #run_the_network

    inputs = [0,0,0,0,0,0,0,0]

    outputs = p.run(inputs)

    print(outputs)


if __name__ == '__main__':
    main()
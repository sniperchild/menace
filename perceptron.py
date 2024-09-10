import random
# To Add - argparse

class Neuron:
    '''
    Individual neuron with activatio bis and backprop
    '''
    def __init__(self,weight_size) -> None:
        # bias
        # weight
        self.bias = random.random()
        self.weights = [random.random() for _ in weight_size]

    def activate(self,inputs):
        # multiply weights by inputs and add bias
        output = self.bias + []

    numpy muliply here

class Layer:
    def __init__(self,num,size) -> None:
        if num == 0:
            #initial layer - no weights
            self.neurons = [Neuron() for _ in size]
            self.input_layer = True
        else:
            self.neurons = [Neuron() for _ in size]
            self.input_layer = False

    def run(self,inputs):

        for neuron in self.neurons:
            output = neuron.activate(inputs)


        return outputs


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


    def run(self,input):
        
        for layer in layers:
            input = layer.run(input)

        return input




def main():

    # instantiate the structure

    p = Perceptron(9,16,9)

    #run_the_network

    inputs = [0,0,0,0,0,0,0,0]

    outputs = p.run(inputs)

    print(outputs)


if __name__ == '__main__':
    main()
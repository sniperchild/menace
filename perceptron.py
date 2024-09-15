import random
import numpy as np
# To Add - argparse

class Neuron:
    '''
    Individual neuron with activatio bis and backprop
    '''
    def __init__(self,initial,idx,weight_size) -> None:
        # bias
        # weight
        self.bias = np.random.random()
        self.weights = np.random.random(weight_size)
        self.initial = initial
        self.idx=idx

    def activate(self,inputs):
        print("inputs",inputs)
        if self.initial:
            print("return")
            return inputs[self.idx]
        print("weights",self.weights)
        # multiply weights by inputs and add bias
        activation = self.bias + np.dot(self.weights,inputs)
        #print(output)
        output = self.transfer(activation)
        self.output = output
        return output
    
    def transfer(self,activation):
        '''
        Implements transfer function
        here a relu
        '''
        activation = max(0,activation)
        return activation
    
    def transfer_derivative(self,val):
        '''
        Derivative of transfer function
        here a relu
        '''
        dv = float(int(val > 0)) # returns 1 when > 0
        return dv
    
    def backprop(self,target):
        '''backpropagate the error'''
        #take the fed back correct solution
        ''' calculate the error '''
        error = (self.output - target) * self.transfer_derivative(self.output)

        ''' generate a new set of inputs based on the weights '''
        errors = [error * weight * self.transfer_derivative(self.output) for weight in self.weights]
        return np.array(errors)




class Layer:
    def __init__(self,num,size,layers) -> None:
        if num == 0:
            #initial layer - no weights
            self.neurons = [Neuron(True,x,0) for x in range(size)]
            self.input_layer = True

        else:
            self.neurons = [Neuron(False,x,layers[num-1]) for x in range(size)]
            self.input_layer = False

        self.outputs = np.zeros(size)
        print("init")

    def run(self,inputs):

        #self.outputs

        for idx,neuron in enumerate(self.neurons):
            print(idx)
            print(neuron)
            print(self.outputs)
            self.outputs[idx] = neuron.activate(inputs)
            print("op")
        return self.outputs

    def learn(self,solution):
        '''
        solution is an array that represents the ideal output of the layer
        '''
        errors = np.zeros(len(self.neurons[0].weights))
        for idx,neuron in enumerate(self.neurons):
            errors += neuron.backprop(solution[idx])
            print("op")
            print(errors)
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
            print("layer")
            input = layer.run(input)

        return input
    
    def learn(self,solution):
        '''
        backpropagate the solution through the network

        
        '''

        #for each neuron in the output layer
        #feed it the value it should have produced

        for layer in reversed(self.layers):
            solution = layer.learn(solution)
            print("learning")


def main():

    # instantiate the structure

    p = Perceptron([9,16,9])

    #run_the_network

    inputs = np.zeros(9)

    outputs = p.run(inputs)

    print(outputs)

    solution = np.array([0,0,0,0,0,0,0,0,1])

    p.learn(solution)


if __name__ == '__main__':
    main()
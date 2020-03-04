from ..Matrix.Matrix import Matrix
import math

class NeuralNet:
    def __init__ (self,*args):
        '''
        Initiate the Neural Network of N layers, each number put in args
        will be converted into a layer, so (1,2,3,4) will create a
        NeuNet of :
           - 1 input neuron
           - 2 neurons hidden first layer
           - 3 neurons hidden second layer
           - 4 output neurons

        Each layer has its own index (from 0 to N - 1)
        The data of the weight, biaises, activation and zed are stored in a
        list of matrices.

        Finally, a set of "nabla" matrices are initate for the propagate
        backward.
        '''

        # here is a list of the number of neuron foreach layer
        self.neuron_number = args
        self.layers_number = len(args)

        # here I create the weight and biases Matrices for each
        # layers and link between them
        # Also randomize them

        self.weights_matrices = []
        self.biaises_matrices = []
        for i in range(self.layers_number - 1):
            # weigths
            tmp_w = Matrix(self.neuron_number[i+1],self.neuron_number[i])
            tmp_w.randomize()
            self.weights_matrices.append(tmp_w)
            # biaises
            tmp_b = Matrix(self.neuron_number[i+1],1)
            tmp_b.randomize()
            self.biaises_matrices.append(tmp_b)

        # initiate the activations (and maybe Z) matrices
        # activations are just Z.map(sigmoid) btw
        self.zed_matrices=[]
        self.activations_matrices=[]

        self.Nabla_weigth_matrices=[]
        self.Nabla_biases_matrices=[]

    def __str__ (self):
        printage=""
        for i in range(self.layers_number - 1):
            printage += "--------"
            printage += "Activation" + str(i) + "\n"
            printage += str(self.activations_matrices[i])
            printage += "Weight\n"
            printage += str(self.weights_matrices[i])
            printage += "biaises\n"
            printage += str(self.biaises_matrices[i])
            printage += "\n"
        printage += "--------"
        printage += "Activation" + str(i) + "\n"
        printage += str(self.activations_matrices[self.layers_number - 1])
        return printage
    # static functions used
    @staticmethod
    def sigmoid (x):
        return math.e**x / ( math.e**x + 1 )

    @staticmethod
    def sigmoidprim (x):
        return math.e**x / ( math.e**x + 1 )**2

    def feed_forward (self,inputs):
        '''
        Caclulate the activations and zed matrices
        and fill the appropriates lists
        Return : None
        '''
        self.activations_matrices.append(inputs)
        self.zed_matrices.append(inputs)
        for i in range(self.layers_number - 1):
            zed_mat = self.weights_matrices[i] * self.activations_matrices[i]
            zed_mat += self.biaises_matrices[i]
            self.zed_matrices.append(zed_mat)
            act_mat = Matrix.map(self.sigmoid,zed_mat)
            self.activations_matrices.append(act_mat)

    def propagate_backward (self,answers):
        '''
        One wave of Nabla calculus by comparing
        it with the answer (Matrix nx1 object with
        n = number of outpus of the network)

        answers need to be a Matrix type (TODO: fromArray in that func?)

        Return :
            - nabla_weights (list of matrices)
            - nabla_biaises (list of matrices)
        '''
        # Nabla_activate calculus will

        # first : outputs, last position in the act_matrices list
        DCa = self.activations_matrices[-1] - answers
        DCa *= 2
        # from the last to the first excluding inputs and outputs
        Nabla_b=[]
        Nabla_w=[]
        for layer in reversed(range(1,self.layers_number)):
            sigpZ = Matrix.map(self.sigmoidprim,self.zed_matrices[layer])
            W = self.weights_matrices[layer - 1]
            DCb = sigpZ * DCa
            DZw = self.activations_matrices[layer - 1]
            DCw = DZw * sigpZ * DCa  # need to check that
            Nabla_b.insert(0, DCb)
            Nabla_w.insert(0, DCw)
            DCa = W * sigpZ * DCa
        return Nabla_b,Nabla_w


'''
act [i,h1,h2,o]
zed [i,h1,h2,o]
wei [ih1,h1h2,h2o]
b [h1,h2,o]
'''

    def train (self,inputs,answers):
        '''
        feed_forward and back_propagade
        '''
        self.feed_forward(inputs)
        nabla_w,nabla_b = self.propagate_backward(answers)
        self.add_to_nablas(nabla_w,nabla_b)

    @staticmethod
    def add_to_nablas(nabla_w,nabla_b):
        print("TODO")

    def adjust(self):
        '''
        Substract the sotre big_nabla_gradient to the
        matrices of weight and biaises
        '''
        print("TODO")

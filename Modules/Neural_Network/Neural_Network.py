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

        # initialize the Nabla_weigth TODO: make it more elegant
        self.Nabla_weigth_matrices=[]
        self.Nabla_biases_matrices=[]
        for i in range(self.layers_number - 1):
            matw = Matrix(self.neuron_number[i+1],self.neuron_number[i])
            matb = Matrix(self.neuron_number[i+1],1)
            self.Nabla_biases_matrices.append(matb)
            self.Nabla_weigth_matrices.append(matw)

    def __str__ (self):
        printage=""
        for i in range(self.layers_number - 1):
            printage += "--------\n"
            printage += "Activation" + str(i) + "\n"
            printage += str(self.activations_matrices[i])
            printage += "Weight\n"
            printage += str(self.weights_matrices[i])
            printage += "biaises\n"
            printage += str(self.biaises_matrices[i])
            printage += "\n"
        printage += "--------\n"
        printage += "Activation" + str(i) + "\n"
        printage += str(self.activations_matrices[self.layers_number - 1])
        printage += "--------\n"
        printage += "Nabla biases matrices:\n"
        for mat in self.Nabla_biases_matrices:
            printage += str(mat)
        printage += "--------\n"
        printage += "Nabla wieght matrices:\n"
        for mat in self.Nabla_weigth_matrices:
            printage += str(mat)
        return printage
    # static functions used
    @staticmethod
    def sigmoid (x):
        return math.e**x / ( math.e**x + 1 )

    @staticmethod
    def sigmoidprim (x):
        return math.e**x / ( math.e**x + 1 )**2

    def feed_forward (self,inputs_arr):
        '''
        Caclulate the activations and zed matrices
        and fill the appropriates lists
        Return : None
        '''
        inputs = Matrix.fromArray(inputs_arr)

        self.activations_matrices = []
        self.zed_matrices = []
        self.activations_matrices = [inputs]
        self.zed_matrices = [inputs]
        for i in range(self.layers_number - 1):
            zed_mat = self.weights_matrices[i] * self.activations_matrices[i]
            zed_mat += self.biaises_matrices[i]
            self.zed_matrices.append(zed_mat)
            act_mat = Matrix.map(self.sigmoid,zed_mat)
            self.activations_matrices.append(act_mat)

    def backpropagation (self,answers_arr):
        '''
        One wave of Nabla calculus by comparing
        it with the answer (Matrix nx1 object with
        n = number of outpus of the network)

        answers need to be a Matrix type (TODO: fromArray in that func?)

        Return :
            - nabla_weights (list of matrices)
            - nabla_biaises (list of matrices)
        '''
        answers = Matrix.fromArray(answers_arr)

        Nabla_b=[]
        Nabla_w=[]

        # first : outputs, last position in the act_matrices list
        DCaL = self.activations_matrices[-1] - answers
        sigpZ = Matrix.map(self.sigmoidprim,self.zed_matrices[-1])
        error = Matrix.had_prod(DCaL,sigpZ)
        # from the last to the first excluding inputs and outputs
        for layer in reversed(range(1,self.layers_number)):
            # error on biaises
            dCb = error
            Nabla_b.insert(0,dCb)
            # weight
            ac = self.activations_matrices[layer - 1]
            dCw = Matrix(error.rows,ac.rows)
            for j in range(dCw.rows):
                for k in range(dCw.columns):
                    lej = error.data[j][0]
                    ack = ac.data[k][0]
                    dCw.data[j][k] = ack * lej
            Nabla_w.insert(0,dCw)
            # new local error
            mat_mul = self.weights_matrices[layer - 1].transpose() * error
            sigpZ = Matrix.map(self.sigmoidprim,self.zed_matrices[layer - 1])
            error = Matrix.had_prod(mat_mul,sigpZ)
        return Nabla_w,Nabla_b

    def train (self,inputs_arr,answers_arr):
        '''
        feed_forward and back_propagade n times
        '''
        self.feed_forward(inputs_arr)
        nabla_w,nabla_b = self.backpropagation(answers_arr)
        for i in range(self.layers_number - 1):
            self.Nabla_weigth_matrices[i] += nabla_w[i]
            self.Nabla_biases_matrices[i] += nabla_b[i]

    def adjust(self,lr):
        '''
        Substract the sotre big_nabla_gradient to the
        matrices of weight and biaises
        Get learning rate
        '''
        for i in range(self.layers_number - 1):
            self.weights_matrices[i] -= self.Nabla_weigth_matrices[i] * lr
            self.biaises_matrices[i] -= self.Nabla_biases_matrices[i] * lr
            self.Nabla_weigth_matrices[i] *= 0 # reinitialize Nabla
            self.Nabla_biases_matrices[i] *= 0 # reinitialize Nabla

    def output(self,inputs_arr):
        self.feed_forward(inputs_arr)
        return self.activations_matrices[-1]

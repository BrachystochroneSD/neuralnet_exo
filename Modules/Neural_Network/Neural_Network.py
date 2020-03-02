from ..Matrix.Matrix import Matrix
import math

class NeuralNet:
    def __init__(self,inum,hnum,onum):
        # Initiate the Neural Network (3 layers) with the number of neuron in
        # inputs, hidden and outputs layer
        self.inum=inum
        self.hnum=hnum
        self.onum=onum

        self.wih=Matrix(self.hnum,self.inum)
        self.bh=Matrix(self.hnum,1)
        self.wih.randomize()
        self.bh.randomize()

        self.who=Matrix(self.onum,self.hnum)
        self.bo=Matrix(self.onum,1)
        self.who.randomize()
        self.bo.randomize()

        self.outputs=Matrix(self.onum,1)
        self.zi = []
        self.dCa = []
        self.dCw = []
        self.dCb = []

    # functions used

    @staticmethod
    def sigmoid(x):
        return math.e**x / ( math.e**x + 1 )

    @staticmethod
    def sigmoidprim(x):
        return math.e**x / ( math.e**x + 1 )**2

    # Training related:

    def backprop(self,guess):
        # step 1: calculate errors dCa
        for i in range(self.onum):
            self.dCa[i] = 2 * (self.outputs.data[i][0] - guess[i]) # will only be used during one step
        # step 2: calculate dCb
        for i in range(self.onum):
            zi = "TODO" # matrix.multipley self.who,hiddens et add bo (already done in the feed forward )
            self.dCb[i] += self.sigmoidprim(zi[i]) * dCa[i] # add up to it, because each session of training will change it
        # step 3: calculate dCw hardest TODO

    def feed_forward(self,inputs):
        hiddens = Matrix.multiply(self.wih,inputs)
        hiddens.add(self.bh)
        hiddens.map(self.sigmoid)
        outputs = Matrix.multiply(self.who,hiddens)
        outputs.add(self.bo)
        outputs.map(self.sigmoid)
        return outputs

    def train(self,inputs,answer):
        print("TODO")

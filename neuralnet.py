from Modules.Neural_Network.Neural_Network import NeuralNet
from Modules.Matrix.Matrix import Matrix
import random

nn=NeuralNet(2,2,1)

ia = [([1,1], [0]),
      ([0,1], [1]),
      ([1,0], [1]),
      ([0,0], [0])]

# Just a xor test
for i in range(20000):
    index = random.randint(0,len(ia)-1)
    i,a = ia[index]
    nn.train(i,a)
    nn.adjust(1)

print(nn.output([1,1]))
print(nn.output([0,0]))
print(nn.output([1,0]))
print(nn.output([0,1]))

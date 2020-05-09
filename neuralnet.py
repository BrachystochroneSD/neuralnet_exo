from Modules.Neural_Network.Neural_Network import NeuralNet
from Modules.Matrix.Matrix import Matrix
import random

nn=NeuralNet(2,10,10,1)

ia = [([1,1], [0]),
      ([0,1], [1]),
      ([1,0], [1]),
      ([0,0], [0])]

# Just a xor test
for i in range(10000):
    index = random.randint(0,len(ia)-1)
    inp,ans = ia[index]
    nn.train(inp,ans)
    if (i % 10) == 0:
        nn.adjust(1)

print(nn.output([1,1]))
print(nn.output([0,0]))
print(nn.output([1,0]))
print(nn.output([0,1]))

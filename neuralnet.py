from Modules.Neural_Network.Neural_Network import NeuralNet
from Modules.Matrix.Matrix import Matrix

nn=NeuralNet(2,3,3,1)

inputs=Matrix.fromArray([1,2])
nn.feed_forward(inputs)

print(nn)

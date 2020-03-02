from Modules.Neural_Network.Neural_Network import NeuralNet
from Modules.Matrix.Matrix import Matrix

nn=NeuralNet(2,2,1)

inputs=Matrix.fromArray([1,2])

output=nn.feed_forward(inputs)

print(output.toArray())

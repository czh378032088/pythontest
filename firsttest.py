import numpy as np
import matplotlib.pyplot as plt


from normalizationclass import NormalizationClass
from pybrain.structure import *
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer


def generate_data():
    """generate original data of u and y"""
    u1 = np.random.uniform(0,5,200)
    u2 = np.random.uniform(0,10,200)
    y = u1 * u2 + u1 + u2
    return u1,u2,y


# obtain the original data
u1,u2,y = generate_data()

normu = NormalizationClass()
normy = NormalizationClass()

u1 = normu.norma(u1)
u2 = normu.norma(u2)
y = normy.norma(y)
# createa neural network
fnn = FeedForwardNetwork()

# create three layers, input layer:2 input unit; hidden layer: 10 units; output layer: 1 output
inLayer = LinearLayer(2, name='inLayer')
hiddenLayer0 = SigmoidLayer(10, name='hiddenLayer0')
outLayer = LinearLayer(1, name='outLayer')

# add three layers to the neural network
fnn.addInputModule(inLayer)
fnn.addModule(hiddenLayer0)
fnn.addOutputModule(outLayer)

# link three layers
in_to_hidden0 = FullConnection(inLayer,hiddenLayer0)
hidden0_to_out = FullConnection(hiddenLayer0, outLayer)

# add the links to neural network
fnn.addConnection(in_to_hidden0)
fnn.addConnection(hidden0_to_out)

# make neural network come into effect
fnn.sortModules()

# definite the dataset as two input , one output
DS = SupervisedDataSet(2,1)

# add data element to the dataset
for i in np.arange(199):
    DS.addSample([u1[i],u2[i]],[y[i]])

# you can get your input/output this way
X = DS['input']
Y = DS['target']

# split the dataset into train dataset and test dataset
dataTrain, dataTest = DS.splitWithProportion(0.8)
xTrain, yTrain = DS['input'],DS['target']
xTest, yTest = dataTest['input'], dataTest['target']

# train the NN
# we use BP Algorithm
# verbose = True means print th total error
trainer = BackpropTrainer(fnn, dataTrain, verbose=True,learningrate=0.1)
# set the epoch times to make the NN  fit
trainer.trainUntilConvergence(maxEpochs=100)

# prediction = fnn.activate(xTest[1])
# print("the prediction number is :",prediction," the real number is:  ",yTest[1])
predict_resutl=[]
for i in np.arange(len(xTest)):
    predict_resutl.append(fnn.activate(xTest[i])[0])
print(predict_resutl)
yTest = normy.recvalue111(yTest)
predict_resutl = normy.recvalue111(predict_resutl)

plt.figure()
plt.plot(np.arange(0,len(xTest)), predict_resutl, 'ro--', label='predict number')
plt.plot(np.arange(0,len(xTest)), yTest, 'ko-', label='true number')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")

plt.show()

for mod in fnn.modules:
  print ("Module:", mod.name)
  if mod.paramdim > 0:
    print ("--parameters:", mod.params)
  for conn in fnn.connections[mod]:
    print ("-connection to", conn.outmod.name)
    if conn.paramdim > 0:
       print ("- parameters", conn.params)
  if hasattr(fnn, "recurrentConns"):
    print ("Recurrent connections")
    for conn in fnn.recurrentConns:
       print ("-", conn.inmod.name, " to", conn.outmod.name)
       if conn.paramdim > 0:
          print ("- parameters", conn.params)
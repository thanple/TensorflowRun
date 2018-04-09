from machinelearninginaction.Ch02 import kNN

group,labels = kNN.createDataSet()
print group,labels

minVals = group.min(0)
print minVals

result0 = kNN.classify0([0,0],group , labels, 3)
print result0

#handwritingClassTest
kNN.handwritingClassTest()


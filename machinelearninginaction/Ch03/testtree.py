import machinelearninginaction.Ch03.trees as trees
from machinelearninginaction.Ch03.treePlotter import createPlot, retrieveTree

dataSet,labels = trees.createDataSet()

#print trees.splitDataSet(dataSet, 0, 1)

#print trees.chooseBestFeatureToSplit(dataSet)

#resTree = trees.createTree(dataSet,labels)
#createPlot(resTree)

mytree = retrieveTree(0)
print trees.classify(mytree,labels,[1,0])
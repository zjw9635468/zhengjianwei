from dataprocessing import get_data
from sklearn.linear_model import SGDClassifier
from time import time
from sklearn.externals import joblib
import os
from sklearn import tree
from sklearn.neighbors.nearest_centroid import NearestCentroid
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB


trainX,trainY,testX,testY,validX,validY=get_data()

print len(trainX),len(trainY),len(testX),len(testY),len(validX),len(validY)

X = trainX
Y = trainY
clfSGD = SGDClassifier(loss="hinge", penalty="l2",n_iter=10)
if not os.path.isfile('sklearnModelSGD.pkl'):
    clfSGD.fit(X, Y)
else:
    clfSGD=joblib.load('sklearnModelSGD.pkl')
if not os.path.isfile('sklearnModelSGD.pkl'):
    joblib.dump(clfSGD, 'sklearnModelSGD.pkl')
XSGD=clfSGD.predict(validX)


clfDT = tree.DecisionTreeClassifier()
if not os.path.isfile('sklearnModelDT.pkl'):
    clfDT.fit(X, Y)
else:
    clfDT=joblib.load('sklearnModelDT.pkl')
if not os.path.isfile('sklearnModelDT.pkl'):
    joblib.dump(clfDT, 'sklearnModelDT.pkl')
XDT=clfDT.predict(validX)

clfNCC = NearestCentroid()
if not os.path.isfile('sklearnModelNCC.pkl'):
    clfNCC.fit(X, Y)
else:
    clfNCC=joblib.load('sklearnModelNCC.pkl')
if not os.path.isfile('sklearnModelNCC.pkl'):
    joblib.dump(clfNCC, 'sklearnModelNCC.pkl')
XNCC=clfNCC.predict(validX)

clfNTC = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(13, 5),
                    random_state=1,max_iter=100,
                    early_stopping=True,verbose=True)
if not os.path.isfile('sklearnModelNTC.pkl'):
    clfNTC.fit(X, Y)
else:
    clfNTC=joblib.load('sklearnModelNTC.pkl')
if not os.path.isfile('sklearnModelNTC.pkl'):
    joblib.dump(clfNTC, 'sklearnModelNTC.pkl')
XNTC=clfNTC.predict(validX)

clfGMB=GaussianNB()
if not os.path.isfile('sklearnModelGMB.pkl'):
    clfGMB.fit(X, Y)
else:
    clfGMB=joblib.load('sklearnModelGMB.pkl')
if not os.path.isfile('sklearnModelGMB.pkl'):
    joblib.dump(clfGMB, 'sklearnModelGMB.pkl')
XGMB=clfGMB.predict(validX)

def get_accuracy(validX,validY,x):

    correct=0
    length=len(validX)
    for n in range(length):
        if x[n]==validY[n] :
            correct=correct+1
    percent=correct/1.0/length
    return percent


percentSGD=get_accuracy(validX,validY,XSGD)
percentNCC=get_accuracy(validX,validY,XNCC)
percentNTC=get_accuracy(validX,validY,XNTC)
percentDT=get_accuracy(validX,validY,XDT)
percentGMB=get_accuracy(validX,validY,XGMB)

print percentSGD
print percentNCC
print percentNTC
print percentDT
print percentGMB



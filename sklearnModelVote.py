from sklearn.externals import joblib
from dataprocessing import get_data
from sklearnModel import get_accuracy


trainX,trainY,testX,testY,validX,validY=get_data()

clfSGD=joblib.load('sklearnModelSGD.pkl')
XSGD=clfSGD.predict(testX)

clfDT=joblib.load('sklearnModelDT.pkl')
XDT=clfDT.predict(testX)

clfNCC=joblib.load('sklearnModelNCC.pkl')
XNCC=clfNCC.predict(testX)

clfNTC=joblib.load('sklearnModelNTC.pkl')
XNTC=clfNTC.predict(testX)

clfGMB=joblib.load('sklearnModelGMB.pkl')
XGMB=clfGMB.predict(testX)

def voteIt(XSGD,XDT,XNCC,XNTC,XGMB):
    predict_result=[]
    for a,b,c,d,e in zip(XSGD,XDT,XNCC,XNTC,XGMB):
        sing=0
        if a=='sing':
            sing=sing+1
            if b=='sing':
                sing=sing+1
                if c=='sing':
                    sing=sing+1
                    if d=='sing':
                        sing=sing+1
                        if e=='sing':
                            sing=sing+1
        if sing>2:
            result='sing'
        else:
            result='nosing'
        predict_result.append(result)
    return predict_result


    print len(testY)
    print len(predict_result)
    final_percent=get_accuracy(testX,testY,predict_result)
    print final_percent

predict_list=[]
test_list=[]
def change_list(predict_list,XNTC):
    for a in range(0,len(XNTC),100):
        List=list(XNTC[a:a+100])
        singnumber=List.count('sing')
        if singnumber>=50:
            list_result='sing'
        else:
            list_result='nosing'
        predict_list.append(list_result)
    return predict_list
predictNTC=change_list(predict_list,XNTC)
test_Y=change_list(test_list,testY)
final_percent_change=get_accuracy(test_Y,test_Y,predictNTC)
print final_percent_change
print predictNTC
print test_Y


import os
from baseZhang import wavread, calcMFCC
from sklearn.externals import joblib
from sklearnModelVote import voteIt
from sklearnModel import get_accuracy

wav_dir='/Users/mac/Downloads/jamendo/wav/'
def extract_feature(wav_path):
    if 'train' in wav_path:
        lab_path=wav_path.replace('wav/train','jamendo_lab')[:-3]+'lab'
    elif 'test' in wav_path:
        lab_path=wav_path.replace('wav/test','jamendo_lab')[:-3]+'lab'
    elif 'valid' in wav_path:
        lab_path=wav_path.replace('wav/valid','jamendo_lab')[:-3]+'lab'
    else:
        lab_path='null'
    label_file=open(lab_path,'r')
    labels=label_file.readlines()
    label_file.close()
    audioData,fs=wavread(wav_path)

    predict_song_label=[]
    song_label_Y=[]
    for item_label in labels:
        startTime,endTime,labelY=item_label.split(' ')
        startTime=float(startTime)
        endTime=float(endTime)
        labelY=labelY[:-1]
        audio_part_data=audioData[int(startTime*fs):int(endTime*fs)]
        mfcc=calcMFCC(audio_part_data,fs)
        song_label_Y.append(labelY)
        song_mfcc_X = []
        for mfcc_item in mfcc:
            song_mfcc_X.append(mfcc_item)
        clfSGD = joblib.load('sklearnModelSGD.pkl')
        XSGD = clfSGD.predict(song_mfcc_X)
        clfDT = joblib.load('sklearnModelDT.pkl')
        XDT = clfDT.predict(song_mfcc_X)

        clfNCC = joblib.load('sklearnModelNCC.pkl')
        XNCC = clfNCC.predict(song_mfcc_X)

        clfNTC = joblib.load('sklearnModelNTC.pkl')
        XNTC = clfNTC.predict(song_mfcc_X)

        clfGMB = joblib.load('sklearnModelGMB.pkl')
        XGMB = clfGMB.predict(song_mfcc_X)
        predict_result_X=[]
        for a, b, c, d, e in zip(XSGD, XDT, XNCC, XNTC, XGMB):
            sing = 0
            if a == 'sing':
                sing = sing + 1
                if b == 'sing':
                    sing = sing + 1
                    if c == 'sing':
                        sing = sing + 1
                        if d == 'sing':
                            sing = sing + 1
                            if e == 'sing':
                                sing = sing + 1
            if sing > 2:
                result = 'sing'
            else:
                result = 'nosing'
            predict_result_X.append(result)
            if predict_result_X.count('sing') > predict_result_X.count('nosing'):
                segmentLabel = 'sing'
            else:
                segmentLabel = 'nosing'
        predict_song_label.append(segmentLabel)
    return predict_song_label,song_label_Y
wav_path='/Users/mac/Downloads/jamendo/wav/train/01 - 01 Les Jardins Japonais.wav'

def batch_svd(dataset_dir='/Users/mac/Downloads/jamendo/wav/test/'):
    all_pre_seg = []
    all_tru_seg = []
    for root, dirs, filenames in os.walk(dataset_dir):
        for audioFile in filenames:
            audio_path = os.path.join(root, audioFile)
            if '.wav' in audio_path:
                pre, tru = extract_feature(audio_path)
                all_pre_seg.extend(pre)
                all_tru_seg.extend(tru)
    print get_accuracy(all_tru_seg, all_tru_seg,all_pre_seg)

    return 0
batch_svd()

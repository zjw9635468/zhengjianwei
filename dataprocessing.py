import numpy as np
from baseZhang import wavread, calcMFCC
from pydub import AudioSegment
import os
from baseZhang import if_no_create_it
import h5py

data_dir='/Users/mac/Downloads/jamendo/'
lab_dir=data_dir+'jamendo_lab/'

def trans_audio_to_wav(audio_path):
    audio_format=audio_path.split('.')[-1]
    song=AudioSegment.from_file(audio_path,audio_format)
    song=song.set_channels(1)
    out_path=audio_path.replace('/jamendo/','/jamendo/wav/')
    out_path=out_path.replace(audio_format,'wav')
    if_no_create_it(out_path)
    song.export(out_path,'wav')
    return 0

def batach_to_wav(data_dir):
    for root,dirs,filenames in os.walk(data_dir):
        for audioFile in filenames:
            audio_path=os.path.join(root,audioFile)
            if '.ogg' in audio_path or '.mp3' in audio_path:
                trans_audio_to_wav(audio_path)
                print audio_path
    return 0
# batach_to_wav(data_dir)

wav_dir=data_dir+'wav/'
def extract_feature(wav_path):
    if 'train' in wav_path:
        lab_path=wav_path.replace('wav/train','jamendo_lab')[:-3]+'lab'
    elif 'test' in wav_path:
        lab_path=wav_path.replace('wav/test','jamendo_lab')[:-3]+'lab'
    elif 'valid' in wav_path:
        lab_path=wav_path.replace('wav/valid','jamendo_lab')[:-3]+'lab'
    label_file=open(lab_path,'r')
    labels=label_file.readlines()
    label_file.close()
    audioData,fs=wavread(wav_path)
    song_mfcc_X=[]
    song_label_Y=[]
    for item_label in labels:
        startTime,endTime,labelY=item_label.split(' ')
        startTime=float(startTime)
        endTime=float(endTime)
        labelY=labelY[:-1]
        audio_part_data=audioData[int(startTime*fs):int(endTime*fs)]
        mfcc=calcMFCC(audio_part_data,fs)
        for mfcc_item in mfcc:
            song_mfcc_X.append(mfcc_item)
            song_label_Y.append(labelY)
    return song_mfcc_X,song_label_Y

def batach_feature(wav_dir):
    datasetX=[]
    datesetY=[]
    for root,dirs,filenames in os.walk(wav_dir):
        for audioFile in filenames:
            audio_path=os.path.join(root,audioFile)
            if '.wav' in audio_path:
                song_mfcc_X,song_label_Y=extract_feature(audio_path)
                datasetX.extend(song_mfcc_X)
                datesetY.extend(song_label_Y)
                print audio_path
    return datasetX,datesetY

# trainX,trainY=batach_feature(wav_dir+'train')
# testX,testY=batach_feature(wav_dir+'test')
# validX,validY=batach_feature(wav_dir+'valid')
#
# file=h5py.File('dataProcessing.h5','w')
# file.create_dataset('trainX',data=trainX)
# file.create_dataset('trainY',data=trainY)
# file.create_dataset('testX',data=testX)
# file.create_dataset('testY',data=testY)
# file.create_dataset('validX',data=validX)
# file.create_dataset('validY',data=validY)
# file.close()


def get_data(h5_path='dataProcessing.h5'):
    file=h5py.File(h5_path,'r')
    trainX=file['trainX'][:]
    trainY = file['trainY'][:]
    testX = file['testX'][:]
    testY = file['testY'][:]
    validX = file['validX'][:]
    validY = file['validY'][:]
    file.close()
    return trainX,trainY,testX,testY,validX,validY



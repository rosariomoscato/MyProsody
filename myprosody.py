'''
Prosodic Library
Original Version Author: Shahab Sabahi
Modified and adapted by Rosario Moscato on 28-01-2021
'''

import parselmouth
from parselmouth.praat import call, run_file
import glob
import pandas as pd
import numpy as np
import scipy
from scipy.stats import binom
from scipy.stats import ks_2samp
from scipy.stats import ttest_ind
import os

def run_praat_file(m, p):
    """
    p : path to dataset folder
    m : path to file

    returns : objects outputed by the praat script
    """
  
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
  
    assert os.path.isfile(sound), "Wrong path to audio file"
    assert os.path.isfile(sourcerun), "Wrong path to praat script"
    assert os.path.isdir(path), "Wrong path to audio files"

    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        #print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        return z2
    except:
        z3 = 0
        print ("Try again the sound of the audio was not clear")


def myspsyl(m,p):
    """
    Detect and count number of syllables
    Returns: Integer
    """
    z2 = run_praat_file(m, p)
    z3=int(z2[0]) # will be the integer number 10
    z4=float(z2[3]) # will be the floating point number 8.3
    #print ("number_ of_syllables=",z3)
    return z3

def mysppaus(m,p):
    """
    Detect and count number of fillers and pauses
    Returns: Integer
    """
    z2 = run_praat_file(m, p)
    z3=int(z2[1]) # will be the integer number 10
    z4=float(z2[3]) # will be the floating point number 8.3
    #print ("number_of_pauses=",z3)
    return z3

def myspsr(m,p):
    """
    Measure the rate of speech (speed)
    Returns: Integer
    """
    z2 = run_praat_file(m, p)
    z3=int(z2[2]) # will be the integer number 10
    z4=float(z2[3]) # will be the floating point number 8.3
    #print ("rate_of_speech=",z3,"# syllables/sec original duration")
    return z3

def myspatc(m,p):
    """
    Measure the articulation (speed)
    Returns: Integer
    """
    z2 = run_praat_file(m, p)
    z3=int(z2[3]) # will be the integer number 10
    z4=float(z2[3]) # will be the floating point number 8.3
    #print ("articulation_rate=",z3,"# syllables/sec speaking duration")
    return z3

def myspst(m,p):
    """
    Measure speaking time (excl. fillers and pause)
    Returns: Integer
    """
    z2 = run_praat_file(m, p)
    z3=int(z2[3]) # will be the integer number 10
    z4=float(z2[4]) # will be the floating point number 8.3
    #print ("speaking_duration=",z4,"# sec only speaking duration without pauses")
    return z4

def myspod(m,p):
    """
    Measure total speaking duration (inc. fillers and pauses)
    Returns: Integer
    """
    z2 = run_praat_file(m, p)
    z3=int(z2[3]) # will be the integer number 10
    z4=float(z2[5]) # will be the floating point number 8.3
    #print ("original_duration=",z4,"# sec total speaking duration with pauses")
    return z4

def myspbala(m,p):
    """
    Measure ratio between speaking duration and total speaking duration
    Returns: Integer
    """
    z2 = run_praat_file(m, p)
    z3=int(z2[3]) # will be the integer number 10
    z4=float(z2[6]) # will be the floating point number 8.3
    #print ("balance=",z4,"# ratio (speaking duration)/(original duration)")
    return z4

def myspf0mean(m,p):
    """
    Measure fundamental frequency distribution mean
    Returns: Integer
    """
    z2 = run_praat_file(m, p)
    z3=int(z2[3]) # will be the integer number 10
    z4=float(z2[7]) # will be the floating point number 8.3
    #print ("f0_mean=",z4,"# Hz global mean of fundamental frequency distribution")
    return z4

def myspf0sd(m,p):
    """
    Measure fundamental frequency distribution SD
    Returns: Integer
    """
    z2 = run_praat_file(m, p)
    z3=int(z2[3]) # will be the integer number 10
    z4=float(z2[8]) # will be the floating point number 8.3
    #print ("f0_SD=",z4,"# Hz global standard deviation of fundamental frequency distribution")
    return z4

def myspf0med(m,p):
    """
    Measure fundamental frequency distribution median
    Returns: Integer
    """
    z2 = run_praat_file(m, p)
    z3=int(z2[3]) # will be the integer number 10
    z4=float(z2[9]) # will be the floating point number 8.3
    #print ("f0_MD=",z4,"# Hz global median of fundamental frequency distribution")
    return z4

def myspf0min(m,p):
    """
    Measure fundamental frequency distribution minimum
    Returns: Integer
    """
    z2 = run_praat_file(m, p)
    z3=int(z2[10]) # will be the integer number 10
    z4=float(z2[10]) # will be the floating point number 8.3
    #print ("f0_min=",z3,"# Hz global minimum of fundamental frequency distribution")
    return z3

def myspf0max(m,p):
    """
    Measure fundamental frequency distribution maximum
    Returns: Integer
    """
    z2 = run_praat_file(m, p)
    z3=int(z2[11]) # will be the integer number 10
    z4=float(z2[11]) # will be the floating point number 8.3
    #print ("f0_max=",z3,"# Hz global maximum of fundamental frequency distribution")
    return z3

def myspf0q25(m,p):
    """
    Measure 25th quantile fundamental frequency distribution
    Returns: Integer
    """
    z2 = run_praat_file(m, p)
    z3=int(z2[12]) # will be the integer number 10
    z4=float(z2[11]) # will be the floating point number 8.3
    #print ("f0_quan25=",z3,"# Hz global 25th quantile of fundamental frequency distribution")
    return z3

def myspf0q75(m,p):
    """
    Measure 75th quantile fundamental frequency distribution
    Returns: Integer
    """
    z2 = run_praat_file(m, p)
    z3=int(z2[13]) # will be the integer number 10
    z4=float(z2[11]) # will be the floating point number 8.3
    #print ("f0_quan75=",z3,"# Hz global 75th quantile of fundamental frequency distribution")
    return z3

def mysptotal(m,p):
    """
    Overview
    Returns: 14x1 (14 rows, 1 column) dataset
    """
    z2 = run_praat_file(m, p)
    z3=np.array(z2)
    z4=np.array(z3)[np.newaxis]
    z5=z4.T
    dataset=pd.DataFrame(
      {"number_of_syllables":z5[0,:],
       "number_of_pauses":z5[1,:],
       "rate_of_speech":z5[2,:],
       "articulation_rate":z5[3,:],
       "speaking_duration":z5[4,:],
       "original_duration":z5[5,:],
       "balance":z5[6,:],
       "f0_mean":z5[7,:],
       "f0_std":z5[8,:],
       "f0_median":z5[9,:],
       "f0_min":z5[10,:],
       "f0_max":z5[11,:],
       "f0_quantile25":z5[12,:],
       "f0_quantile75":z5[13,:]})
    #print (dataset.T)
    return dataset.T

def mysppron(m,p):
    """
    Pronunciation posteriori probability score percentage
    Returns: Integer
    """

    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        #print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=int(z2[13]) # will be the integer number 10
        z4=float(z2[14]) # will be the floating point number 8.3
        db= binom.rvs(n=10,p=z4,size=10000)
        a=np.array(db)
        b=np.mean(a)*100/10
        #print ("Pronunciation_posteriori_probability_score_percentage= :%.2f" % (b))
        return b
    except:
        print ("Try again the sound of the audio was not clear")
    return

def myspgend(m,p):
    """
    Gender recognition and mood of speech
    Returns: tuple (gender, mood of speech)
    """
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat" 
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        #print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
        z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z2=z1.strip().split()
        z3=float(z2[8]) # will be the integer number 10
        z4=float(z2[7]) # will be the floating point number 8.3
        if z4<=114:
            g=101
            j=3.4
        elif z4>114 and z4<=135:
            g=128
            j=4.35
        elif z4>135 and z4<=163:
            g=142
            j=4.85
        elif z4>163 and z4<=197:
            g=182
            j=2.7
        elif z4>197 and z4<=226:
            g=213
            j=4.5
        elif z4>226:
            g=239
            j=5.3
        else:
            print("Voice not recognized")
            exit()
        def teset(a,b,c,d):
            d1=np.random.wald(a, 1, 1000)
            d2=np.random.wald(b,1,1000)
            d3=ks_2samp(d1, d2)
            c1=np.random.normal(a,c,1000)
            c2=np.random.normal(b,d,1000)
            c3=ttest_ind(c1,c2)
            y=([d3[0],d3[1],abs(c3[0]),c3[1]])
            return y
        nn=0
        mm=teset(g,j,z4,z3)
        while (mm[3]>0.05 and mm[0]>0.04 or nn<5):
            mm=teset(g,j,z4,z3)
            nn=nn+1
        nnn=nn
        if mm[3]<=0.09:
            mmm=mm[3]
        else:
            mmm=0.35
        if z4>97 and z4<=114:
            #print("Male, mood of speech: Showing no emotion, normal, p-value/sample size= :%.2f" % (mmm), (nnn))
            result = ("Male", "Showing no emotion, normal.")
            return result
        elif z4>114 and z4<=135:
            #print("Male, mood of speech: Reading, p-value/sample size= :%.2f" % (mmm), (nnn))
            result = ("Male", "Reading.")
            return result
        elif z4>135 and z4<=163:
            #print("Male, mood of speech: speaking passionately, p-value/sample size= :%.2f" % (mmm), (nnn))
            result = ("Male", "Speaking passionately.")
            return result
        elif z4>163 and z4<=197:
            #print("Female, mood of speech: Showing no emotion, normal, p-value/sample size= :%.2f" % (mmm), (nnn))
            result = ("Female", "Showing no emotion, normal.")
            return result
        elif z4>197 and z4<=226:
            #print("Female, mood of speech: Reading, p-value/sample size= :%.2f" % (mmm), (nnn))
            result = ("Female", "Reading.")
            return result
        elif z4>226 and z4<=245:
            #print("Female", "Mood of speech: speaking passionately, p-value/sample size= :%.2f" % (mmm))
            result = ("Female", "Speaking passionately.")
            return result
        else:
            #print("Voice not recognized")
            return ("Interrupt","Voice not recognized")
    except:
        #print ("Try again the sound of the audio was not clear")
        return ("Interrupt","Try again the sound of the audio was not clear")

def myprosody(m,p):
    """
    Compared to native speech, here are the prosodic features of your speech
    Returns: printed report
    """
    sound=p+"/"+"dataset"+"/"+"audioFiles"+"/"+m+".wav"
    sourcerun=p+"/"+"dataset"+"/"+"essen"+"/"+"MLTRNL.praat"
    path=p+"/"+"dataset"+"/"+"audioFiles"+"/"
    outo=p+"/"+"dataset"+"/"+"datanewchi22.csv"
    outst=p+"/"+"dataset"+"/"+"datanewchi44.csv"
    outsy=p+"/"+"dataset"+"/"+"datanewchi33.csv"
    pa2=p+"/"+"dataset"+"/"+"stats.csv"
    pa7=p+"/"+"dataset"+"/"+"datanewchi44.csv" 
    result_array = np.empty((0, 100))
    files = glob.glob(path)
    result_array = np.empty((0, 27))
    try:
        objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
        z1=( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
        z3=z1.strip().split()
        z2=np.array([z3])
        result_array=np.append(result_array,[z3], axis=0)
        #print(z3)
        np.savetxt(outo,result_array, fmt='%s',delimiter=',')
        #Data and features analysis
        df = pd.read_csv(outo,
						 names = ['avepauseduratin','avelongpause','speakingtot','avenumberofwords','articulationrate','inpro','f1norm','mr','q25',
								  'q50','q75','std','fmax','fmin','vowelinx1','vowelinx2','formantmean','formantstd','nuofwrds','npause','ins',
								  'fillerratio','xx','xxx','totsco','xxban','speakingrate'],na_values='?')
        scoreMLdataset=df.drop(['xxx','xxban'], axis=1)
        scoreMLdataset.to_csv(outst, header=False,index = False)
        newMLdataset=df.drop(['avenumberofwords','f1norm','inpro','q25','q75','vowelinx1','nuofwrds','npause','xx','totsco','xxban','speakingrate','fillerratio'], axis=1)
        newMLdataset.to_csv(outsy, header=False,index = False)
        namess=nms = ['avepauseduratin','avelongpause','speakingtot','articulationrate','mr',
								  'q50','std','fmax','fmin','vowelinx2','formantmean','formantstd','ins',
								  'xxx']
        df1 = pd.read_csv(outsy, names = namess)
        nsns=['average_syll_pause_duration','No._long_pause','speaking_time','ave_No._of_words_in_minutes','articulation_rate','No._words_in_minutes','formants_index','f0_index','f0_quantile_25_index',
								  'f0_quantile_50_index','f0_quantile_75_index','f0_std','f0_max','f0_min','No._detected_vowel','perc%._correct_vowel','(f2/f1)_mean','(f2/f1)_std',
									'no._of_words','no._of_pauses','intonation_index',
						'(voiced_syll_count)/(no_of_pause)','TOEFL_Scale_Score','Score_Shannon_index','speaking_rate']
        dataframe = pd.read_csv(pa2)
        df55 = pd.read_csv(outst,names=nsns)
        dataframe=dataframe.values
        array = df55.values
        print("Compared to native speech, here are the prosodic features of your speech:")
        for i in range(25):
            sl0=dataframe[4:7:1,i+1]
            score = array[0,i]
            he=scipy.stats.percentileofscore(sl0, score, kind='strict')
            if he==0:
                he=25
                dfout = "%s:\t %f (%s)" %  (nsns[i],he,"% percentile ")
                print(dfout)
            elif he>=25 and he<=75:
                dfout = "%s:\t %f (%s)" % (nsns[i],he,"% percentile ")
                print(dfout)
            else:
                dfout = "%s:\t (%s)" % (nsns[i],":Out of Range")
                print(dfout)
    except:
        print ("Try again the sound of the audio was not clear")	


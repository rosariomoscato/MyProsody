import myprosody as mysp
import pickle

p="julia_1" #file name without extension (.wav)
c=r"/home/runner/MyProsody/myprosody" #(absolute path to myprosody folder)

#Statistics Overview
total = mysp.mysptotal(p,c)
print(total[0])

#Gender ID + speech mood (semantic analysis)
#result = mysp.myspgend(p,c)
#print("Gender:",result[0])
#print("Mood of speech:",result[1])

#Number of Syllables
#nsyl = mysp.myspsyl(p,c)
#print("Number of Syllables:",nsyl)

#Number of Pauses
#npau = mysp.mysppaus(p,c)
#print("Number of Pauses:", npau)

#Rate of Speech (syllables/second)
#sprate = mysp.myspsr(p,c)
#print("Rate of Speech:", sprate)

#Articulation Rate
#artrate = mysp.myspatc(p,c)
#print("Articulation Rate:", artrate)

#Speaking Duration (sec only speaking duration without pauses)
#spduration = mysp.myspst(p,c)
#print("Speaking Duration (sec, only speaking duration without pauses):", spduration)

#Original Duration (sec total speaking duration with pauses)
#orduration = mysp.myspod(p,c)
#print("Original Duration (sec, total speaking duration with pauses):", orduration)

#Balance Ratio (speaking duration/original duration)
#bala = mysp.myspbala(p,c)
#print("Balance Ratio (speaking duration/original duration):", bala)

#f0 mean (global mean of fundamental frequency distribution Hz)
#f0mean = mysp.myspf0mean(p,c)
#print("F0 Mean (global mean of fundamental frequency distribution in Hz):", f0mean)

#f0 SD (global standard deviation of fundamental frequency distribution Hz)
#f0sd = mysp.myspf0sd(p,c)
#print("F0 SD (global standard deviation of fundamental frequency distribution in Hz):", f0sd)

#f0 MD (global median of fundamental frequency distribution Hz)
#f0med = mysp.myspf0med(p,c)
#print("F0 Median (global median of fundamental frequency distribution in Hz):", f0med)

#f0 Min (global minimum of fundamental frequency distribution)
#f0min = mysp.myspf0min(p,c)
#print("F0 Minimum (global minimum of fundamental frequency distribution in Hz):", f0min)

#f0 Max (global maximum of fundamental frequency distribution Hz)
#f0max = mysp.myspf0max(p,c)
#print("F0 Maximum (global maximum of fundamental frequency distribution in Hz):", f0max)

#f0 quan25 (global 25th quantile of fundamental frequency distribution Hz)
#f025 = mysp.myspf0q25(p,c)
#print("F0 25th Quantile (global 25th quantile of fundamental frequency distribution in Hz):", f025)

#f0 quan75 (global 75th quantile of fundamental frequency distribution)
#f075 = mysp.myspf0q75(p,c)
#print("F0 75th Quantile (global 75th quantile of fundamental frequency distribution in Hz):", f075)

#Pronunciation posteriori probability score percentage
#post = mysp.mysppron(p,c)
#print("Pronunciation posteriori probability score percentage:", round(post,3))

#Compared to native speech, here are the PROSODIC features of your speech
#mysp.myprosody(p,c)


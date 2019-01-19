import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag
import pandas as pd
import scipy.stats as st


dane = pd.read_csv(r"sub-01_trial-03.csv", delimiter=',', engine='python')
prob=200

t = np.linspace (0, 37.96, 200*37.96)
sygnal=dane['kol2']

sygnalfiltr= ag.pasmowozaporowy(sygnal, prob, 49,51 )
sygnalfiltr2= ag.pasmowoprzepustowy(sygnalfiltr, prob, 1, 50)

plt.plot(sygnalfiltr2)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()

koda=[]
for i in range(len(sygnalfiltr2)):
    if sygnalfiltr2[i] > 0.2:
        koda.append(dane.kol6[i])
koda2=[]
for i in range(len(koda)):
    if koda[i] != koda[i-1]:
        koda2.append(koda[i])
print("Wymrugany kod:",koda2)

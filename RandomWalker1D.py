5# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 12:30:08 2022

@author: nemot
"""

# dit is een random walker in de eerste dimentie. Deze is ontworpen om SAW's beter te kunnen begrijpen
import random
import numpy
import matplotlib.pyplot as plt

#kl en kh getal tussen 0 en 1 invullen voor "kanshoger", "kanslager"
# kl en kh representeren dus de kans dat er een stap omhoog en omlaag gezet word
# mi is minimale waarde van grafiek en ma maximale waarde

def rw1d(n, kl, kh, mi, ma): # voor het aanroepen van de code dus rw1d(aantal stappen, kans omhoog, kans omlaag, ondergrens, bovengrens)
    
    #kans[0] is dus kans omlaag en kans[1] is dus kans omhoog
    kans = [kl, kh]
    
    #begin postitie = 0
    start = 0
    # houd de posities bij 
    posities = [start]
    
    # willekeurige plaatsen genereren
    rr = numpy.random.random(n) #aantal willekeurige stappen 
    plager = rr < kans[0]
    phoger = rr > kans[1]
    
    for iplager, iphoger in zip(plager, phoger):
        lager = iplager and posities[-1] > mi
        hoger = iphoger and posities[-1] < ma
        posities.append(posities[-1] - lager + hoger)
    
    #print(posities) # om posities bij te houden (niet gebruiken bij hoge n ivm laadtijd)
    return posities
    
# rw2 en rw 3 kunnen gebruikt worden om walks te vergelijken

rw1 = rw1d(20, 0.5, 0.5, -10, 10)   
rw2 = rw1d(20, 0.5, 0.5, -10, 10)
rw3 = rw1d(20, 0.5, 0.5, -10, 10)

# grafiek plotten in 1D 
plt.plot(rw1, 'r-') #plot eerste grafiek

# hiermee worden de andere twee walks gesimuleerd
plt.plot(rw2, 'g-') #plot tweede grafiek
plt.plot(rw3, 'b-') #plot derde grafiek
plt.title("Random Walk in 1ste dimensie") #geeft titel boven grafiek
plt.show() #laat de grafiek visueel zien


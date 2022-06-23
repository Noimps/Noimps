# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 13:06:07 2022

@author: nemot
"""
# Dit is de tweede walker die ik voor dit project heb uitgewerkt.
# Deze random walkers zijn gemaakt om de SAW beter te begrijpen en ervaring op te doen voor het programmeren van walkers

import numpy
import random
import pylab

# n = aantal stappen
# begint altijd op (0,0)
# n is het aantal stappen xmin en xmax geven de maximale x waarden van de grafiek aan en ymin/ymax doen dat voor de y-as
def rw2d(n, xmin, xmax, ymin, ymax):
    stappen = []
    x = numpy.zeros(n)  # er worden n x posities 
    y = numpy.zeros(n)  # er komen n y posities
    stap = x[0], y[0]
    stappen.append(stap)
    for i in range(1, n):
        
        if x[i - 1] == xmin:    # zorgt dat er geen stappen buiten de grafiek worden genomen
            stap = random.choice([1, 3, 4])
            
        elif x[i - 1] == xmax:   # zorgt dat er geen stappen buiten de grafiek worden genomen
            stap = random.choice([2, 3, 4])
            
        elif y[i - 1] == ymin:   # zorgt dat er geen stappen buiten de grafiek worden genomen
            stap = random.choice([1, 2, 3])
            
        elif y[i - 1] == ymax:  # zorgt dat er geen stappen buiten de grafiek worden genomen
            stap = random.choice([1, 2, 4])
            
        else: #kiest n willekeurige getallen tussen 1 en 4
            stap = random.randint(1, 4)
        
        #als stap = 1 dan een stap positieve stap over x as (naar rechts)
        if stap == 1:
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
            stap = x[i],y[i]
            stappen.append(stap)
        # als stap = 2 dan een negatieve stap over de x as (naar links)
        elif stap == 2:
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
            stap = x[i],y[i]
            stappen.append(stap)
        # als stap = 3 dan een postitieve stap over y as (omhoog)
        elif stap == 3:
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
            stap = x[i],y[i]
            stappen.append(stap)
        # als stap = 4 dan een negatieve stap over y as (omlaag)
        
        else:
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1
            stap = x[i],y[i]
            stappen.append(stap)
   
    #grafiek plotte plotten
    pylab.title("Random Walk 2D ($n = " + str(n) + "$ stappen)") # naam boven de grafiek
    pylab.plot(x, y) # plot de x en y assen 
    
    # niet aanzetten tenzij je daadwerkelijk onderzoek gaat doen anders krijg je veel grafieken in je files.
    # pylab.savefig("rand_walk"+str(n)+".png",bbox_inches ="tight", dpi = 600) # hiermee worden de grafieken in files opgeslagen
  
    pylab.show()

rw2d(100, -30, 30, -30, 30)
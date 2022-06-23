# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 13:44:09 2022

@author: nemot
"""

#Deze code is gebaseerd op de code gebruikt voor het maken van een 2D walker, echter kunnen de stappen naar binnen en naar buiten
#nu ook uitgevoerd worden (positieve en negatieve stappen over de z-as)
import numpy
import random
import pylab
import matplotlib.pyplot as plt

# n = aantal stappen
# begint altijd op (0, 0, 0)
# deze code hoeft slechts aangeroepen te worden door het aantal stappen te geven
# er is dus geen maximale waarde van de assen

def rw3d(n):
    
    x = numpy.zeros(n)      #zorgt ervoor dat er n x-as cordinaten komen
    y = numpy.zeros(n)      #zorgt ervoor dat er n y-as cordinaten komen
    z = numpy.zeros(n)      #zorgt ervoor dat er n z-as cordinaten komen
    posities = [(int(x[0]), int(y[0]), int(z[0]))]  #hiermee worden de bezette posities per i bijgehouden
    for i in range(1, n):
        #kiest n willekeurige getallen tussen 1 en vier
        stap = random.randint(1, 6)
        
        #als stap = 1 dan een stap positieve stap over x as (naar rechts)
        if stap == 1:
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
            z[i] = z[i - 1]
            
            
        # als stap = 2 dan een negatieve stap over de x as (naar links)
        elif stap == 2:
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
            z[i] = z[i - 1]
            
        # als stap = 3 dan een postitieve stap over y as (omhoog)
        elif stap == 3:
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
            z[i] = z[i - 1]
            
        # als stap = 4 dan een negatieve stap over y as (omlaag)
        elif stap == 4:
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1
            z[i] = z[i - 1]
            
        # als stap = 5 dan een positieve stap over z as
        elif stap == 5:
            x[i] = x[i - 1]
            y[i] = y[i - 1]
            z[i] = z[i - 1] + 1
        #negatieve stap over de z-as
        elif stap == 5:
            x[i] = x[i - 1]
            y[i] = y[i - 1]
            z[i] = z[i - 1] - 1
       
        posities.append((int(x[i]), int(y[i]), int(z[i])))
   
    
    return x, y, z 


#door de 10 in rw3d() te veranderen word het aantal stappen aangepast
x_cord, y_cord, z_cord = rw3d(10) #in rw3d(n) geeft het in te voeren getal het aantal stappen aan.


ax = plt.subplot(1, 1, 1, projection='3d')
ax.plot(x_cord, y_cord, z_cord, alpha=1.0) #plot de lijn en alpha geeft dikte van de lijn
ax.scatter(x_cord[-1], y_cord[-1], z_cord[-1]) # hierdoor eindigd de lijn bij het laatste punt 
            
plt.show()


    
    
    
   

    
        
    #grafiek plotte plotten
    #pylab.title("Random Walk 3D ($n = " + str(n) + "$ stappen)") # naam boven de grafiek
    #pylab.plot(x, y) # plot de x en y assen 
    
    # niet aanzetten tenzij je daadwerkelijk onderzoek gaat doen anders krijg je veel grafieken in je files.
    # pylab.savefig("rand_walk"+str(n)+".png",bbox_inches ="tight", dpi = 600) # hiermee worden de grafieken in files opgeslagen
  
  


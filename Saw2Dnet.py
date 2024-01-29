# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 18:17:58 2022

@author: nemot
"""

import numpy
import random
import pylab
import matplotlib.pyplot as plt

def check(point): # controle van de bezochte posities

    
    directions = [
        (point[0]+1, point[1]),  # Rechts
        (point[0]-1, point[1]),  # Links
        (point[0], point[1]+1),  # naar boven
        (point[0], point[1]-1),  # naar beneden
    ]
    return directions


def rw2d(n):
    stappen = range(n)                                                                                      # er worden n stappen gezet
    positie = (0, 0)                                                                                        # de eerste bezochte positie
    bezocht = []                                                                                            # houd bij welke posities er bezocht zijn 
    for _ in stappen:
        bezocht.append(positie)                                                                             
        all_directions = check(positie)                                                                     # er word bekeken wat de uitkomsten van stappen in iedere richting zijn
        not_visited_directions = [direction for direction in all_directions if direction not in bezocht]    # deze uitkomsten worden vergeleken met de al bezochte posities, de niet bezochte uitkomsten worden als stap optie opgeslagen
        positie = random.choice(not_visited_directions)                                                     # Er word willekeurig uit de stappen met niet bezochte uitkomsten gekozen

    x_cord, y_cord = zip(*bezocht)
    return x_cord, y_cord              



if __name__ == "__main__":
    n = 10
    saw1 = rw2d(n)                              
    #grafiek plotte plotten
    pylab.title("Self vermijdende wandeling 2D ($n = " + str(n) + "$ stappen)") # naam boven de grafiek
    pylab.plot(saw1[0], saw1[1]) # plot de x en y assen 
    
    saw2 = rw2d(10)
    pylab.plot(saw2[0], saw2[1], '-r')          #plot een tweede SAW in het rood
    

    saw3 = rw2d(10)
    pylab.plot(saw3[0], saw3[1], '-g')              #plot een derde SAW in het groen

    # niet aanzetten tenzij je daadwerkelijk onderzoek gaat doen anders krijg je veel grafieken in je files.
    # pylab.savefig("rand_walk"+str(n)+".png",bbox_inches ="tight", dpi = 600) # hiermee worden de grafieken in files opgeslagen
  
pylab.show()

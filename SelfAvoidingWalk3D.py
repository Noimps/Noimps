# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 18:04:28 2022

@author: nemot
"""

import numpy
import random
import pylab
import matplotlib.pyplot as plt

def check(positie): # controle van de bezochte posities

    
    richtingen = [
        (positie[0]+1, positie[1], positie[2]),  # omhoog
        (positie[0]-1, positie[1], positie[2]),  # link
        (positie[0], positie[1]+1, positie[2]),  # naar voren
        (positie[0], positie[1]-1, positie[2]),  # naar achter
        (positie[0], positie[1], positie[2]+1),  # omhoog
        (positie[0], positie[1], positie[2]-1)   # omlaag
    ]
    return richtingen


def rw3d(n):
        stappen = range(n)                                                                                      # er worden n stappen gezet
    positie = (0, 0, 0)                                                                                        # de eerste bezochte positie
    bezocht = []                                                                                               # houd bij welke posities er bezocht zijn 
    for _ in stappen:
        bezocht.append(positie)                                                                             
        all_directions = check(positie)                                                                     # er word bekeken wat de uitkomsten van stappen in iedere richting zijn
        not_visited_directions = [direction for direction in all_directions if direction not in bezocht]    # deze uitkomsten worden vergeleken met de al bezochte posities, de niet bezochte uitkomsten worden als stap optie opgeslagen
        positie = random.choice(not_visited_directions)                                                     # Er word willekeurig uit de stappen met niet bezochte uitkomsten gekozen


    x_cord, y_cord, z_cord = zip(*bezocht)
    return x_cord, y_cord, z_cord  



saw1 = rw3d(100) #in rw3d geeft het in te voeren getal het aantal stappen aan.
ax = plt.subplot(1, 1, 1, projection='3d')
ax.plot(saw1[0], saw1[1], saw1[2], '-b', alpha=1.0) #plot de lijn en alpha geeft dikte van de lijn
ax.scatter(saw1[0][-1], saw1[1][-1], saw1[2][-1])

saw2 = rw3d(10)
ax = plt.subplot(1, 1, 1, projection='3d')
ax.plot(saw2[0], saw2[1], saw2[2], '-r', alpha=1.0) #plot de lijn en alpha geeft dikte van de lijn
ax.scatter(saw2[0][-1], saw2[1][-1], saw2[2][-1])

saw3 = rw3d(10)
ax = plt.subplot(1, 1, 1, projection='3d')
ax.plot(saw3[0], saw3[1], saw3[2], '-g', alpha=1.0) #plot de lijn en alpha geeft dikte van de lijn
ax.scatter(saw3[0][-1], saw3[1][-1], saw3[2][-1])

                
plt.show()



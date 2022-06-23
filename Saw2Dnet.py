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
    stappen = range(n)
    positie = (0, 0)
    bezocht = []
    for _ in stappen:
        bezocht.append(positie)
        all_directions = check(positie)
        not_visited_directions = [direction for direction in all_directions if direction not in bezocht]
        positie = random.choice(not_visited_directions)

    x_cord, y_cord = zip(*bezocht)
    return x_cord, y_cord # returns tuples. If you want lists, just do list(xp), ...



if __name__ == "__main__":
    n = 10
    saw1 = rw2d(n)
    #grafiek plotte plotten
    pylab.title("Self vermijdende wandeling 2D ($n = " + str(n) + "$ stappen)") # naam boven de grafiek
    pylab.plot(saw1[0], saw1[1]) # plot de x en y assen 
    
    saw2 = rw2d(10)
    pylab.plot(saw2[0], saw2[1], '-r')
    

    saw3 = rw2d(10)
    pylab.plot(saw3[0], saw3[1], '-g')

    # niet aanzetten tenzij je daadwerkelijk onderzoek gaat doen anders krijg je veel grafieken in je files.
    # pylab.savefig("rand_walk"+str(n)+".png",bbox_inches ="tight", dpi = 600) # hiermee worden de grafieken in files opgeslagen
  
pylab.show()
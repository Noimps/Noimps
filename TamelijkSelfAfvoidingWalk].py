# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 16:00:48 2022

@author: nemot
"""

import numpy
import random
import pylab

# n = aantal stappen
# begint altijd op (0,0)

def rw2d(n):
    stappen = []        # om bij te houden welke posities al ingenomen zijn
    x = numpy.zeros(n**2)
    y = numpy.zeros(n**2) 
    p = 1
    stap = int(x[0]),int(y[0])
    stappen.append(stap)
    xmin = 0
    xmax = n - 1
    ymin = 0
    ymax = n - 1
    pmax = n ** 2   #maximale aantal postities
    
#    while p != pmax:
    for i in range(1, pmax):
        print(stappen)
        if x[i - 1] == xmin and y[i - 1] == ymin:
            #stap = random.choice[1,3]
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
            stap = int(x[i]),int(y[i])
            print(stap)
            for j in range(0, len(stappen)):
                if stap == stappen[j]:
                    x[i] = x[i - 1]
                    y[i] = y[i - 1] + 1
                    stap = int(x[i]),int(y[i])
                    stappen.append(stap)
                    for k in range(0, len(stappen)):
                        if stap == stappen[k]:
                            break #terug gaan naar vorige i en andere optie kiezen
                        elif k == len(stappen) - 1 and stap != stappen[k]:
                            stappen.append(stap)
                                
                elif j == len(stappen) - 1 and stap != stappen[j]:
                    stappen.append(stap) 
            
        elif x[i - 1] == xmax and y[i - 1] == ymax:
            #stap = random.choice[2,4]
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
            stap = int(x[i]),int(y[i])
            for j in range(0, len(stappen)):
                if stap == stappen[j]:
                    x[i] = x[i - 1]
                    y[i] = y[i - 1] - 1
                    stap = int(x[i]),int(y[i])
                    for k in range(0, len(stappen)):
                        if stap == stappen[k]:
                            break #terug gaan naar vorige i en andere optie kiezen
                        elif k == len(stappen) - 1 and stap != stappen[k]:
                            stappen.append(stap)
                                
                elif j == len(stappen) - 1 and stap != stappen[j]:
                    stappen.append(stap) 
            
            
        elif x[i - 1] == xmin:    # zorgt dat er geen stappen buiten de grafiek worden genomen
            #stap = random.choice([1, 3, 4])
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
            stap = int(x[i]),int(y[i])
            for j in range(0, len(stappen)):
                if stap == stappen[j]:
                    x[i] = x[i - 1]
                    y[i] = y[i - 1] + 1
                    stap = int(x[i]),int(y[i])
                    stappen.append(stap)
                    for k in range(0, len(stappen)):
                        if stap == stappen[k]:
                            x[i] = x[i - 1]
                            y[i] = y[i - 1] - 1
                            stap = int(x[i]),int(y[i])
                            for l in range(0, len(stappen)):
                                if stap == stappen[l]:
                                    break # terug naar vorige stap
                                elif l == len(stappen) - 1 and stap != stappen[l]:
                                    stappen.append(stap)
                        elif k == len(stappen) - 1 and stap != stappen[k]:
                            stappen.append(stap)
                                
                elif j == len(stappen) - 1 and stap != stappen[j]:
                    stappen.append(stap) 
                
        elif x[i - 1] == xmax:   # zorgt dat er geen stappen buiten de grafiek worden genomen
            # stap = random.choice([2, 3, 4])
            print("xmax")
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
            stap = int(x[i]),int(y[i])
            for j in range(0, len(stappen)):
                if stap == stappen[j]:
                    x[i] = x[i - 1]
                    y[i] = y[i - 1] + 1
                    stap = int(x[i]),int(y[i])
                 
                    for k in range(0, len(stappen)):
                        print(stap)
                        print(stappen, 'stappebn')
                        if stap == stappen[k]:
                            x[i] = x[i - 1]
                            y[i] = y[i - 1] - 1
                            stap = int(x[i]),int(y[i])
                            for l in range(0, len(stappen)):
                                if stap == stappen[l]:
                                    break # terug naar vorige stap
                                elif l == len(stappen) - 1 and stap != stappen[l]:
                                    stappen.append(stap)
                        elif k == len(stappen) - 1 and stap != stappen[k]:
                            stappen.append(stap)
                                
                elif j == len(stappen) - 1 and stap != stappen[j]:
                    stappen.append(stap) 
                    
        elif y[i - 1] == ymin:   # zorgt dat er geen stappen buiten de grafiek worden genomen
           #stap = random.choice([1, 2, 3])
           x[i] = x[i - 1] + 1
           y[i] = y[i - 1]
           stap = int(x[i]),int(y[i])
           for j in range(0, len(stappen)):
               if stap == stappen[j]:
                   x[i] = x[i - 1] - 1
                   y[i] = y[i - 1]
                   stap = int(x[i]),int(y[i])
                   for k in range(0, len(stappen)):
                       if stap == stappen[k]:
                           x[i] = x[i - 1]
                           y[i] = y[i - 1] + 1
                           stap = int(x[i]),int(y[i])
                           for l in range(0, len(stappen)):
                               if stap == stappen[l]:
                                  break
                               elif l == len(stappen) - 1 and stap != stappen[l]:
                                   stappen.append(stap)
                       elif k == len(stappen) - 1 and stap != stappen[k]:
                           stappen.append(stap)
                               
               elif j == len(stappen) - 1 and stap != stappen[j]:
                   stappen.append(stap) 
                
        elif y[i - 1] == ymax:  # zorgt dat er geen stappen buiten de grafiek worden genomen
           # stap = random.choice([1, 2, 4])
           x[i] = x[i - 1] + 1
           y[i] = y[i - 1]
           stap = int(x[i]),int(y[i])
           for j in range(0, len(stappen)):
               if stap == stappen[j]:
                   x[i] = x[i - 1] - 1
                   y[i] = y[i - 1]
                   stap = int(x[i]),int(y[i])
                   for k in range(0, len(stappen)):
                       if stap == stappen[k]:
                           x[i] = x[i - 1]
                           y[i] = y[i - 1] - 1
                           stap = int(x[i]),int(y[i])
                           for l in range(0, len(stappen)):
                               if stap == stappen[l]:
                                   break
                               elif l == len(stappen) - 1 and stap != stappen[l]:
                                   stappen.append(stap)
                       elif k == len(stappen) - 1 and stap != stappen[k]:
                           stappen.append(stap)
                               
               elif j == len(stappen) - 1 and stap != stappen[j]:
                   stappen.append(stap) 
                
        else: #kiest n willekeurige getallen tussen 1 en 4
            #stap = random.randint(1, 4)
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
            stap = int(x[i]),int(y[i])
            for j in range(0, len(stappen)):
                if stap == stappen[j]:
                    x[i] = x[i - 1] - 1
                    y[i] = y[i - 1]
                    stap = int(x[i]),int(y[i])
                    for k in range(0, len(stappen)):
                        if stap == stappen[k]:
                            x[i] = x[i - 1]
                            y[i] = y[i - 1] + 1
                            stap = int(x[i]),int(y[i])
                            for l in range(0, len(stappen)):
                                if stap == stappen[l]:
                                    x[i] = x[i - 1]
                                    y[i] = y[i - 1] - 1
                                    stap = int(x[i]),int(y[i])
                                    for m in range(0, len(stappen)):
                                        if stap == stappen[m]:
                                            break
                                        elif m == len(stappen) - 1 and stap != stappen[m]:
                                            stappen.append(stap)
                                elif l == len(stappen) - 1 and stap != stappen[l]:
                                    stappen.append(stap)
                                        
                        elif k == len(stappen) - 1 and stap != stappen[k]:
                            stappen.append(stap) 
                elif j == len(stappen) - 1 and stap != stappen[j]:
                    stappen.append(stap)
        
    print(stappen)
    #grafiek plotte plotten
    pylab.title("Random Walk 2D ($n = " + str(n) + "$ stappen)") # naam boven de grafiek
    pylab.plot(x, y) # plot de x en y assen 
    
    # niet aanzetten tenzij je daadwerkelijk onderzoek gaat doen anders krijg je veel grafieken in je files.
    # pylab.savefig("rand_walk"+str(n)+".png",bbox_inches ="tight", dpi = 600) # hiermee worden de grafieken in files opgeslagen
  
    pylab.show()

rw2d(10)
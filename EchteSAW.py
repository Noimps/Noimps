# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 20:13:52 2022

@author: nemot
"""

import numpy
import random
import pylab

# n = aantal stappen
# begint altijd op (0,0)


    
def check(keuzes, x, y, stappen, i, last, elast, gekozen, keuze):
        keuze = keuzes[-1]
        keuzes.pop()
        x[i - 1] = x[i - 2]
        y[i - 1] = y[i - 2]
        i -= 1
        stappen.pop()
        for j in range(0, len(keuze)):
            if keuze[j] == last:
                keuze.pop(j)
                if len(keuze) >= 1:
                        break
                else:
                    
                    gekozen.pop()
                    last = gekozen[-1]
                    elast = gekozen[-2]
                    keuzes, x, y, stappen, i, last, elast, gekozen, keuze  = check(keuzes, x, y, stappen, i, last, elast, gekozen, keuze)
                    
        if keuze == []:
            saw2d(n)
        return keuzes, x, y, stappen, i, last, elast, gekozen, keuze    
        

def saw2d(n):
    gekozen = [0]                                   #om bij te houden in welke richting er telkens word gestapt
    stappen = []                                    #houd de eerder bezette posities bij
    x = numpy.zeros(n + 1)                          #zorg ervoor dat er n + 1 x cordinaten komen
    y = numpy.zeros(n + 1)  #                       #zorg ervoor dat er n + 1 x cordinaten komen
    stap = x[0], y[0]                               #om de positie (0,0) aan stappen toe te voegen
    stappen.append(stap)                            #Positie word daadwerkelijk toegevoegd
    last = 0                                        # houd bij welke richting er voor het laatst heen is gestapt
    keuze = []                                      #word telkens opnieuw gebruikt om aan te geven welke stap mogelijk heden er op tijd i zijn 
    keuzes = []                                      #om bij te houden welke keuze mogelijkheden er telkens bij stap i waren
    i = 1                                           # houd stappen bij 
    elast = 0                                         #houd bij in welke richting er 2 stappen geleden is gestapt (voor backtracken)
    while i != n + 1:
        if last != 2:
            for j in range(0, len(stappen)):
                R = int(x[i - 1] + 1), int(y[i - 1])
                RR = int(x[i - 1] + 2), int(y[i - 1])
                RD = int(x[i - 1] + 1), int(y[i - 1] - 1)
                RH = int(x[i - 1] + 1), int(y[i - 1] + 1)
                a = 3
                
                if R == stappen[j]:
                    break
                if j == len(stappen) - 1:
                    for m in range(0, len(stappen)):
                        if RR == stappen[m]:
                            a -= 1
                            
                        if RD == stappen[m]:
                            a -= 1
                            
                        if RH == stappen[m]:
                            a -= 1
                    
                    if a >= 1:
                        
                        keuze.append(1)
                        break
        if last != 1:             
            for k in range(0, len(stappen)):
                b = 3
                L = int(x[i - 1] - 1), int(y[i - 1])
                LL = int(x[i - 1] - 2), int(y[i - 1])
                LD = int(x[i - 1] + 1), int(y[i - 1] - 1)
                LH = int(x[i - 1] + 1), int(y[i - 1] + 1)
                
                if L == stappen[k]:
                    break
                
                if k == len(stappen) - 1:
                    for m in range(0, len(stappen)):
                        if LL == stappen[m]:
                            b -= 1
                            
                        if LD == stappen[m]:
                            b -= 1
                            
                        if LH == stappen[m]:
                            b -= 1
                    if b >= 1:
                        
                        keuze.append(2)
                        break
        if last != 4:
            for l in range(0, len(stappen)):
                c = 3
                H = int(x[i - 1]), int(y[i - 1] + 1)
                HR = int(x[i - 1] + 1), int(y[i - 1] + 1)
                HL = int(x[i - 1] - 1), int(y[i - 1] + 1)
                HH = int(x[i - 1]), int(y[i - 1] + 2)
                
                if H == stappen[l]:
                    break
                
                if l == len(stappen) - 1:
                    for m in range(0, len(stappen)):
                        if HR == stappen[m]:
                            c -= 1
                            
                        if HL == stappen[m]:
                            c -= 1
                            
                        if HH == stappen[m]:
                            c -= 1
                    if c >= 1:
                        keuze.append(3)
                        break
        if last != 3:            
            for t in range(0, len(stappen)):
                d = 3
                O = int(x[i - 1]), int(y[i - 1] - 1)
                OR = int(x[i - 1] + 1), int(y[i - 1] - 1)
                OL = int(x[i - 1] - 1), int(y[i - 1] - 1)
                OO = int(x[i - 1]), int(y[i - 1] - 2)
                
                if O == stappen[t]:
                    break
                
                if t == len(stappen) - 1:
                    for m in range(0, len(stappen)):
                        if OR == stappen[m]:
                            d -= 1
                            
                        if OL == stappen[m]:
                            d -= 1
                            
                        if OO == stappen[m]:
                            d -= 1
                    if d >= 1:
                        keuze.append(4)
                        break
        if i >= 3:
            if len(keuzes[-2]) == 1 and len(keuze) == 1:
                keuzes, x, y, stappen, i, last, elast, gekozen, keuze = check(keuzes, x, y, stappen, i, last, elast, gekozen, keuze)
                stap = random.choice(keuze)    
                keuzes.append(keuze)
                gekozen.append(stap)
                elast = gekozen[-2]
                last = gekozen[-1]
            
        if keuze == []:
            keuzes, x, y, stappen, i, last, elast, gekozen, keuze = check(keuzes, x, y, stappen, i, last, elast, gekozen, keuze)
            stap = random.choice(keuze)    
            keuzes.append(keuze)
            gekozen.append(stap)
            elast = gekozen[-2]
            last = gekozen[-1]
            
        else:
        #kiest n willekeurige getallen tussen 1 en 4
            keuzes.append(keuze)
            stap = random.choice(keuze)
            gekozen.append(stap)
            elast = gekozen[-2]
            last = gekozen[-1]
        
        
        #als stap = 1 dan een stap positieve stap over x as (naar rechts)
        if stap == 1:
        
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
            stap = x[i],y[i]
            keuze = []
            stappen.append(stap)
            i += 1
        # als stap = 2 dan een negatieve stap over de x as (naar links)
        elif stap == 2:
            
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
            stap = x[i],y[i]
            keuze = []
            stappen.append(stap)
            i += 1
        # als stap = 3 dan een postitieve stap over y as (omhoog)
        elif stap == 3:
            
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
            stap = x[i],y[i]
            keuze = []
            stappen.append(stap)
            i += 1
        # als stap = 4 dan een negatieve stap over y as (omlaag)
        
        else:
            
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1
            stap = x[i],y[i]
            keuze = []
            stappen.append(stap)
            i += 1 
    return x, y

if __name__ == "__main__":
    n = 100
    saw1 = saw2d(n)
    #grafiek plotte plotten
    pylab.title("Self vermijdende wandeling 2D ($n = " + str(n) + "$ stappen)") # naam boven de grafiek
    pylab.plot(saw1[0], saw1[1]) # plot de x en y assen 
    
    saw2 = saw2d(10)
    pylab.plot(saw2[0], saw2[1], '-r')
    

    saw3 = saw2d(10)
    pylab.plot(saw3[0], saw3[1], '-g')

    # niet aanzetten tenzij je daadwerkelijk onderzoek gaat doen anders krijg je veel grafieken in je files.
    # pylab.savefig("rand_walk"+str(n)+".png",bbox_inches ="tight", dpi = 600) # hiermee worden de grafieken in files opgeslagen
  
pylab.show()


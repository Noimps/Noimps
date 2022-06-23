# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:21:39 2022

@author: nemot
"""


import numpy
import random
import pylab

# n = aantal stappen
# begint altijd op (0,0)



        

def saw2d(n):
    gekozen = [0]
    stappen = []
    x = numpy.zeros(n + 1)
    y = numpy.zeros(n + 1)
    stap = x[0], y[0]
    stappen.append(stap)
    last = 0
    keuze = []
    keuzes = []
    i = 1
    elast = 0
    while i != n + 1:
        if last != 2:                                            #vorige stap mag niet links zijn
            for j in range(0, len(stappen)):
                R = int(x[i - 1] + 1), int(y[i - 1])            #bekijkt 1 stap naar rechts
                RR = int(x[i - 1] + 2), int(y[i - 1])           #bekijkt mogelijke stap daarna
                RD = int(x[i - 1] + 1), int(y[i - 1] - 1)       #bekijkt mogelijke stap daarna
                RH = int(x[i - 1] + 1), int(y[i - 1] + 1)       #bekijkt mogelijke stap daarna
                a = 3                                               # geeft aan hoeveel mogelijkheden er uiteindelijk over zijn
                
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
                    
                    if a >= 1:                                  #Deze aanpassen om gevoeligheid voor mogelijkheiden te versterken
                        
                        keuze.append(1)
                        break
        if last != 1:                                             #vorige stap mag niet rechts zijn
            for k in range(0, len(stappen)):
                b = 3                                           # geeft aan hoeveel mogelijkheden er uiteindelijk over zijn
                L = int(x[i - 1] - 1), int(y[i - 1])
                LL = int(x[i - 1] - 2), int(y[i - 1])           #bekijkt mogelijke stap daarna
                LD = int(x[i - 1] + 1), int(y[i - 1] - 1)       #bekijkt mogelijke stap daarna
                LH = int(x[i - 1] + 1), int(y[i - 1] + 1)       #bekijkt mogelijke stap daarna
                
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
                    if b >= 1:                                  #Deze aanpassen om gevoeligheid voor mogelijkheiden te versterken
                        
                        keuze.append(2)
                        break
        if last != 4:                                           #vorige stap mag niet omlaag zijn
            for l in range(0, len(stappen)):
                c = 3                                            # geeft aan hoeveel mogelijkheden er uiteindelijk over zijn
                H = int(x[i - 1]), int(y[i - 1] + 1)            #kijkt of stap naar omhoog mogelijk is
                HR = int(x[i - 1] + 1), int(y[i - 1] + 1)       #bekijkt mogelijke stap daarna
                HL = int(x[i - 1] - 1), int(y[i - 1] + 1)       #bekijkt mogelijke stap daarna
                HH = int(x[i - 1]), int(y[i - 1] + 2)           #bekijkt mogelijke stap daarna
                
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
                    if c >= 1:                                   #Deze aanpassen om gevoeligheid voor mogelijkheiden te versterken
                        keuze.append(3)
                        break
        if last != 3:                                           #vorige stap mag niet omhoog zijn
            for t in range(0, len(stappen)):
                d = 3                                           # geeft aan hoeveel mogelijkheden er uiteindelijk over zijn
                O = int(x[i - 1]), int(y[i - 1] - 1)            #kijkt of stap omlaag mogelijk is
                OR = int(x[i - 1] + 1), int(y[i - 1] - 1)       #bekijkt mogelijke stap daarna
                OL = int(x[i - 1] - 1), int(y[i - 1] - 1)       #bekijkt mogelijke stap daarna
                OO = int(x[i - 1]), int(y[i - 1] - 2)           #bekijkt mogelijke stap daarna
                    
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
        if i >= 3 and len(keuzes[-1]) == 1 and len(keuze) == 1:     # kijkt of er twee maal 1 stap mogelijk heid achter elkaar is
            i -= 1
            stappen.pop()                                       # pop de positie waarop len(keuzes[-1]) = 1 was
            keuzes.pop()                                         #pop de vorige keuze met 1 getal
            keuze = keuzes[-1]                                   #bekijk de vorige keuze met meer dan 1 getal opnieuw
            keuzes.pop()                                            #pop de keuzes die hij opnieuw bekijkt
            
            for j in range(0, len(keuze)):
                if keuze[j] == last:                              #haal het getal dat vorige keer in meerdere enkele keuzes achter elkaar liet ontstaan
                    keuze.pop(j)
                    keuzes.append(keuze)                            # zet de keuze die word bekeken terug zonder 
                    break                                           # break omdat de index anders error gaat geven na de pop en dit scheelt ook tijd
           
            if keuze == []:
                saw2d(n)
            stap = random.choice(keuze)
            last = stap                                                #nieuwe vorige keuze aan variabele last koppelen
            gekozen.pop()                                              # gooi de stap die net is verwijderd weg
            gekozen.append(stap)                                      #voeg de juiste nieuwe stap toe
            elast = gekozen[-2]                                        #een na laaste aan een na laatste keuze voor de backtrack koppelen
            
        elif keuze == [] and len(keuzes[-1]) > 1:
            
            keuze = keuzes[-1]                                          # bekijk vorige keuzes
            keuzes.pop()                                                #haal deze uit de lijst
            for j in range(0, len(keuze)):                              #loop tot je de vorige keuze vind
                if keuze[j] == last:                                    #haal het getal dat vorige keer in meerdere enkele keuzes achter elkaar liet ontstaan
                    keuze.pop(j)
                    keuzes.append(keuze)                                #   zet de keuze die word bekeken terug zonder 
                    break                                               # break omdat de index anders error gaat geven na de pop en dit scheelt ook tijd
            stap = random.choice(keuze)                                 #kies een van de overige keuzes
            gekozen.append(stap)                                        #nieuwe gekozen terugzetten
            elast = gekozen[-2]
            last = gekozen[-1]
            
        elif keuze == [] and len(keuzes[-1]) == 1:
            
            
            keuze = keuzes[-2]                                        # bekijk keuzes voor vorige keuzes
            keuzes.pop()                                             #haal de keuzes met len(1) uit de lijst
            for j in range(0, len(keuze)):
                if keuze[j] == elast:                               #haal de keuze die 2 keuzes geleden voor een error zorgde uit de lijst
                    keuze.pop(j)
                    keuzes.append(keuze)                            # zet de nieuwe lijst keuze die word bekeken terug in keuzes
                    break                                           # break omdat de index anders error gaat geven na de pop en dit scheelt ook tijd
            stap = random.choice(keuze)
            last = stap                                             #nieuwe vorige keuze aan variabele last koppelen
            gekozen.pop()                                           # gooi de stap die net is verwijderd weg
            gekozen.append(stap)                                    #voeg de juiste nieuwe stap toe
            elast = gekozen[-2]                                      #een na laaste aan een na laatste keuze voor de backtrack koppelen
            
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
    print(len(stappen))
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
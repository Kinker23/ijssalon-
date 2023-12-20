def mijn_functie_1():
     tabel = {
         2 : 4,
         4 : 16,
         10 : 100,
         12 : 144
     } 
     sleutels = [2, 4, 10, 12]
     resultaat = [tabel[sleutel] for sleutel in sleutels]
     return resultaat

def mijn_functie_2():
    tabel = {
        12.3 : [15,9, 36, 4],
        12.2 : [14,10,24,6],
        10.5: [15, 5, 50, 2],
        100.20: [120, 80, 2000, 5]
    }
    
    resultaat_2 = [tabel[sleutel] for sleutel in tabel]
    return resultaat_2


resultaat_1 = mijn_functie_1()
print(resultaat_1)
resultaat_2 = mijn_functie_2()
print(resultaat_2)

#
from algemene_functies import mijn_functie_2


def aanbieding_1(smaak,prijs,korting):
    nieuwe_prijs = prijs - (prijs * korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs} euro."

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw=0.0):
 totaal_inkomsten = sum(inkomsten)
 btw_bedrag = totaal_inkomsten * btw 
 totaal_met_btw = totaal_inkomsten + btw_bedrag
 return f"Het totaal van alle inkomsten van deze week is {totaal_met_btw} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
   
    
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09
totale_resultaat = inkomsten_totaal(inkomsten_per_dag, btw=btw_percentage)
print(totale_resultaat)
   
   

def laag_en_hoog(mijn_lijst):
 hoogste_waarde = max(mijn_lijst)
 laagste_waarde = min(mijn_lijst)
 return [hoogste_waarde, laagste_waarde]


inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]       
resultaat = laag_en_hoog(inkomsten_per_dag)
print("Hoogste en laagste waarden:", resultaat)


def gemiddelde(mijn_lijst):
    totaal_bedrag = sum(mijn_lijst)
    gemiddelde_inkomsten = totaal_bedrag / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten} euro."

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
resultaat = gemiddelde(inkomsten_per_dag)
print(resultaat)

def meervoudig(invoer_lijst):
 return laag_en_hoog(invoer_lijst)

getallen_lijst = [10, 5, 3, 2, 1, 2, 9]
resultaat = meervoudig(getallen_lijst)
print("Hoogste en laagste waarden:", resultaat)
    

def combinatie(invoer_lijst_2):
 korte_lijst = meervoudig(invoer_lijst_2)
 resultaat = meervoudig(invoer_lijst_2)
 return resultaat


getallen_lijst_2 = [8, 15, 3, 7, 12, 5, 10]
eindresultaat = combinatie(getallen_lijst_2)
print("Eindresultaat:", eindresultaat)
    

#
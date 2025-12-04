import math
#ho definito prima delle funzioni che calcolano i perimetri
def perimetroQ(l): #perimetro Quadrato
    perQ = l * 4
    return(perQ)

def ciconferenza(r): #circonferenza del Cerchio
    circC = 2 * math.pi * r
    return(circC)

def perimetroR(b,h): #perimetro Rettangolo
    perR = (2 * b) + (2 * h)
    return(perR)

print("Benvenuto/a nel calcolatore dei perimetri!\n")
a = 0
while a != 4: #ciclo per continuare a chiedere i perimetri finché non preme '4' per uscire
    a = float((input("\n\nQuale figura geometrica vuoi calcolare?\n 1 Quadrato\n 2 Cerchio\n 3 Rettangolo\n 4 Esci\n\n")))
    
    if a == 1:
            lQ = float(input("Inserisci la lunghezza del lato del quadrato: "))
            perimetroQuadrato = perimetroQ(lQ) #utilizzo della funzione definito sopra
            print(f"\nIl perimetro del quadrato di lato {lQ} è {perimetroQuadrato}")
    elif a == 2:
            rC = float(input("Inserisci la lunghezza del raggio del cerchio: "))
            circonferenzaCerchio = ciconferenza(rC) #utilizzo della funzione definito sopra
            print(f"\nLa circonferenza del cerchio di raggio {rC} è {circonferenzaCerchio}")
    elif a == 3:
            bR = float(input("Inserisci la lunghezza della base del rettangolo: "))
            aR = float(input("Inserisci l'altezza della base del rettangolo: "))
            perimetroRettangolo = perimetroR(bR, aR) #utilizzo della funzione definito sopra
            print(f"\nIl perimetro del rettangolo di base {bR} e di altezza {aR} è {perimetroRettangolo}")
    elif a == 4: #uscita dal programma
            print("\nAlla prossima!")
            break
    else: #se sceglie un numero al di fuori della lista
          print("\nQuesto numero non è presente nella lista, riprova.\n") 

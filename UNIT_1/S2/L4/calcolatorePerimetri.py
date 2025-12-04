import math
print("Benvenuto/a nel calcolatore dei perimetri!\n")
a = 0
while a != 4: #ciclo per continuare a chiedere i perimetri finché non preme '4' per uscire
    a = float((input("\n\nQuale figura geometrica vuoi calcolare?\n 1 Quadrato\n 2 Cerchio\n 3 Rettangolo\n 4 Esci\n\n")))

    if a == 1:
        latoQuadrato = float(input("Inserisci la lunghezza del lato del quadrato: "))
        perimetroQuadrato = latoQuadrato * 4 #calcolo del perimetro del quadrato
        print(f"\nIl perimetro del quadrato di lato {latoQuadrato} è {perimetroQuadrato}")
    elif a == 2:
            raggioCerchio = float(input("Inserisci la lunghezza del raggio del cerchio: "))
            ciconferenza = 2 * math.pi * raggioCerchio #calcolo della circonferenza 
            print(f"\nLa circonferenza del cerchio di raggio {raggioCerchio} è {ciconferenza}")
    elif a == 3:
            baseRettangolo = float(input("Inserisci la lunghezza della base del rettangolo: "))
            altezzaRettangolo = float(input("Inserisci l'altezza della base del rettangolo: "))
            perimetroRettangolo = 2 * baseRettangolo + 2 * altezzaRettangolo #calcolo del perimetro del rettangolo
            print(f"\nIl perimetro del rettangolo di base {baseRettangolo} e di altezza {altezzaRettangolo} è {perimetroRettangolo}")
    elif a == 4: #uscita dal programma
            print("\nAlla prossima!")
            break
    else: #se sceglie un numero al di fuori della lista
          print("\nQuesto numero non è presente nella lista, riprova.\n") 
    
  

import datetime

def assistente_virtuale(comando):
    if comando == "Qual è la data di oggi?".lower().strip():
        oggi = datetime.datetime.today()
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")
    elif comando == "Che ore sono?".lower().strip():
        ora_attuale = datetime.datetime.now().time()
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")
    elif comando == "Come ti chiami?".lower().strip():
        risposta = "Mi chiamo Assistente Virtuale"
    else:
        risposta = "Non ho capito la tua domanda."
    return risposta

print ('''
       Benvenuto/a! Sono un Assistente Virtuale. 
       
       Queste sono le funzionalità che posso offrire:
       - Qual è la data di oggi?
       - Che ore sono?
       - Come ti chiami
       Se vuoi uscire baste digitare "esci"
       ''')
while True:
    comando_utente = input("Cosa vuoi sapere? ")
    newComando = comando_utente.lower().strip()
    if newComando == "esci":
        print("Arrivederci!")
        break
    else:
        print(assistente_virtuale(newComando))

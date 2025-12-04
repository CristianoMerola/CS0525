figura=input("Inserisci una figura (quadrato, cerchio, rettangolo): ").lower()
if figura=="quadrato":
    lato=float(input("Inserisci il lato del quadrato: "))
    risultato_quadrato=lato*4
    print(f"Il perimetro del quadrato è: {risultato_quadrato}")
elif figura=="cerchio":
    raggio=float(input("Inserisci il raggio del cerchio: "))
    risultato_cerchio=2*3.14*raggio
    print(f"La circonferenza del cerchio è: {risultato_cerchio}")
elif figura=="rettangolo":
    base=float(input("Inserisci la base del rettangolo: "))
    altezza=float(input("Inserisci l'altezza del rettangolo: "))
    risultato_rettangolo=base*2+altezza*2
    print(f"Il perimetro del rettangolo è: {risultato_rettangolo}")
else:
    print("Nessuna della figure è nella lista.")
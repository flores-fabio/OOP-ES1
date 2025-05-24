from studente import Studente

studente1 = Studente("Mario" , "4B")
n = int(input("Inserisci il numero dei tuoi voti: "))
for i in range(n):
    voto = int(input("Inserisci il voto (tra 0 e 10):"))
    studente1.aggiungi_voto(voto)

print("Media dei voti:", studente1.media_voti())
print("Informazioni dello studente: ")
print(studente1.stampa_info())

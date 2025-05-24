class Studente:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.voti = []
    
    def aggiungi_voto(self, voto):
        if 0 <= voto <= 10:
            self.voti.append(voto)
        else: 
            print ("Voto non valido")
    
    def media_voti(self):
        if len(self.voti) ==0:
            return 0

        media = 0
        for i in range(len(self.voti)):
            media = media + self.voti[i]

        return media / len(self.voti)

    def stampa_info(self):
        return "Nome: " + self.nome + ", Classe: " + self.classe + ", Media" + str(self.media_voti()) + (", Numero di voti: ") + str(len(self.voti))
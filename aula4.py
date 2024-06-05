"Mantendo Status"

class Pokemon:
    def __init__(self, nome, ataque=False, defesa=False):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self):
        if self.ataque:
            print(f'{self.nome} ja esta atacando')
            return 
        else:
            self.ataque = True
            print(f'{self.nome} iniciou a fase de ataque')
            return 
        

    def defender(self):
        if self.defesa:
            print(f'{self.nome} ja esta defendendo')
            return 
        else:
            self.defesa = True
            print(f'{self.nome} iniciou a fase de defesa')
            return
        
lucario = Pokemon('Lucario')
lucario.atacar()
lucario.atacar()
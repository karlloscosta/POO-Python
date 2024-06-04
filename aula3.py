class Carta:
    def __init__(self, nome, defesa, ataque):
        self.nome = nome
        self.defesa = defesa
        self.ataque = ataque

    def atacar(self):
        print(f'{self.nome} esta atacando')

    def defender(self):
        print(f'{self.nome} foi posicionado em posição de defesa')

    def invocacar (self):
        print(f'{self.nome} foi invocado no campo de duelo')

MagoNegro = Carta('Mago Negro', 2500, 2100)
MagoNegro.invocacar()
MagoNegro.atacar()
MagoNegro.defender()

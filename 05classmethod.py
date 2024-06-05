class Cliente:
    
    def __init__ (self, nome, conta):
        self.nome = nome
        self.conta = conta
        
    @classmethod
    def criarcontacorrente (cls, nome):
        return cls(nome, 'Conta Corrente')
    
cliente = Cliente.criarcontacorrente('Karllos')
print(cliente.nome, cliente.conta)
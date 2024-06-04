'''self é um parâmetro usado em métodos dentro de uma 
classe para se referir à instância atual da classe. 
Ele permite que você acesse 
atributos e outros métodos dessa instância. 
É uma convenção de nomenclatura; 
você poderia nomeá-lo de outra forma, 
mas self é a convenção amplamente adotada.'''

class Pessoa:
    def __init__(self,nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Karllos','Eduardo')

print(p1.nome,p1.sobrenome)
class Personagem:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    def atacar(self): #subjetivo
        raise NotImplementedError("Método 'atacar' deve ser implementado nas subclasses")

    def receber_dano(self, quantidade):
        print(f"{self.nome} recebeu {quantidade} de dano")

# Exemplo de subclasse que estende a classe Personagem
class Guerreiro(Personagem):
    def atacar(self):
        print(f"{self.nome} atacou com sua espada!")

# Exemplo de subclasse que estende a classe Personagem
class Mago(Personagem):
    def atacar(self):
        print(f"{self.nome} lançou uma bola de fogo!")

# Criando instâncias de personagens
guerreiro = Guerreiro("Conan", 10)
mago = Mago("Gandalf", 12)

# Chamando métodos dos personagens
guerreiro.atacar()
mago.receber_dano(5)

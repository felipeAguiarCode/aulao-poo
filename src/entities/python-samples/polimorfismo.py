class Personagem:
    def __init__(self, nome):
        self.nome = nome

    def atacar(self):
        pass  # Método atacar genérico

class Guerreiro(Personagem):
    def atacar(self):
        print(f"{self.nome} atacou com sua espada!")

class Mago(Personagem):
    def atacar(self):
        print(f"{self.nome} lançou uma bola de fogo!")

class Paladin(Personagem):
    def atacar(self):
        print(f"{self.nome} atacou utilizando magia sagrada")



# Criando instâncias de personagens
guerreiro = Guerreiro("Conan")
mago = Mago("Gandalf")
joao = Paladin("joão")

guerreiro.atacar()
mago.atacar()
joao.atacar()

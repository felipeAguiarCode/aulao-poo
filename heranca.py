class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self):
        print(f"{self.nome} atacou!")

class Guerreiro(Personagem):
    def __init__(self, nome, vida, arma):
        super().__init__(nome, vida)
        self.arma = arma

    def usar_arma(self):
        print(f"{self.nome} usou {self.arma}!")

# class Mago(Personagem):
#     def __init__(self, nome, vida, magia):
#         super().__init__(nome, vida)
#         self.magia = magia

#     def lançar_magia(self):
#         print(f"{self.nome} lançou a magia {self.magia}!")

# Criando instâncias de personagens
guerreiro1 = Guerreiro("Cloud", 100, "Espada gigante")
guereiro2 = Guerreiro("Guts", 300, "Great Sword")

# mago1 = Mago("Gandalf", 80, "Bola de Fogo")

# Testando os métodos das subclasses
guerreiro1.atacar()
guerreiro1.usar_arma()

# mago1.atacar()
# mago1.lançar_magia()

class FantasmaPacman:
    def __init__(self, nome, cor, apelido):
        self.nome = nome
        self.cor = cor
        self.apelido = apelido

    def apresentar(self):
        print(f"Olá, eu sou o fantasma {self.nome}, conhecido como {self.apelido}, e minha cor é {self.cor}.")

    def mover(self, direcao):
        print(f"{self.nome} está se movendo para {direcao}.")

# Criando instâncias dos fantasmas do Pac-Man
blinky = FantasmaPacman("Blinky", "vermelho", "Perseguidor")
pinky = FantasmaPacman("Pinky", "rosa", "Acelerador")
inky = FantasmaPacman("Inky", "azul", "Trapaceiro")
clyde = FantasmaPacman("Clyde", "laranja", "Assustador")
rafael = FantasmaPacman("Rafael", "amarelo","rafitos")


# Apresentando os fantasmas
blinky.apresentar()
pinky.apresentar()
inky.apresentar()
clyde.apresentar()
rafael.apresentar()


# Movendo os fantasmas
blinky.mover("cima")
pinky.mover("baixo")
inky.mover("esquerda")
clyde.mover("direita")
rafael.mover("direita")
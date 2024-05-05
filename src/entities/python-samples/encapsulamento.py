class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def get_saldo(self):
        return self.__saldo  # Método getter para acessar o saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor  # Adiciona valor ao saldo

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor  # Subtrai valor do saldo

# Criando uma instância da classe ContaBancaria
conta = ContaBancaria(1000)

# Tentando acessar o saldo diretamente (erro devido ao encapsulamento)
# print(conta.__saldo)  # Isso geraria um erro de atributo

# Acessando o saldo por meio do método getter
print("Saldo atual:", conta.get_saldo())  # Saída: Saldo atual: 1000

# Depositando dinheiro na conta
conta.depositar(500)
print("Saldo após depósito:", conta.get_saldo())  # Saída: Saldo após depósito: 1500

# Sacando dinheiro da conta
conta.sacar(200)
print("Saldo após saque:", conta.get_saldo())  # Saída: Saldo após saque: 1300




from abc import ABC, abstractmethod


class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome


def andar(self):
    print(f"O animal {self.nome} andou")
    return


def emittir_som(self):
    pass


class Cachorro(Animal):
    def emitir_som(self):
        return "Au, Au"


class Gato(Animal):
    def emitir_som(self):
        return "Miau"


dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")


class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo


conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=-500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=200)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=2000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")


print("Exemplor de abstração")


class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return ("Carro ligando")

    def desligar(self):
        return ("Carro desligando")


carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())

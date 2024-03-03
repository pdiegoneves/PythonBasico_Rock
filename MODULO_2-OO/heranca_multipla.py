class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        print("Emitindo Som")
        pass


class Mamifero(Animal):
    def ammamentar(self):
        return f"{self.nome} está amamentando."


class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando."


class Morcego(Mamifero, Ave):
    def emitir_som(self):
        super().emitir_som()  # chama a implementação da classe mãe
        return "Morcegos emitem sons ultrasônicos"


sanguinho = Morcego(nome="Sanguinho")
print(sanguinho.nome)
print(sanguinho.emitir_som())
print(sanguinho.voar())

# @classmethod
# @staticmethod

class MinhaClasse:

    valor = 10

    def __init__(self, nome) -> None:
        self.nome = nome

    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome} valor = {self.valor}"

    @classmethod
    def metodo_classe(cls):
        return f"Metodo da classe chamado para valor = {cls.valor}"

    @staticmethod
    def metodo_estatico():
        return "Método estático chamado"


obj = MinhaClasse(nome="Classe exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

from abc import ABC, abstractmethod

class Armazenador(ABC):
    @abstractmethod
    def salvar(self, dado):
        pass


class ArmazenadorArquivo(Armazenador):
    def __init__(self, caminho):
        self.caminho = caminho

    def salvar(self, dado):
        print(f"[Arquivo] Salvando '{dado}' no arquivo: {self.caminho}")


class ArmazenadorBanco(Armazenador):
    def __init__(self, banco):
        self.banco = banco

    def salvar(self, dado):
        print(f"[Banco] Salvando '{dado}' no banco: {self.banco}")
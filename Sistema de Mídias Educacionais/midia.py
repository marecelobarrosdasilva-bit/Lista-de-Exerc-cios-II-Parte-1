from abc import ABC, abstractmethod

class Midia(ABC):
    def __init__(self, titulo, duracao):
        self._titulo = ""
        self._duracao = 0

        self.titulo = titulo
        self.duracao = duracao

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        if isinstance(novo_titulo, str) and novo_titulo.strip() != "":
            self._titulo = novo_titulo
        else:
            print("Erro: título inválido.")

    @property
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self, nova_duracao):
        if isinstance(nova_duracao, (int, float)) and nova_duracao >= 0:
            self._duracao = nova_duracao
        else:
            print("Erro: duração inválida.")

    def mostrar_info(self):
        print(f"Título: {self.titulo} | Duração: {self.duracao} min")

    @abstractmethod
    def reproduzir(self):
        pass
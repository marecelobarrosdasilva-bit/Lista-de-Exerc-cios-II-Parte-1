from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, cpf):
        self._nome = ""
        self._cpf = ""

        self.nome = nome
        self.cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip() != "":
            self._nome = novo_nome
        else:
            print("Erro: nome inválido.")

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        if isinstance(novo_cpf, str) and novo_cpf.strip() != "":
            self._cpf = novo_cpf
        else:
            print("Erro: CPF inválido.")

    def mostrar_dados(self):
        print(f"Nome: {self.nome} | CPF: {self.cpf}")

    @abstractmethod
    def calcular_pagamento(self):
        pass
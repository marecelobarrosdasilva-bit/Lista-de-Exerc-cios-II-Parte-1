class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f"{funcionario.nome} foi adicionado à empresa {self.nome}.")

    def listar_funcionarios(self):
        print(f"\nFuncionários de {self.nome}")
        for funcionario in self.funcionarios:
            funcionario.mostrar_dados()

    def mostrar_folha_pagamento(self):
        print(f"\nFolha de pagamento de {self.nome}")
        total = 0
        for funcionario in self.funcionarios:
            pagamento = funcionario.calcular_pagamento()
            total += pagamento
            print(f"{funcionario.nome}: R$ {pagamento:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")
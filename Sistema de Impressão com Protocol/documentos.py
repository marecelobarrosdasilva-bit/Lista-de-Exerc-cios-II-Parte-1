class Boleto:
    def __init__(self, codigo, valor):
        self.codigo = codigo
        self.valor = valor

    def imprimir(self):
        print(f"[Boleto] Código: {self.codigo} | Valor: R$ {self.valor:.2f}")


class Etiqueta:
    def __init__(self, destinatario, endereco):
        self.destinatario = destinatario
        self.endereco = endereco

    def imprimir(self):
        print(f"[Etiqueta] Para: {self.destinatario} | "
              f"Endereço: {self.endereco}")


class RelatorioSimples:
    def __init__(self, titulo):
        self.titulo = titulo

    def imprimir(self):
        print(f"[Relatório] Título: {self.titulo}")
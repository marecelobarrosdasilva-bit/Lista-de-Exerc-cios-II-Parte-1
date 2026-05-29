class ArmazenadorNuvem:
    def __init__(self, servico):
        self.servico = servico

    def salvar(self, dado):
        print(f"[Nuvem] Salvando '{dado}' no serviço: {self.servico}")
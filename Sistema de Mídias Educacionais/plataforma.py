class Plataforma:
    def __init__(self, nome):
        self.nome = nome
        self.midias = []

    def adicionar_midia(self, midia):
        self.midias.append(midia)
        print(f"'{midia.titulo}' adicionado à plataforma {self.nome}.")

    def listar_midias(self):
        print(f"\n Mídias disponíveis em {self.nome}")
        for midia in self.midias:
            midia.mostrar_info()

    def reproduzir_todas(self):
        print(f"\nReproduzindo todas as mídias de {self.nome}")
        for midia in self.midias:
            midia.reproduzir()
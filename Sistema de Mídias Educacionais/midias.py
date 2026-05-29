from midia import Midia

class Video(Midia):
    def __init__(self, titulo, duracao, resolucao):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def reproduzir(self):
        print(f"[Vídeo] Reproduzindo '{self.titulo}' em {self.resolucao}.")


class Podcast(Midia):
    def __init__(self, titulo, duracao, apresentador):
        super().__init__(titulo, duracao)
        self.apresentador = apresentador

    def reproduzir(self):
        print(f"[Podcast] Reproduzindo '{self.titulo}' "
              f"com {self.apresentador}.")


class TextoNarrado(Midia):
    def __init__(self, titulo, duracao, idioma):
        super().__init__(titulo, duracao)
        self.idioma = idioma

    def reproduzir(self):
        print(f"[Texto Narrado] Reproduzindo '{self.titulo}' "
              f"no idioma {self.idioma}.")
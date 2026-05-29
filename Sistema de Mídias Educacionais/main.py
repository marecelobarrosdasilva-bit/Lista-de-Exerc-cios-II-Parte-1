from midias import Video, Podcast, TextoNarrado
from plataforma import Plataforma

plataforma = Plataforma("SI.Play")

v1 = Video("Introdução à POO", 15.0, "1080p")
p1 = Podcast("Falando sobre programação", 45.0, "Prof. Alternei")
t1 = TextoNarrado("Capítulo 1 - Introdução", 10.0, "Português")

plataforma.adicionar_midia(v1)
plataforma.adicionar_midia(p1)
plataforma.adicionar_midia(t1)

plataforma.listar_midias()
plataforma.reproduzir_todas()

# Perguntas:

# Qual é a classe abstrata do sistema?
# R: Midia, pois herda de ABC e declara reproduzir() com @abstractmethod.

# Onde aparece a hierarquia?
# R: Video, Podcast e TextoNarrado herdam de Midia usando super().__init__() para reaproveitar o construtor base.

# Onde aparece o polimorfismo?
# R: No método reproduzir_todas() da classe Plataforma, onde o for chama midia.reproduzir() em cada objeto da lista,
#  e cada subclasse executa sua versão específica.

# Por que Midia não deveria ser instanciada diretamente?
# R: Porque ela é genérica demais para ter uma reprodução concreta. 
# O @abstractmethod garante que o Python bloqueie isso com TypeError, obrigando as subclasses a definirem o comportamento real.
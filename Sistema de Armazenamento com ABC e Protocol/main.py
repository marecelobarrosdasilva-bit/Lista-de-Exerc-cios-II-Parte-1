from armazenador import ArmazenadorArquivo, ArmazenadorBanco
from nuvem import ArmazenadorNuvem
from salvamento import executar_salvamento_formal, executar_salvamento_flexivel

a1 = ArmazenadorArquivo("dados/relatorio.txt")
a2 = ArmazenadorBanco("PostgreSQL")
a3 = ArmazenadorNuvem("Amazon S3")

print("Parte A: salvamento formal (ABC)\n")
executar_salvamento_formal(a1, "Relatório Maio 2025")
executar_salvamento_formal(a2, "Relatório Maio 2025")

print("\nParte B: salvamento flexível (Protocol)\n")
executar_salvamento_flexivel(a1, "Backup diário")
executar_salvamento_flexivel(a2, "Backup diário")
executar_salvamento_flexivel(a3, "Backup diário")

print("\nObservação: nuvem NÃO funciona no formal\n")
print(f"ArmazenadorNuvem herda de Armazenador? "
      f"{issubclass(ArmazenadorNuvem, ArmazenadorArquivo.__class__.__bases__[0])}")


# Perguntas:
# Em qual parte há contrato por herança?
# R: Na Parte A, com ABC. ArmazenadorArquivo e ArmazenadorBanco herdam
#    obrigatoriamente de Armazenador e são obrigados a implementar salvar().

# Em qual parte há contrato estrutural?
# R: Na Parte B, com Protocol. ArmazenadorNuvem não herda de nada, mas é
#    compatível com Salvavel por possuir o método salvar().

# Qual abordagem é mais rígida?
# R: ABC, pois exige herança explícita e bloqueia a instanciação se o
#    método abstrato não for implementado.

# Qual abordagem é mais flexível?
# R: Protocol, pois aceita qualquer objeto que tenha o método esperado,
#    independentemente de sua hierarquia ou origem.

# Em qual situação ABC faz mais sentido? E em qual Protocol faz mais sentido?
# R: ABC faz mais sentido quando existe uma família de classes relacionadas
#    com estrutura e comportamento em comum, como diferentes tipos de
#    funcionários ou formas geométricas.
#    Protocol faz mais sentido quando se quer aceitar objetos de origens
#    diversas sem forçar herança, como integrar classes de bibliotecas
#    externas ou sistemas que não podem ser alterados.
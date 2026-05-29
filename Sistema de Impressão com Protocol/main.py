from documentos import Boleto, Etiqueta, RelatorioSimples
from impressao import processar_impressao

b1 = Boleto("2024.0001", 150.00)
e1 = Etiqueta("Marcelo Barros da Silva", "Rua Isaac Peres, 2841 - Itacoatiara/AM")
r1 = RelatorioSimples("Relatório de Vendas - Maio/2025")

print("Processando impressões\n")
processar_impressao(b1)
processar_impressao(e1)
processar_impressao(r1)


#  Perguntas:
# Onde está o contrato nesse caso?
# R: Na classe Imprimivel, definida com Protocol. Ela declara que qualquer objeto compatível deve ter o método imprimir().

# Por que as classes funcionam sem herdar explicitamente do protocolo?
# R: Porque Protocol usa verificação estrutural. O Python não exige herança explícita; ele verifica se o objeto tem os métodos esperados, 
# independentemente de sua hierarquia.

# Esse caso se aproxima mais de ABC ou de duck typing?
# R: De duck typing. Não há herança obrigatória nem erro em tempo de instanciação. O que importa é que o objeto tenha o método imprimir()
#  independentemente de qual classe ele pertence.

# Qual a principal diferença entre esse caso e o da Questão 3?
# R: Na Questão 3, Notificador é uma ABC e a herança é obrigatória. O Python bloqueia subclasses que não implementem o método abstrato. 
# Aqui, com Protocol, as classes são completamente independentes entre  si e nenhuma herança é exigida; o contrato é verificado apenas
#pela estrutura do objeto.
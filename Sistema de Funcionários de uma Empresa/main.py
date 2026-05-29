from funcionarios import FuncionarioAssalariado, FuncionarioHorista, FuncionarioComissionado
from empresa import Empresa

empresa = Empresa("Tech Amazônia")

f1 = FuncionarioAssalariado("Ana Siva", "111.111.111-11", 4500.00)
f2 = FuncionarioHorista("Marcelo Barros", "222.222.222-22", 160, 25.00)
f3 = FuncionarioComissionado("Gustavo Souza", "333.333.333-33", 20000.00, 10)

empresa.adicionar_funcionario(f1)
empresa.adicionar_funcionario(f2)
empresa.adicionar_funcionario(f3)

empresa.listar_funcionarios()
empresa.mostrar_folha_pagamento()

# Perguntas:
# Qual é a superclasse da hierarquia?
# R: Funcionario, classe abstrata que herda de ABC e define o contrato da hierarquia.

# Quais são as subclasses?
# R: FuncionarioAssalariado, FuncionarioHorista e FuncionarioComissionado.

# Onde ocorre sobrescrita?
# R: Cada subclasse sobrescreve calcular_pagamento() com sua própria lógica:salário fixo, horas * valor_hora, ou total_vendas * percentual.

# Onde ocorre polimorfismo?
# R: Em mostrar_folha_pagamento(), onde o for chama calcular_pagamento() em cada funcionário e cada objeto executa sua versão específica do método.

# Qual a vantagem de usar ABC nesse caso?
# R: O @abstractmethod garante que nenhuma subclasse seja criada sem implementar calcular_pagamento(), evitando funcionários sem lógica de pagamento definida.
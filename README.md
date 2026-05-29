# Lista de Exercícios II - Parte 1
## Programação Orientada a Objetos — Python

Repositório criado para armazenar as resoluções dos exercícios práticos
da disciplina de Programação Orientada a Objetos (POO), aplicando
hierarquia de classes, polimorfismo e classes abstratas.

---

## Requisitos

- Python 3.10 ou superior
- Nenhuma biblioteca externa necessária

---

## Como executar

1. Clone o repositório:
   git clone https://github.com/marecelobarrosdasilva-bit/Lista-de-Exerc-cios-II-Parte-1.git

2. Acesse a pasta da questão desejada:
   cd "Sistema de Mídias Educacionais"

3. Execute o arquivo principal:
   python main.py

---

## Estrutura do Repositório

Lista-de-Exerc-cios-II-Parte-1/
│
├── Sistema de Mídias Educacionais/
│   ├── midia.py            # Classe abstrata Midia
│   ├── midias.py           # Subclasses Video, Podcast e TextoNarrado
│   ├── plataforma.py       # Classe Plataforma
│   └── main.py             # Arquivo principal de testes
│
├── Sistema de Funcionários de uma Empresa/
│   ├── funcionario.py      # Classe abstrata Funcionario
│   ├── funcionarios.py     # Subclasses Assalariado, Horista e Comissionado
│   ├── empresa.py          # Classe Empresa
│   └── main.py             # Arquivo principal de testes
│
├── Sistema de Notificações com ABC/
│   ├── notificador.py      # Classe abstrata Notificador
│   ├── notificadores.py    # Subclasses Email, SMS e App
│   ├── central_notificacoes.py  # Classe CentralNotificacoes
│   └── main.py             # Arquivo principal de testes
│
├── Sistema de Impressão com Protocol/
│   ├── imprimivel.py       # Protocol Imprimivel
│   ├── documentos.py       # Classes Boleto, Etiqueta e RelatorioSimples
│   ├── impressao.py        # Função processar_impressao()
│   └── main.py             # Arquivo principal de testes
│
├── Sistema de Armazenamento com ABC e Protocol/
│   ├── armazenador.py      # Classe abstrata Armazenador e subclasses
│   ├── salvavel.py         # Protocol Salvavel
│   ├── nuvem.py            # Classe ArmazenadorNuvem
│   ├── salvamento.py       # Funções de salvamento
│   └── main.py             # Arquivo principal de testes
│
└── README.md

---

## Questões implementadas

### Questão 1 — Sistema de Mídias Educacionais
Hierarquia com classe abstrata Midia e subclasses Video, Podcast
e TextoNarrado. Demonstra polimorfismo no método reproduzir_todas()
da classe Plataforma.

### Questão 2 — Sistema de Funcionários de uma Empresa
Hierarquia com classe abstrata Funcionario e subclasses
FuncionarioAssalariado, FuncionarioHorista e FuncionarioComissionado.
Demonstra polimorfismo no método mostrar_folha_pagamento()
da classe Empresa.

### Questão 3 — Sistema de Notificações com ABC
Hierarquia com classe abstrata Notificador e subclasses
NotificadorEmail, NotificadorSMS e NotificadorApp.
Demonstra polimorfismo no método enviar_para_todos()
da classe CentralNotificacoes.

### Questão 4 — Sistema de Impressão com Protocol
Uso de Protocol para contrato estrutural sem herança obrigatória.
Classes Boleto, Etiqueta e RelatorioSimples implementam imprimir()
sem herdar de Imprimivel.

### Questão 5 — Sistema de Armazenamento com ABC e Protocol
Comparação entre ABC e Protocol no mesmo problema.
Parte A usa herança formal com Armazenador.
Parte B usa contrato estrutural com Salvavel.

---

## Conceitos aplicados

- Classes abstratas com ABC e @abstractmethod
- Protocol para contratos estruturais
- Polimorfismo e ligação dinâmica
- Herança e sobrescrita de métodos
- Encapsulamento com properties e setters

---

## Autor

Marcelo Barros da Silva
Universidade Federal do Amazonas — UFAM
Disciplina: Programação Orientada a Objetos

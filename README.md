# Python System Tool

Ferramenta de diagnóstico e monitoramento de sistemas desenvolvida em Python. O projeto oferece uma interface de linha de comando para consultar informações do computador, acompanhar o uso de recursos e verificar o armazenamento disponível.

## Funcionalidades

- Exibição de informações do computador e do sistema operacional.
- Consulta do uso e da disponibilidade da memória RAM.
- Verificação da capacidade e do espaço utilizado em disco.
- Identificação do nome do computador e do usuário conectado.
- Exibição da versão do Python e da arquitetura do sistema.

## Tecnologias utilizadas

- **Python 3:** linguagem principal do projeto.
- **psutil:** biblioteca para consulta de recursos do sistema e monitoramento de processos.
- **Git:** controle de versão do código-fonte.
- **GitHub:** hospedagem e gerenciamento do repositório.

## Requisitos

- Python 3.10 ou superior.
- pip para instalação de dependências.
- Windows, Linux ou outro sistema operacional compatível.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/JVRochaMaciel/PythonSystemTool.git
```

Acesse a pasta do projeto:

```bash
cd PythonSystemTool
```

Instale a dependência necessária:

```bash
python -m pip install psutil
```

## Execução

Execute o programa a partir da pasta do projeto:

```bash
python main.py
```

No Windows, também é possível utilizar:

```bash
py main.py
```

Após a execução, será apresentado um menu interativo com as opções de diagnóstico disponíveis.

## Estrutura do projeto

```text
PythonSystemTool/
├── main.py
└── README.md
```

## Melhorias planejadas

- [ ] Monitoramento do uso da CPU em tempo real.
- [ ] Listagem de processos com maior consumo de memória.
- [ ] Geração automática de relatórios do sistema.
- [ ] Aprimoramento da interface do terminal.
- [ ] Implementação de novas ferramentas de diagnóstico.

## Objetivo

O projeto tem como objetivo aprimorar conhecimentos em Python, explorar recursos de monitoramento do sistema operacional e desenvolver habilidades práticas com controle de versão e gerenciamento de código.

## Autor

**João Vitor Rocha Maciel**

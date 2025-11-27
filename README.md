Relatório Automático de Vendas – Lanchonete (Python + Pandas)
Este projeto é um sistema em Python que lê os dados das maquininhas de cartão de uma lanchonete, faz o tratamento das informações, calcula indicadores importantes (KPIs), gera gráficos e monta automaticamente um relatório em PDF com os resultados.

O objetivo é facilitar a análise de vendas, ajudando o dono da lanchonete a entender melhor o desempenho do negócio sem precisar fazer contas manualmente.

Funcionalidades principais
Leitura automática dos arquivos CSV das maquininhas
Padronização e limpeza dos dados (tratamento de colunas, tipos e datas)
CáRelatório Automático de Vendas – Lanchonete (Python + Pandas)

Este projeto consiste em um sistema desenvolvido em Python para leitura, tratamento e análise automática dos dados de vendas de uma lanchonete, a partir dos arquivos CSV exportados pelas maquininhas de cartão. O programa calcula indicadores importantes (KPIs), gera gráficos e cria automaticamente um relatório completo em PDF com os resultados.

O objetivo é permitir que o proprietário tenha uma visão clara e rápida do desempenho do negócio, evitando cálculos manuais e facilitando a tomada de decisões.

Funcionalidades Principais
1. Leitura automática dos dados

Importação dos arquivos CSV das maquininhas.

Padronização dos nomes das colunas, independente do formato original.

Conversão de tipos, limpeza de dados e tratamento de valores inconsistentes.

2. Cálculo dos KPIs (Indicadores de Desempenho)

O sistema calcula automaticamente:

Faturamento total

Quantidade total de itens vendidos

Ticket médio por item

Produto com maior faturamento

Produto mais vendido em quantidade

Agrupamento das vendas:

Por produto

Por dia

3. Geração de gráficos (dashboard)

O programa utiliza o Matplotlib para gerar gráficos que auxiliam na visualização das vendas:

Top 10 produtos por faturamento

Top 10 produtos por quantidade vendida

Faturamento diário

Os gráficos são salvos como arquivos PNG.

4. Criação do relatório em PDF

O relatório final é montado utilizando a biblioteca FPDF e contém:

Cabeçalho com título e data de geração

KPIs consolidados

Texto explicativo sobre o desempenho

Gráficos integrados

Observações relevantes sobre o comportamento das vendas

Estrutura do Projeto
relatorio-vendas-python/
│
├── main.py                 # Arquivo principal do sistema
├── maquina1.csv            # Exemplo de arquivo da maquininha 1 (opcional)
├── maquina2.csv            # Exemplo de arquivo da maquininha 2 (opcional)
├── relatorios/             # Pasta onde serão salvos PDFs e gráficos
│
└── README.md               # Documentação do projeto

Observação: Caso a pasta relatorios/ não exista, ela será criada automaticamente pelo sistema.

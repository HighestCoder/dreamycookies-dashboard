Relatório Automático de Vendas – Lanchonete (Python + Pandas)
Este projeto é um sistema em Python que lê os dados das maquininhas de cartão de uma lanchonete, faz o tratamento das informações, calcula indicadores importantes (KPIs), gera gráficos e monta automaticamente um relatório em PDF com os resultados.

O objetivo é facilitar a análise de vendas, ajudando o dono da lanchonete a entender melhor o desempenho do negócio sem precisar fazer contas manualmente.

Funcionalidades principais
Leitura automática dos arquivos CSV das maquininhas
Padronização e limpeza dos dados (tratamento de colunas, tipos e datas)
Cálculo dos principais indicadores de vendas:
Faturamento total
Quantidade total de itens vendidos
Ticket médio por item
Produto com maior faturamento
Produto mais vendido em quantidade
Agrupamento das vendas por produto e por dia
Geração de três gráficos:
Top 10 produtos por faturamento
Top 10 produtos por quantidade vendida
Faturamento diário
Criação automática de um relatório em PDF com:
Título e data
KPIs principais
Pequeno feedback interpretativo
Gráficos integrados
Estrutura do projeto (recomendada)
relatorio-vendas-python/
│
├── main.py                 # Código principal do sistema
├── maquina1.csv            # Arquivo de exemplo da maquininha 1 (opcional)
├── maquina2.csv            # Arquivo de exemplo da maquininha 2 (opcional)
├── relatorios/             # Pasta onde serão salvos PDFs e gráficos
│
└── README.md               # Este arquivo
Obs.: Se a pasta relatorios/ não existir, o próprio código cria automaticamente.

🛠 Tecnologias utilizadas
Python 3

Pandas – manipulação e análise dos dados

Matplotlib – geração dos gráficos

FPDF – criação do relatório em PDF

Datetime / OS – organização de datas e arquivos

▶ Como executar o projeto
Coloque os arquivos maquina1.csv e maquina2.csv na mesma pasta do main.py.

Os arquivos devem ter, pelo menos, as colunas: Produto, Quantidade, Valor e, se possível, Data.

Certifique-se de que as bibliotecas necessárias estejam instaladas:

bash
Copiar código
pip install pandas matplotlib fpdf
Execute o arquivo principal:

bash
Copiar código
python main.py
Ao final da execução, será exibida no terminal a mensagem informando o caminho do PDF gerado, por exemplo:

text
Copiar código
Processo concluído!
Arquivo PDF gerado em: relatorios/relatorio_vendas_20251126_092346.pdf
Abra a pasta relatorios/ e visualize o PDF com os gráficos e indicadores.

## Visão geral do funcionamento
De forma resumida, o fluxo do sistema é:

Preparação: garante que a pasta de relatórios exista.

Carregamento: lê os CSVs das maquininhas, padroniza nomes de colunas e limpa os dados.

Análise: calcula os KPIs e agrupa as vendas por produto e por dia.

Dashboard: gera os gráficos em PNG usando o Matplotlib.

Relatório: monta um PDF com os KPIs, texto explicativo e gráficos integrados.

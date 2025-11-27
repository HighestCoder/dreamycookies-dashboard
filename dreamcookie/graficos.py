import os
from datetime import datetime
import pandas as pd 
import matplotlib.pyplot as plt 
from fpdf import FPDF 

CSV_PATHS = ["maquina1.csv", "maquina2.csv"]#lista dos arquivos de entrada (duas maquininhas).
OUTPUT_DIR = "relatorios"#pasta onde vão ficar gráficos + PDF
DATE_FORMAT = "%Y-%m-%d"#padrão de data para conversão
ESTOQUE_PATH = "estoque.csv"

def ensure_output_dir(): #essa função garante que a pasta relatorios exista. 
    os.makedirs(OUTPUT_DIR, exist_ok=True) #se não existir, ele cria. Isso evita erro na hora de salvar os arquivos.

def gerar_graficos(kpis: dict, ts: str) -> dict: #recebe os KPIs e cria arquivos PNG com os gráficos. O timestamp garante que os arquivos nunca se sobreponham

    paths = {} #Cria um dicionário vazio que vai armazenar os caminhos dos gráficos gerados.

    vendas_prod = kpis["vendas_por_produto"].head(10) #Seleciona os top 10 produtos
    plt.figure(figsize=(9, 4)) #abre uma nova figura (tamanho 9x4)
    vendas_prod.plot(kind="bar") #plota um gráfico de barras
    plt.title("Faturamento por produto (Top 10)")
    plt.xlabel("Produto")
    plt.ylabel("Faturamento (R$)")
    plt.tight_layout() #ajusta layout para evitar texto cortado
    graf1 = os.path.join(OUTPUT_DIR, f"graf_vendas_por_produto_{ts}.png") #Define o caminho (nome do arquivo)
    plt.savefig(graf1) #salva o gráfico como PNG
    plt.close() #fecha a figura para liberar memória
    paths["graf_vendas_por_produto"] = graf1 #armazena o caminho no dicionário

    #uma cópia do anterior, mas usando a métrica de quantidade vendida, não o faturamento.
    qtd_prod = kpis["qtd_por_produto"].head(10) #Seleciona os top 10 produtos
    plt.figure(figsize=(9, 4))#abre uma nova figura (tamanho 9x4)
    qtd_prod.plot(kind="bar")#plota um gráfico de barras
    plt.title("Quantidade vendida por produto (Top 10)")
    plt.xlabel("Produto")
    plt.ylabel("Quantidade")
    plt.tight_layout()#ajusta layout para evitar texto cortado
    graf2 = os.path.join(OUTPUT_DIR, f"graf_qtd_por_produto_{ts}.png")#Define o caminho (nome do arquivo)
    plt.savefig(graf2) #salva o gráfico como PNG
    plt.close() #fecha a figura para liberar memória
    paths["graf_qtd_por_produto"] = graf2 #armazena o caminho no dicionário

    #esse gráfico mostra o faturamento diário. Ele ajuda a identificar dias mais fortes e mais fracos, facilitando decisões sobre estoque, produção e demanda.
    vendas_dia = kpis["vendas_por_dia"]
    plt.figure(figsize=(9, 4))
    #.plot() → cria um gráfico de linha.
    vendas_dia.plot(marker="o") #marker="o" → coloca bolinhas em cada ponto
    plt.title("Faturamento diário") #titulo 
    plt.xlabel("Data") #eixo X → datas
    plt.ylabel("Faturamento (R$)") #eixo Y → quanto foi faturado no dia
    plt.xticks(rotation=45) #rotacionar em 45 graus, deixa legível. 
    plt.tight_layout() #ajusta margens automaticamente para evitar cortar texto.
    graf3 = os.path.join(OUTPUT_DIR, f"graf_vendas_por_dia_{ts}.png") #monta o nome do arquivo (com timestamp para não repetirem)
    plt.savefig(graf3) #salva o gráfico PNG
    plt.close() #fecha a figura para liberar memória
    paths["graf_vendas_por_dia"] = graf3 #armazena o caminho no dicionário

    return paths

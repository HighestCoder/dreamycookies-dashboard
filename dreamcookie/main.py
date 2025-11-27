import os
from datetime import datetime
import pandas as pd 
import matplotlib.pyplot as plt 
from fpdf import FPDF 
from dados import carregar_dados, CSV_PATHS, OUTPUT_DIR
from calculos import calcular_kpis, calcular_lucro
from graficos import gerar_graficos
from gerarpdf import gerar_pdf
from estoque import carregar_estoque
from datetime import datetime

CSV_PATHS = ["maquina1.csv", "maquina2.csv"]#lista dos arquivos de entrada (duas maquininhas).
OUTPUT_DIR = "relatorios"#pasta onde vão ficar gráficos + PDF
DATE_FORMAT = "%Y-%m-%d"#padrão de data para conversão
ESTOQUE_PATH = "estoque.csv"

def ensure_output_dir(): #essa função garante que a pasta relatorios exista. 
    os.makedirs(OUTPUT_DIR, exist_ok=True) #se não existir, ele cria. Isso evita erro na hora de salvar os arquivos.


def main():
    ensure_output_dir()

    print("Carregando dados das maquininhas...")
    df = carregar_dados(CSV_PATHS)

    print("Calculando indicadores...")
    kpis = calcular_kpis(df)

    # NOVO: carregar estoque e calcular lucro
    print("Carregando dados de estoque/custos...")
    df_estoque = carregar_estoque(ESTOQUE_PATH)

    print("Calculando lucro...")
    dados_lucro = calcular_lucro(df, df_estoque)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    print("Gerando gráficos (dashboard)...")
    graf_paths = gerar_graficos(kpis, ts)

    print("Gerando relatório em PDF...")
    pdf_path = gerar_pdf(kpis, graf_paths, ts, dados_lucro)

    dados_lucro = calcular_lucro(df, df_estoque)

    print("\n Processo concluído!")
    print("Arquivo PDF gerado em:", pdf_path)

if __name__ == "__main__":
    main()

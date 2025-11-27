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

def gerar_pdf(kpis: dict, graf_paths: dict, ts: str, dados_lucro: dict | None = None) -> str:
    pdf_path = os.path.join(OUTPUT_DIR, f"relatorio_vendas_{ts}.pdf") #monta o caminho onde o PDF será salvo.

    pdf = FPDF() #cria um objeto PDF.
    pdf.set_auto_page_break(auto=True, margin=15) #habilita quebra automática de página
    pdf.add_page() #cria a primeira página

    # Título
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Relatório de Vendas - Lanchonete", ln=True, align="C")
    pdf.ln(4)

    # Data de geração
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}", ln=True)
    pdf.ln(4)

    # KPIs principais
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "Resumo Geral:", ln=True)
    pdf.set_font("Arial", "", 11)

    #extraindo os KPIs para variáveis
    fat = kpis["faturamento_total"]
    qtd = kpis["quantidade_total"]
    ticket = kpis["ticket_medio"]
    top_valor = kpis["top_produto_valor"]
    top_qtd = kpis["top_produto_qtd"]

    lucro_total = None
    produto_mais_lucrativo = None

    if dados_lucro is not None:
        lucro_total = dados_lucro.get("lucro_total")
        lucro_por_produto = dados_lucro.get("lucro_por_produto")

        if lucro_por_produto is not None and not lucro_por_produto.empty:
            produto_mais_lucrativo = lucro_por_produto.idxmax()


    #principais indicadores de vendas: faturamento, quantidade, ticket médio e os produtos destaque.
    #cada KPI vira uma linha do PDF
    pdf.cell(0, 7, f"Faturamento total: R$ {fat:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), ln=True)
    pdf.cell(0, 7, f"Quantidade total de itens vendidos: {qtd}", ln=True)
    pdf.cell(0, 7, f"Ticket médio por item: R$ {ticket:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), ln=True)
    pdf.cell(0, 7, f"Produto com maior faturamento: {top_valor}", ln=True)
    pdf.cell(0, 7, f"Produto mais vendido em quantidade: {top_qtd}", ln=True)

    if lucro_total is not None:
        pdf.cell(
            0,
            7,
            f"Lucro total estimado: R$ {lucro_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            ln=True,
        )

    if produto_mais_lucrativo is not None:
        pdf.cell(0, 7, f"Produto mais lucrativo: {produto_mais_lucrativo}", ln=True)

    # gráfico 1
    if os.path.exists(graf_paths["graf_vendas_por_produto"]):#verifica se o arquivo existe
        pdf.ln(4)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 8, "Gráfico - Faturamento por produto (Top 10)", ln=True)
        pdf.image(graf_paths["graf_vendas_por_produto"], w=180)

    pdf.add_page()

    # gráfico 2
    if os.path.exists(graf_paths["graf_qtd_por_produto"]):
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 8, "Gráfico - Quantidade vendida por produto (Top 10)", ln=True)
        pdf.image(graf_paths["graf_qtd_por_produto"], w=180)
        pdf.ln(4)

    # gráfico 3
    if os.path.exists(graf_paths["graf_vendas_por_dia"]): 
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 8, "Gráfico - Faturamento diário", ln=True)
        pdf.image(graf_paths["graf_vendas_por_dia"], w=180)

    pdf.output(pdf_path)
    return pdf_path
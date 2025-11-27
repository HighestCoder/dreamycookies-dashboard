import os
from datetime import datetime
import pandas as pd 
import matplotlib.pyplot as plt 
from fpdf import FPDF 

def calcular_kpis(df: pd.DataFrame) -> dict: #"DICT" indica que a função retorna um dicionário com vários resultados

    df["Total"] = df["Quantidade"] * df["Valor"]

    faturamento_total = df["Total"].sum()
    quantidade_total = df["Quantidade"].sum()
    ticket_medio = faturamento_total / quantidade_total if quantidade_total > 0 else 0 #quanto, em média, cada item “vale” (faturamento / quantidade).
    #Se quantidade_total for 0, evita divisão por zero e coloca 0.

    #df.groupby("Produto"): agrupa todas as linhas por nome de produto.
    vendas_por_produto = df.groupby("Produto")["Total"].sum().sort_values(ascending=False) #["Total"].sum(): soma o valor total por produto.
    #["Quantidade"].sum(): soma a quantidade vendida por produto
    qtd_por_produto = df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False) #.sort_values(ascending=False): ordena do maior para o menor.

    vendas_por_dia = df.groupby(df["Data"].dt.date)["Total"].sum()

    top_produto_valor = vendas_por_produto.idxmax()
    top_produto_qtd = qtd_por_produto.idxmax()

    return {
        "faturamento_total": faturamento_total,
        "quantidade_total": quantidade_total,
        "ticket_medio": ticket_medio,
        "vendas_por_produto": vendas_por_produto,
        "qtd_por_produto": qtd_por_produto,
        "vendas_por_dia": vendas_por_dia,
        "top_produto_valor": top_produto_valor,
        "top_produto_qtd": top_produto_qtd,
    }

def calcular_lucro(df_vendas: pd.DataFrame, df_estoque: pd.DataFrame) -> dict:

    df_v = df_vendas.copy()#copia do df, pra nao mexer no original
    df_e = df_estoque.copy()

    df_v["Produto"] = df_v["Produto"].astype(str).str.strip().str.title() #aqui, padronizo os nomes
    df_e["Produto"] = df_e["Produto"].astype(str).str.strip().str.title()

    if "Total" not in df_v.columns: #garante que a coluna Total exista em df_v
        df_v["Total"] = df_v["Quantidade"] * df_v["Valor"]

    if "Custo_unitario" not in df_e.columns: #mantém apenas as colunas necessárias de estoque/custo
        raise ValueError("A coluna 'Custo_unitario' não foi encontrada no DataFrame de estoque.")

    df_e = df_e[["Produto", "Custo_unitario"]]

    df_merged = pd.merge(df_v, df_e, on="Produto", how="left")

    df_merged["Custo_unitario"] = pd.to_numeric(#se algum produto não tiver custo cadastrado, considera 0 
        df_merged["Custo_unitario"], errors="coerce"
    ).fillna(0.0)

    df_merged["Custo_total"] = df_merged["Quantidade"] * df_merged["Custo_unitario"]
    df_merged["Lucro"] = df_merged["Total"] - df_merged["Custo_total"]

    lucro_total = df_merged["Lucro"].sum()

    lucro_por_produto = (
        df_merged.groupby("Produto")["Lucro"]
        .sum()
        .sort_values(ascending=False)
    )

    faturamento_por_produto = df_merged.groupby("Produto")["Total"].sum()#margem por produto (lucro / faturamento), em percentual
    margem_por_produto = (lucro_por_produto / faturamento_por_produto * 100).fillna(0)

    return {
        "df_lucro": df_merged, # df completo com colunas de lucro/custo
        "lucro_total": lucro_total, #valor total de lucro no período
        "lucro_por_produto": lucro_por_produto,
        "margem_por_produto": margem_por_produto,  # em %
    }


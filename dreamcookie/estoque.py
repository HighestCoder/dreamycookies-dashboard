import os
from datetime import datetime
import pandas as pd 
import matplotlib.pyplot as plt 
from fpdf import FPDF 

ESTOQUE_PATH = "estoque.csv"

def carregar_estoque(path_estoque: str = ESTOQUE_PATH) -> pd.DataFrame:

    if not os.path.exists(path_estoque):
        raise FileNotFoundError(f"Arquivo de estoque não encontrado: {path_estoque}")

    df_estoque = pd.read_csv(path_estoque)

    cols_lower = {c.lower(): c for c in df_estoque.columns} #poe em minusculo pra facilitar
    mapping = {}

#padronizando nomes em colunas
    if "produto" in cols_lower:
        mapping[cols_lower["produto"]] = "Produto"
    elif "item" in cols_lower:
        mapping[cols_lower["item"]] = "Produto"

    if "custo_unitario" in cols_lower:
        mapping[cols_lower["custo_unitario"]] = "Custo_unitario"
    elif "custo" in cols_lower:
        mapping[cols_lower["custo"]] = "Custo_unitario"

    if "estoque_atual" in cols_lower:
        mapping[cols_lower["estoque_atual"]] = "Estoque_atual"
    elif "estoque" in cols_lower:
        mapping[cols_lower["estoque"]] = "Estoque_atual"

    if "estoque_minimo" in cols_lower:
        mapping[cols_lower["estoque_minimo"]] = "Estoque_minimo"
    elif "estoque_min" in cols_lower:
        mapping[cols_lower["estoque_min"]] = "Estoque_minimo"

    if mapping:
        df_estoque = df_estoque.rename(columns=mapping)

    df_estoque["Produto"] = df_estoque["Produto"].astype(str).str.strip().str.title()

    if "Custo_unitario" in df_estoque.columns:
        df_estoque["Custo_unitario"] = pd.to_numeric(
            df_estoque["Custo_unitario"], errors="coerce"
        ).fillna(0.0)

    if "Estoque_atual" in df_estoque.columns:
        df_estoque["Estoque_atual"] = pd.to_numeric(
            df_estoque["Estoque_atual"], errors="coerce"
        ).fillna(0).astype(int)

    if "Estoque_minimo" in df_estoque.columns:
        df_estoque["Estoque_minimo"] = pd.to_numeric(
            df_estoque["Estoque_minimo"], errors="coerce"
        ).fillna(0).astype(int)

    return df_estoque

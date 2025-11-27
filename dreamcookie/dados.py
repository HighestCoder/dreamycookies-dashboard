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

    #Como os arquivos das maquininhas podem vir com nomes de colunas diferentes, essa função padroniza tudo
def normalizar_colunas(df: pd.DataFrame) -> pd.DataFrame:

    mapping = {}
    cols_lower = {c.lower(): c for c in df.columns}

    if "produto" in cols_lower:
        mapping[cols_lower["produto"]] = "Produto"
    elif "item" in cols_lower:
        mapping[cols_lower["item"]] = "Produto"

    if "quantidade" in cols_lower:
        mapping[cols_lower["quantidade"]] = "Quantidade"
    elif "qtd" in cols_lower:
        mapping[cols_lower["qtd"]] = "Quantidade"

    if "valor" in cols_lower:
        mapping[cols_lower["valor"]] = "Valor"

    if "data" in cols_lower:
        mapping[cols_lower["data"]] = "Data"

    if mapping:
        df = df.rename(columns=mapping)

    return df

def carregar_dados(csv_paths): #essa função é responsável por ler todos os arquivos das maquininhas, tratar e unificar os dados
    dfs = [] #cria uma lista para acumular os DataFrames de cada maquininha

    for path in csv_paths:
        if not os.path.exists(path):
            print(f" Arquivo não encontrado: {path} (pulando)")
            continue

        try:
            df = pd.read_csv(path)
        except Exception as e:
            print(f" Erro ao ler {path}: {e}")
            continue

        df = normalizar_colunas(df)

        # garante colunas mínimas Garante que o arquivo tem as colunas mínimas necessárias. Se faltar alguma -> levanta erro com mensagem clara
        col_obrig = ["Produto", "Quantidade", "Valor"]
        for c in col_obrig:
            if c not in df.columns:
                raise ValueError(f"Coluna obrigatória '{c}' não encontrada em {path}")

        # limpeza
        df["Produto"] = df["Produto"].astype(str).str.strip().str.title() #astype(str) → garante que tudo seja string // #.str.title() → deixa “coxinha” → “Coxinha”, “REFRIGERANTE” → “Refrigerante”.
        df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce").fillna(0).astype(int) #.str.strip() remove espaços no começo e no fim.
        df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce").fillna(0.0) 
        if "Data" in df.columns: 
            df["Data"] = pd.to_datetime(df["Data"], errors="coerce") #Se já existe coluna Data, converte para datetime
        else:
            df["Data"] = pd.to_datetime(datetime.now().strftime(DATE_FORMAT))#Se não existe, assume a data de hoje (pra não ficar sem referência).

        df["Maquininha"] = os.path.basename(path) #cria coluna Maquininha com o nome do arquivo (maquina1.csv, etc).

        dfs.append(df) #Adiciona o DataFrame df na lista dfs.

    if not dfs:
        raise ValueError("Nenhum dado carregado. Verifique os arquivos CSV.") #Se nenhum CSV foi lido com sucesso → erro (não tem como continuar).

    df_all = pd.concat(dfs, ignore_index=True) #Senão, concatena tudo (maquina1 + maquina2) num único df_all
    return df_all
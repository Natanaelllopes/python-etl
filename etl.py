import pandas as pd


def extract(caminho_csv: str) -> pd.DataFrame:
    # Extrai os dados de data/usuarios.csv
    return pd.read_csv(caminho_csv)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    # Padroniza o nome da coluna
    if "nome" in df.columns:
        df = df.rename(columns={"nome": "name"})

    # Simula a geração de mensagens personalizadas
    df["mensagem"] = df["name"].apply(
        lambda name: f"{name}, investir hoje ajuda a construir um futuro financeiro mais seguro."
    )

    return df


def load(df: pd.DataFrame, caminho_saida: str):
    # Carrega os dados transformados em data/usuarios_saida.csv
    df.to_csv(caminho_saida, index=False)


if __name__ == "__main__":
    caminho_entrada = "data/usuarios.csv"
    caminho_saida = "data/usuarios_saida.csv"

    dados = extract(caminho_entrada)
    dados_transformados = transform(dados)
    load(dados_transformados, caminho_saida)

    print("ETL concluído. Dados salvos em:", caminho_saida)
    print("\nMensagens geradas:")
    print(dados_transformados[["id", "name", "mensagem"]])

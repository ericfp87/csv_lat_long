import pandas as pd

# Carregando o arquivo csv
df = pd.read_csv(r"C:\Files\INDICADORES DE LEITURAS - COPASA\DATABASE\BASE_LAT_LONG.csv")

# Transformando a coluna 'geometry.coordinates' em uma lista
df['geometry.coordinates'] = df['geometry.coordinates'].apply(eval)

# Selecionando apenas o primeiro valor da lista
df['geometry.coordinates'] = df['geometry.coordinates'].apply(lambda x: x[0])

# Dividindo os valores em duas colunas 'LONG' e 'LAT'
df[['LONG', 'LAT']] = pd.DataFrame(df['geometry.coordinates'].tolist(), index=df.index)

# Concatenando as colunas 'properties.NM_TIP_LOG', 'properties.NM_TIT_LOG', 'properties.NM_LOG'
df['Logradouro'] = df[['properties.NM_TIP_LOG', 'properties.NM_TIT_LOG', 'properties.NM_LOG']].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)

# Selecionando as colunas desejadas
df = df[["Municipio", "Logradouro", "LAT", "LONG"]]

df = df.drop_duplicates(subset=['Logradouro', 'Municipio'])

# Salvando o dataframe em um novo arquivo csv
df.to_csv(r"C:\Files\INDICADORES DE LEITURAS - COPASA\DATABASE\MUNICIPIOS_LAT_LONG.csv", sep=';', index=False)

print("Concluído!")

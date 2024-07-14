# csv_lat_long
 Geração de arquivo .csv com dados de latitude e longitude

# Processamento de Arquivo CSV de Coordenadas Geográficas - COPASA

Este repositório contém um script em Python que processa um arquivo CSV contendo coordenadas geográficas, transforma a estrutura dos dados, e salva o resultado final em um novo arquivo CSV.

## Estrutura do Projeto

```
├── INDICADORES DE LEITURAS - COPASA
│   ├── DATABASE
│   │   ├── BASE_LAT_LONG.csv
│   │   └── MUNICIPIOS_LAT_LONG.csv
│   └── script.py
```

## Requisitos

- Python 3.x
- Pandas

Você pode instalar as dependências usando:

```bash
pip install pandas
```

## Como Usar

1. Coloque o arquivo CSV que você deseja processar no diretório `C:\Files\INDICADORES DE LEITURAS - COPASA\DATABASE\`.

2. Execute o script `script.py`:

```python
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
```

3. O script irá processar o arquivo CSV especificado, transformar os dados e salvar um novo arquivo CSV chamado `MUNICIPIOS_LAT_LONG.csv` no mesmo diretório.

## Funcionalidades

- **Processamento de Arquivo CSV**: O script processa o arquivo CSV contendo coordenadas geográficas.
- **Transformação de Dados**: A coluna de coordenadas é convertida para duas colunas separadas, LAT e LONG.
- **Concatenação de Colunas**: As colunas que formam o logradouro são concatenadas em uma única coluna.
- **Remoção de Duplicatas**: Duplicatas são removidas com base nas colunas Logradouro e Município.
- **Exportação para CSV**: O DataFrame final é exportado para um novo arquivo CSV.

## Contribuição

Sinta-se à vontade para abrir issues e enviar pull requests. Toda contribuição é bem-vinda!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

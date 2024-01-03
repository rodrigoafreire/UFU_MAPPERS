# Importando a biblioteca pandas para manipulação e análise de dados
import pandas as pd

# Lendo um arquivo CSV contendo dados educacionais básicos de 2022
# O delimitador usado no arquivo é o ponto e vírgula (';')
# A codificação dos caracteres é 'iso-8859-1', comum em textos em português
# 'low_memory=False' é usado para eficientemente carregar arquivos grandes
# Altere o caminho do arquivo CSV para o seu diretório
df = pd.read_csv(".../microdados_ed_basica_2022.csv", delimiter=';', encoding='iso-8859-1', low_memory=False)

# Exibindo as primeiras 10 linhas do DataFrame para uma visualização rápida dos dados
df.head(10)

# Filtrando o DataFrame original para incluir apenas as linhas onde o município é Uberlândia
# 'df.loc' é usado para acessar um grupo de linhas e colunas pelo rótulo
# Aqui, estamos selecionando linhas onde 'NO_MUNICIPIO' é igual a 'Uberlândia'
df_mun = df.loc[df['NO_MUNICIPIO'] == 'Uberlândia']

# Exibindo as primeiras linhas do DataFrame filtrado para Uberlândia
df_mun.head()

# Salvando o DataFrame filtrado em um novo arquivo CSV
# 'sep' define o delimitador do arquivo CSV como ponto e vírgula (';')
# 'encoding' é novamente 'iso-8859-1' para manter a consistência de caracteres
# 'index=False' significa que os índices do DataFrame não serão escritos no arquivo CSV
# Altere o caminho do arquivo CSV para o seu diretório
df_mun.to_csv('.../microdados_uberlandia_2022.csv', sep=';', encoding='iso-8859-1', index=False)

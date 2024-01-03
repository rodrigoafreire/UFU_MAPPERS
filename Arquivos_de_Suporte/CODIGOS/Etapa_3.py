# Importando as bibliotecas necessárias
import pandas as pd  # Pandas para manipulação de dados
import matplotlib.pyplot as plt  # Matplotlib para visualização de dados

# Carregando os dados do arquivo CSV em um DataFrame do Pandas
# O arquivo contém dados sobre escolas em Uberlândia
# Altere o caminho do arquivo para o seu diretório
df = pd.read_csv('.../microdados_uberlandia_parte_2.csv', sep=';', encoding='latin-1')

# Supondo que o DataFrame 'df' tem uma coluna 'TP_DEPENDENCIA' que contém a classificação das escolas

# Contando o número de escolas em cada categoria de dependência
contagem_escolas = df['TP_DEPENDENCIA'].value_counts()

# Preparando os dados para o gráfico: rótulos e valores
tipos_escolas = contagem_escolas.index  # Tipos de escolas são os índices
quantidade_escolas = contagem_escolas.values  # Quantidade de escolas são os valores

# Criando um gráfico de barras para visualizar a distribuição das escolas
plt.figure(figsize=(8, 6))
plt.bar(tipos_escolas, quantidade_escolas, color=['blue', 'green', 'red'])
plt.xlabel('Tipo de Dependência')
plt.ylabel('Número de Escolas')
plt.title('Distribuição de Escolas por Tipo de Dependência')
plt.show()  # Exibindo o gráfico
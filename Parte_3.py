import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('E:/GitHub/UFU_MAPPERS/microdados/dados/microdados_uberlandia_parte_2.csv', sep=';', encoding='latin-1')

# Suponhamos que você tenha um DataFrame chamado 'df' com a coluna 'TP_DEPENDENCIA'
# que contém as classificações das escolas.

# Contar o número de escolas em cada categoria
contagem_escolas = df['TP_DEPENDENCIA'].value_counts()

# Definir rótulos e valores para o gráfico
tipos_escolas = contagem_escolas.index
quantidade_escolas = contagem_escolas.values

# Criar um gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(tipos_escolas, quantidade_escolas, color=['blue', 'green', 'red'])

# Adicionar rótulos e título
plt.xlabel('Tipo de Dependência')
plt.ylabel('Número de Escolas')
plt.title('Distribuição de Escolas por Tipo de Dependência')

# Mostrar o gráfico
plt.show()
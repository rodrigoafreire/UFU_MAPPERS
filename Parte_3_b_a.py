import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('E:/GitHub/UFU_MAPPERS/microdados/dados/microdados_uberlandia_parte_2.csv', sep=';', encoding='latin-1')

# Suponhamos que você tenha um DataFrame chamado 'df' com a coluna 'TP_DEPENDENCIA' que contém as classificações das escolas.

# Podemos fazer a legenda de duas formas:
# 1. Mapear os valores numéricos para os rótulos correspondentes
tipos_escolas = {
    1: 'Federal',
    2: 'Estadual',
    3: 'Municipal',
    4: 'Privada'
}

# Contar o número de escolas em cada categoria
labels = df['TP_DEPENDENCIA'].unique()

df['TP_DEPENDENCIA'] = df['TP_DEPENDENCIA'].map(tipos_escolas)

# Contar o número de escolas em cada categoria
contagem_escolas = df['TP_DEPENDENCIA'].value_counts()
print(contagem_escolas)
# Definir rótulos e valores para o gráfico
tipos_escolas = contagem_escolas.index
#quantidade_escolas = contagem_escolas.values

# Vamos imprimir os valores para ver como eles estão:
print(tipos_escolas)

# Definir as cores do gráfico
cores = ['skyblue', 'lightgreen', 'lightcoral', 'orange']

# Criar um gráfico de barras
plt.figure(figsize=(6, 6))

plt.pie(contagem_escolas, colors=cores, autopct='%1.1f%%')

# Inserir uma legenda
plt.legend(title="Legendas", labels=tipos_escolas, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Adicionar rótulos e título
plt.title('Distribuição de Escolas por Tipo de Dependência')

# Mostrar o gráfico
plt.show()
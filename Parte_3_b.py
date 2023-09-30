import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('E:/GitHub/UFU_MAPPERS/microdados/dados/microdados_uberlandia_parte_2.csv', sep=';', encoding='latin-1')

# Suponhamos que você tenha um DataFrame chamado 'df' com a coluna 'TP_DEPENDENCIA' que contém as classificações das escolas.

# Podemos fazer a legenda de duas formas:
# 1. Mapear os valores numéricos para os rótulos correspondentes
mapeamento_tipos_escolas = {
    1: 'Federal',
    2: 'Estadual',
    3: 'Municipal',
    4: 'Privada'
}

# Contar o número de escolas em cada categoria
contagem_escolas = df['TP_DEPENDENCIA'].value_counts()

# Definir rótulos e valores para o gráfico
tipos_escolas = contagem_escolas.index
quantidade_escolas = contagem_escolas.values

# Vamos imprimir os valores para ver como eles estão:
print(tipos_escolas)

# Definir as cores do gráfico
cores = ['r', 'g', 'b', 'y']

# Criar um gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(tipos_escolas, quantidade_escolas, color=['skyblue', 'lightgreen', 'lightcoral', 'orange'])

# Adicionar rótulos e título
plt.xlabel('Tipo de Dependência')
plt.ylabel('Número de Escolas')
plt.title('Distribuição de Escolas por Tipo de Dependência')

# Definir os rótulos no eixo x usando xticks
#plt.xticks(tipos_escolas, leg_tipos_escolas)
print([mapeamento_tipos_escolas[tipo_escola] for tipo_escola in tipos_escolas])

plt.xticks(tipos_escolas, [mapeamento_tipos_escolas[tipo_escola] for tipo_escola in tipos_escolas])

# Rotacionar os rótulos no eixo x para melhor legibilidade
plt.xticks(rotation=45)

# Mostrar o gráfico
plt.show()
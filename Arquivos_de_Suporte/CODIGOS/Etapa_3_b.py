# Importando as bibliotecas pandas e matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados de um arquivo CSV. 
# O parâmetro 'sep' define o separador dos dados (neste caso, ';'), 
# e 'encoding' especifica a codificação dos caracteres (latin-1)
df = pd.read_csv('.../microdados_uberlandia_parte_2.csv', sep=';', encoding='latin-1')

# Supondo que o DataFrame 'df' tenha uma coluna 'TP_DEPENDENCIA', que contém as classificações das escolas.

# Mapeando os valores numéricos para rótulos correspondentes em 'TP_DEPENDENCIA'
mapeamento_tipos_escolas = {
    1: 'Federal',
    2: 'Estadual',
    3: 'Municipal',
    4: 'Privada'
}

# Contando o número de escolas em cada categoria de dependência e armazenando o resultado
contagem_escolas = df['TP_DEPENDENCIA'].value_counts()

# Definindo os rótulos (tipos de escolas) e os valores (quantidade de escolas) para o gráfico
tipos_escolas = contagem_escolas.index
quantidade_escolas = contagem_escolas.values

# Imprimindo os tipos de escolas para verificar os dados
print(tipos_escolas)

# Definindo as cores para cada categoria no gráfico de barras
cores = ['skyblue', 'lightgreen', 'lightcoral', 'orange']

# Criando um gráfico de barras com tamanho 8x6
plt.figure(figsize=(8, 6))
plt.bar(tipos_escolas, quantidade_escolas, color=cores)

# Adicionando rótulos e título ao gráfico
plt.xlabel('Tipo de Dependência')
plt.ylabel('Número de Escolas')
plt.title('Distribuição de Escolas por Tipo de Dependência')

# Imprimindo a correspondência entre os tipos de escolas e seus rótulos
print([mapeamento_tipos_escolas[tipo_escola] for tipo_escola in tipos_escolas])

# Definindo os rótulos no eixo x do gráfico com os rótulos mapeados
plt.xticks(tipos_escolas, [mapeamento_tipos_escolas[tipo_escola] for tipo_escola in tipos_escolas])

# Rotacionando os rótulos no eixo x para melhor legibilidade
plt.xticks(rotation=45)

# Exibindo o gráfico
plt.show()

# Salvando o gráfico em um arquivo PNG
plt.savefig('.../grafico_1.png')
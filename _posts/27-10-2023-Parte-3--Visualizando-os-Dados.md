---
layout: post
title: Parte 3 - Visualização dos dados
categories: [Escolas, Python]
---

Este post trata da visualização dos dados. O objetivo é gerar gráficos e mapas para visualizar os dados de forma mais clara e objetiva.

### 3.a Verificando a instalação dos dados

Agora que temos os dados melhor organizados. Vamos começar a visualizá-los. Para isso, vamos usar a biblioteca matplotlib. A biblioteca matplotlib é uma biblioteca Python para criação de gráficos e visualizações. 
Vamos ver se as bibliotecas que precisamos já estão instaladas. Para isso, abra o prompt de comando e digite:

    pip list

Se as bibliotecas matplotlib e numpy não estiverem instaladas, instale-as com os seguintes comandos:
    
        pip install matplotlib
        pip install numpy

Com as bibliotecas instaladas podemos prosseguir com a visualização dos dados.

### 3.b Gerando a primeira visualização

Agora vamos abrir o nosso IDE ou o Jupyter notebook.

O primeiro passo é importar a biblioteca matplotlib e renomeá-la como plt. Além disso, vamos importar a biblioteca numpy e renomeá-la como np. A biblioteca numpy é uma biblioteca Python para cálculos matemáticos. 
Obs.*A renomeação é opcional, mas é uma prática comum para economizar tempo e digitação.*

    import matplotlib.pyplot as plt
    import numpy as np


Após importar as bibliotecas, iniciaremos nosso código abrindo a base de dados que tratamos anteriormente.
    
        df_mun = pd.read_csv('C:/Users/.../ESCOLAS_UBERLANDIA_PARTE_2.CSV', delimiter=';', encoding='latin')

Vamos supor que você tenha um DataFrame chamado 'df_mun' com a coluna 'TP_DEPENDENCIA' que contém as classificações das escolas.

Agora, vamos criar uma lista com os valores únicos da coluna 'TP_DEPENDENCIA' e armazená-la na variável 'labels'. Para isso, usamos a função unique() da biblioteca Pandas.

    labels = df_mun['TP_DEPENDENCIA'].unique()

Agora, vamos criar uma lista com a quantidade de escolas de cada tipo e armazená-la na variável 'sizes'. Para isso, usamos a função value_counts() da biblioteca Pandas.

    contagem_escolas = df_mun['TP_DEPENDENCIA'].value_counts()

Agora, vamos criar uma lista com as cores que queremos usar e armazená-la na variável 'colors'. Existem diversar formas de definir as cores do gráfico. No caso, adotaremos o nome das cores que está definido da documentação do matplotlib. Para mais informações, acesse o link abaixo:

[Documentação cores](https://matplotlib.org/2.1.1/gallery/color/named_colors.html#sphx-glr-gallery-color-named-colors-py)

No caso, escolhi 4 cores, visto que temos 4 tipos de escolas. Portanto, criaremos uma variável chamada 'colors' com 4 cores.

    colors = ['skyblue', 'lightgreen', 'lightcoral', 'orange']


Já podemos gerar nosso gráfico. Começamos criando uma figura (plt.figure) e definimos o seu tamanho:
    
    plt.figure(figsize=(8, 6))

Agora, vamos criar o gráfico de barra vertical. Para isso, usamos a função bar() da biblioteca matplotlib. Os argumentos da função são a lista com os valores únicos da coluna 'TP_DEPENDENCIA' (labels), a lista com a quantidade de escolas de cada tipo (sizes) e a lista com as cores que queremos usar (colors).

    plt.bar(labels, sizes, color=colors)

No nosso caso 
    plt.bar(tipos_escolas, quantidade_escolas, color=['skyblue', 'lightgreen', 'lightcoral', 'orange'])


Em seguida, definimos os rótulos e títulos
    plt.xlabel('Tipo de escola')
    plt.ylabel('Quantidade de Escolas')
    plt.title('Distribuição de Escolas por Tipo de Dependência')

Definimos os rótulos no eixo x usando xticks: 

    print([mapeamento_tipos_escolas[tipo_escola] for tipo_escola in tipos_escolas])
    plt.xticks(tipos_escolas, [mapeamento_tipos_escolas[tipo_escola] for tipo_escola in tipos_escolas])

. Para isso, usamos a função pie() da biblioteca matplotlib. Os argumentos da função são a lista com os valores únicos da coluna 'TP_DEPENDENCIA' (labels), a lista com a quantidade de escolas de cada tipo (sizes), a lista com as cores que queremos usar (colors) e o argumento autopct='%1.1f%%' para exibir a porcentagem de cada tipo de escola.
    
    plt.pie(contagem_escolas, labels=labels, colors=colors, autopct='%1.1f%%')

Então adicionamos um título ao gráfico. Para isso, usamos a função title() da biblioteca matplotlib. O argumento da função é o título que queremos exibir (Escolas de Uberlândia por tipo).
    
    plt.title('Escolas de Uberlândia por tipo')

Por fim, exibimos o gráfico. Para isso, usamos a função show() da biblioteca matplotlib.
        
    plt.show()

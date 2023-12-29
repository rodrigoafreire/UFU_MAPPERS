# Tutorial de Visualização de Dados de Escolas Parte 3

Este tutorial demonstra como visualizar a distribuição de escolas por tipo de dependência usando Python.

### Importação de Bibliotecas

Começamos importando as bibliotecas necessárias.

```python
import pandas as pd  # Pandas para manipulação de dados
import matplotlib.pyplot as plt  # Matplotlib para visualização de dados
```
**Dica**: Pandas é excelente para manipular dados, e Matplotlib é ótimo para criar gráficos.

### Carregamento dos Dados

Carregue os dados do arquivo CSV para um DataFrame do Pandas.

```python
df = pd.read_csv('caminho_do_arquivo/microdados_uberlandia_parte_2.csv', sep=';', encoding='latin-1')
```
**Dica**: Certifique-se de ajustar o caminho do arquivo para onde ele está localizado em seu sistema.

### Análise dos Dados

Vamos contar o número de escolas em cada tipo de dependência.

```python
contagem_escolas = df['TP_DEPENDENCIA'].value_counts()
```
**Dica**: `value_counts()` é uma maneira eficiente de contar a frequência de valores no Pandas.

### Preparação para o Gráfico

Organize os dados para o gráfico.

```python
tipos_escolas = contagem_escolas.index  # Tipos de escolas são os índices
quantidade_escolas = contagem_escolas.values  # Quantidade de escolas são os valores
```
**Dica**: Separar rótulos e valores ajuda na visualização dos dados.

### Criação do Gráfico

Agora, criaremos um gráfico de barras.

```python
plt.figure(figsize=(8, 6))
plt.bar(tipos_escolas, quantidade_escolas, color=['blue', 'green', 'red'])
plt.xlabel('Tipo de Dependência')
plt.ylabel('Número de Escolas')
plt.title('Distribuição de Escolas por Tipo de Dependência')
plt.show()  # Exibindo o gráfico
```
**Dica**: Ajuste as cores e o tamanho conforme necessário para melhorar a visualização.

---

```

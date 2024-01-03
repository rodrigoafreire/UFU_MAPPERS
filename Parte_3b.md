# Tutorial de Análise de Dados com Python

Este tutorial ensina como analisar a distribuição de escolas por tipo de dependência administrativa usando Python.

### Configuração Inicial

Primeiro, vamos importar as bibliotecas necessárias.

```python
import pandas as pd
import matplotlib.pyplot as plt
```
**Dica**: `pandas` é ótima para manipulação de dados, e `matplotlib` para visualização de dados.

### Carregamento dos Dados

Agora, carregue os dados do arquivo CSV.

```python
df = pd.read_csv('caminho_para_o_arquivo/microdados_uberlandia_parte_2.csv', sep=';', encoding='latin-1')
```
**Dica**: Lembre-se de substituir `'caminho_para_o_arquivo'` pelo caminho real do seu arquivo CSV.

### Mapeamento dos Dados

Vamos mapear os tipos de dependência das escolas para algo mais legível.

```python
mapeamento_tipos_escolas = {
    1: 'Federal',
    2: 'Estadual',
    3: 'Municipal',
    4: 'Privada'
}
```
**Dica**: Este passo torna os dados numéricos mais compreensíveis.

### Análise de Dados

Conte o número de escolas em cada categoria.

```python
contagem_escolas = df['TP_DEPENDENCIA'].value_counts()
```
**Dica**: `value_counts()` é uma forma rápida de contar ocorrências no pandas.

### Preparação para o Gráfico

Prepare os dados para visualização.

```python
tipos_escolas = contagem_escolas.index
quantidade_escolas = contagem_escolas.values
```
**Dica**: Separe os rótulos e valores para facilitar a criação do gráfico.

### Criação do Gráfico

Vamos criar um gráfico de barras colorido.

```python
plt.figure(figsize=(8, 6))
plt.bar(tipos_escolas, quantidade_escolas, color=['skyblue', 'lightgreen', 'lightcoral', 'orange'])
plt.xlabel('Tipo de Dependência')
plt.ylabel('Número de Escolas')
plt.title('Distribuição de Escolas por Tipo de Dependência')
plt.xticks(tipos_escolas, [mapeamento_tipos_escolas[tipo_escola] for tipo_escola in tipos_escolas])
plt.xticks(rotation=45)
plt.show()
```
**Dica**: `plt.figure()` define o tamanho do gráfico. `plt.bar()` cria o gráfico de barras.

### Salvando o Gráfico

Por fim, salve o gráfico em um arquivo PNG.

```python
plt.savefig('caminho_para_salvar_o_arquivo/grafico_1.png')
```
**Dica**: Altere `'caminho_para_salvar_o_arquivo'` para o local desejado em seu sistema de arquivos.

---

```

# Importando a biblioteca pandas para manipulação e análise de dados
import pandas as pd

# Carregando dados de um arquivo CSV referente às escolas em Uberlândia
# 'delimiter' especifica o caractere usado para separar valores (neste caso, o ponto e vírgula)
# 'encoding' define a codificação dos caracteres como 'iso-8859-1'
# 'low_memory=False' é utilizado para carregar eficientemente grandes arquivos
df_mun = pd.read_csv(".../microdados_uberlandia.csv", delimiter=';', encoding='iso-8859-1', low_memory=False)

# Comentários explicando o significado de cada coluna do DataFrame
# Por exemplo, 'CO_ENTIDADE' é o Código da Escola, 'TP_DEPENDENCIA' o Tipo de Dependência Administrativa, etc.

# Filtrando o DataFrame para incluir apenas escolas em funcionamento
# 'TP_SITUACAO_FUNCIONAMENTO' igual a 1 indica que a escola está em atividade
df_mun_func = df_mun.loc[df_mun['TP_SITUACAO_FUNCIONAMENTO'] == 1]

# Contando o número de escolas em funcionamento
df_mun_func['TP_SITUACAO_FUNCIONAMENTO'].value_counts()

# Salvando os dados filtrados em um novo arquivo CSV
df_mun_func.to_csv(".../microdados_uberlandia_em_funcionamento_b.csv", sep=';', encoding='iso-8859-1', index=False)

# Comentário explicativo sobre a verificação da quantidade de alunos matriculados

# Definindo as colunas relacionadas à quantidade de matrículas em diferentes categorias
colunas = ['QT_MAT_BAS', 'QT_MAT_PROF', 'QT_MAT_PROF_TEC', 'QT_MAT_EJA']

# Substituindo valores ausentes (NaN) por 0 nessas colunas
df_mun_func[colunas] = df_mun[colunas].fillna(0)

# Calculando o total de alunos matriculados somando os valores nas colunas especificadas
# 'sum(axis=1)' soma os valores horizontalmente (ao longo das colunas)
df_mun_func['QT_ALUNOS_TOTAL'] = df_mun[colunas].sum(axis=1)

# Agrupando a quantidade total de alunos por tipo de dependência administrativa
# e somando esses valores para cada tipo
print(df_mun_func['QT_ALUNOS_TOTAL'].groupby(df_mun_func['TP_DEPENDENCIA']).sum())

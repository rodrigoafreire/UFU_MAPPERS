# Oficina Mapeamento de Escolas - UFUMappers



## Parte 1 - Instalação do Python e das bibliotecas a serem utilizadas

### 1.a O que é Python (linguagem de programação)?

Python é uma linguagem de programação, ou seja, uma ferramenta que os computadores entendem para realizar tarefas específicas. Mas, ao contrário de outras linguagens de programação que podem parecer complexas, Python é conhecida por sua simplicidade e legibilidade.

Imagine Python como uma linguagem que você usa para dar instruções a um computador. Em vez de usar palavras difíceis de entender, você escreve comandos em Python que são parecidos com a linguagem humana.

### 1.b O que são bibliotecas em programação?

Imagine que você está construindo uma casa a partir do zero, e você precisa fazer todas as peças, como portas, janelas, encanamento, fiação elétrica e muito mais, do zero. Isso seria um trabalho extremamente demorado e complicado.

Agora, pense em programação da mesma maneira. Quando você está escrevendo um programa de computador, às vezes precisa realizar tarefas complexas, como criar gráficos, realizar cálculos matemáticos avançados ou até mesmo interagir com a internet. Em vez de escrever todo o código do zero para realizar essas tarefas, você pode usar "bibliotecas".

Bibliotecas são conjuntos de código pré-escrito que contêm funções, classes e métodos para realizar tarefas específicas. Elas são como kits de ferramentas que programadores podem usar para economizar tempo e esforço. As bibliotecas são criadas por outros programadores e estão disponíveis gratuitamente ou através de licenças específicas.

Por exemplo, se você estiver programando em Python e precisar criar gráficos, pode usar a biblioteca matplotlib, que fornece todas as ferramentas necessárias para criar gráficos bonitos sem escrever o código do zero. Se precisar fazer solicitações à web, a biblioteca requests simplifica essa tarefa.

O uso de bibliotecas economiza tempo e torna a programação mais eficiente, permitindo que os desenvolvedores se concentrem em resolver os problemas específicos do projeto em vez de reinventar a roda a cada vez que enfrentam uma tarefa comum.

```Em resumo, bibliotecas em programação são como caixas de ferramentas cheias de funcionalidades prontas para uso, que os programadores podem incorporar em seus projetos para realizar tarefas específicas sem escrever todo o código do zero. Isso ajuda a tornar o desenvolvimento de software mais rápido e eficiente.```

Agora, como instalar o Python e suas bibliotecas:

### 1.c Instalando o Python e suas bibliotecas

**Baixando o Python:**

A primeira coisa que você precisa fazer é baixar o Python em seu computador. Para isso, siga os passos abaixo:

- Acesse o site oficial do Python em python.org.
- Clique na versão mais recente do Python, que será exibida na página inicial.
- Escolha o instalador apropriado para o seu sistema operacional (Windows, macOS ou Linux) e faça o download.
- Abra o arquivo de instalação baixado e siga as instruções na tela para instalar o Python em seu computador.

**Verificando a instalação:** 

Após a instalação, você pode verificar se o Python foi instalado corretamente. Abra o prompt de comando (no Windows) ou o terminal (no macOS e Linux) e digite o seguinte comando:

    python (ENTER)

    python --version

Isso deve exibir a versão do Python que você instalou, confirmando que a instalação foi bem-sucedida.

### 1.d Instalando as bibliotecas que serão utilizadas.

O Python é permite que você use bibliotecas, que são conjuntos de código pré-escritos para realizar tarefas específicas. Para instalar bibliotecas, você pode usar uma ferramenta chamada pip, que é o gerenciador de pacotes do Python. 
Em princípio, utilizaremos três bibliotecas principais. São elas
* Pandas:  biblioteca Python para análise de dados.
* Matplotlib: biblioteca Python para criação de gráficos e visualizações.
* Folium: biblioteca Python que facilita a criação de mapas interativos e visualizações geoespaciais.
  
Aqui está como você pode instalar uma biblioteca, por exemplo, a biblioteca matplotlib para criar gráficos:

Abra o prompt de comando ou o terminal e digite:

```pip install matplotlib```

*O pip baixará e instalará a biblioteca matplotlib em seu sistema. Você pode fazer isso para qualquer biblioteca Python que você precise* 

```pip install pandas```
```pip install folium```

### 1.e Ambientes de desenvolvimento
Um ambiente de desenvolvimento, comumente chamado de "IDE" (Ambiente de Desenvolvimento Integrado) ou "IDE de Desenvolvimento", é uma ferramenta de software projetada para auxiliar programadores e desenvolvedores em várias etapas do processo de criação de software. Ele fornece um conjunto de recursos e ferramentas integradas que tornam mais fácil e eficiente escrever, depurar e gerenciar código de programação

**Exemplos de IDEs** 
IDLE (Python IDLE):

    IDLE é o ambiente de desenvolvimento integrado padrão que acompanha a instalação do Python.
    É simples, leve e fácil de usar, adequado para iniciantes.
    Oferece recursos básicos de edição de código, execução de scripts e depuração.

Thonny:

    Thonny é um ambiente Python especialmente projetado para iniciantes.
    É leve e fácil de usar, com uma interface intuitiva.
    Oferece recursos de edição de código, depuração e gerenciamento de pacotes.

Visual Studio Code (VS Code) com extensões Python:

    O VS Code é um editor de código altamente personalizável e leve.
    Você pode adicionar extensões Python, como "Python" da Microsoft, para transformá-lo em um ambiente Python completo.
    Ele oferece suporte a depuração, gerenciamento de pacotes e integração com Git.

![Exemplo: VS CODE](Imagens/VS_Code.png)


Sublime Text com extensões Python:

    O Sublime Text é um editor de texto altamente configurável e leve.
    Você pode adicionar pacotes e extensões específicos do Python para habilitar recursos de desenvolvimento Python.
    É amplamente utilizado por desenvolvedores que apreciam sua velocidade e simplicidade.


**Uma outra alternativa** 
No lugar nos IDEs, podemos também utilizar o  *Jupyter*, uma aplicação web de código aberto que permite criar e compartilhar documentos interativos, chamados de *notebooks*. Ele é amplamente usado porque permite combinar código, texto explicativo, visualizações e outros elementos em um único documento interativo.
Para usa-lo é necessário realizar uma instalação, assim como fizemos com as bibliotecas.

Abra o prompt de comando e digite:
```pip install jupyter```

A instalação irá rodar e, em seguida, estará pronta para ser utilizada.

Para rodar o *jupyter* basta digitar no prompt de comando

```jupyter notebook```

![Exemplo da tela do Jupyter, cada linha pode ser executada individualmente](Imagens/Jupyter.png)


Um possível erro é quando o sistema não identifica a instalação do *Jupyter*. Nesse caso, é preciso corrigir o PATH do sistema. Além disso, também é possível que o sistema não consiga abrir o *notebook*, ou seja, o *Jupyter* é encontrado porém não é possível abrir um localhost. Para corrigir esses problemas, leia o item **Observações** ao final do texto

**Pronto, agora você já tem o Python e as bibliotecas instaladas e finalmente podemos começar!!**


## Parte 2 - Levantamento e tratamento dos dados

### 2.a Adquirindo os dados

Os dados utilizados nessa oficina foram obtidos no site do INEP (Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira), que é uma autarquia federal vinculada ao Ministério da Educação (MEC). O INEP é responsável pela coleta, análise e divulgação de informações sobre a educação brasileira.
Para acessa-los basta clicar no link abaixo: 

[INEP - Acessar Microdados ](https://www.gov.br/inep/pt-br/areas-de-atuacao/pesquisas-estatisticas-e-indicadores/censo-escolar/resultados)

![Tela inicial do site do INEP](Imagens/INEP.png)

O arquivo zip baixado contém 3 subpastas. São elas:

1. Anexos: Que contém o dicionário de dados, que é um documento que descreve os dados contidos no arquivo.
2. Dados: Que contém os dados propriamente ditos, em formato CSV.
3. Leia-me: Que contém um arquivo de texto com instruções para a leitura dos dados.

![Arquivos INEP](Imagens/arquivo_inep.png)

Para nós, o mais importante é a pasta Dados, que contém os dados em formato CSV. CSV é um formato de arquivo de texto simples que armazena dados em uma tabela, com **cada linha representando uma linha da tabela e cada coluna representando uma coluna da tabela.** Os dados são separados por vírgulas, daí o nome "CSV" (valores separados por vírgula). Além disso, os **Anexos** ajudam a entender o significado de cada coluna.

É possível abrir o arquivo CSV em uma planilha, como o Microsoft Excel ou o Google Sheets. Para isso, basta abrir o arquivo CSV em uma planilha e os dados serão exibidos em uma tabela. No entanto, arquivos pesados podem travar o Excel ou o Sheets. Além disso, esses programas não são adequados para análise de dados, pois não oferecem recursos de análise de dados avançados. 

No nosso caso, o arquivo csv possui 125mb, o que é um tamanho considerável. Por isso, utilizaremos o Python para ler e analisar os dados, por meio da biblioteca Pandas.

### 2.b Entendendo os dados

Primeiramente, vou abrir o arquivo *dicionário_dados_educação_básica.xlsx* para entender o significado de cada coluna e ter uma visão geral dos dados.
O arquivo fica localizado em: 
``` INEP\Anexos\ANEXO I...\dicionário_dados_educação_básica.xlsx ```

Uma leitura rápida me indica que existem cerca de 400 colunas. Ou seja, existem muitas informações que podem ser retiradas desse arquivo, incluindo a localização (endereço), número de alunos, número de professores, número de salas de aula etc.

### 2.c Abrindo o arquivo CSV com Pandas

Agora, vamos abrir o arquivo CSV com a biblioteca Pandas. Para isso, abra o prompt de comando e digite:

```python```

```import pandas as pd```

```df = pd.read_csv('C:\Users\...\ESCOLAS.CSV', sep='|', encoding='latin-1')```

```df.head()```



## Observações

Erro PATH Jupyter

    import sys

    print (sys.path)


Erro Local Host
    c.ServerApp.use_redirect_file = False

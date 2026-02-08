# Importação da biblioteca para manipulação de dados em tabelas
import pandas as pd

# Importação da biblioteca NumPy para operações matemáticas  e arrays
import numpy as np

# Importação da biblioteca Matplotlib para geração de gráficos
import matplotlib.pyplot as plt

# Importação  da biblioteca Seaborn para Visualização estatística de dados
import seaborn as sns

# Importação da biblioteca random para geração de números aleatórios
import random

# Importação das classes datetime  e timedelta para manipulação de datas e intervalos de tempo
from datetime import datetime, timedelta

# Definição da função para gerar dados fictícios de vendas

# Definição da função para gerar dados fictícios de vendas
def dsa_gera_dados_ficticios(num_registros = 600):
    
    """
    Gera um DataFrame do Pandas com dados de vendas fictícios.
    """

    # Mensagem inicial indicando a quantidade de registros a serem gerados
    print(f"\nIniciando a geração de {num_registros} registros de vendas...")

    # Dicionário com produtos, suas categorias e preços
    produtos = {
        'Laptop Gamer': {'categoria': 'Eletrônicos', 'preco': 7500.00},
        'Mouse Vertical': {'categoria': 'Acessórios', 'preco': 250.00},
        'Teclado Mecânico': {'categoria': 'Acessórios', 'preco': 550.00},
        'Monitor Ultrawide': {'categoria': 'Eletrônicos', 'preco': 2800.00},
        'Cadeira Gamer': {'categoria': 'Móveis', 'preco': 1200.00},
        'Headset 7.1': {'categoria': 'Acessórios', 'preco': 800.00},
        'Placa de Vídeo': {'categoria': 'Hardware', 'preco': 4500.00},
        'SSD 1TB': {'categoria': 'Hardware', 'preco': 600.00}
    }

    # Cria uma lista apenas com os nomes dos produtos
    lista_produtos = list(produtos.keys())

    # Dicionário com cidades e seus respectivos estados
    cidades_estados = {
        'São Paulo': 'SP', 'Rio de Janeiro': 'RJ', 'Belo Horizonte': 'MG',
        'Porto Alegre': 'RS', 'Salvador': 'BA', 'Curitiba': 'PR', 'Fortaleza': 'CE'
    }

    # Cria uma lista apenas com os nomes das cidades
    lista_cidades = list(cidades_estados.keys())

    # Lista que armazenará os registros de vendas
    dados_vendas = []

    # Define a data inicial dos pedidos
    data_inicial = datetime(2026, 1, 1)

    # Loop para gerar os registros de vendas
    for i in range(num_registros):
        
        # Seleciona aleatoriamente um produto
        produto_nome = random.choice(lista_produtos)

        # Seleciona aleatoriamente uma cidade
        cidade = random.choice(lista_cidades)

        # Gera uma quantidade de produtos vendida entre 1 e 7
        quantidade = np.random.randint(1, 8)

        # Calcula a data do pedido a partir da data inicial
        data_pedido = data_inicial + timedelta(days = int(i/5), hours = random.randint(0, 23))

        # Se o produto for Mouse ou Teclado, aplica desconto aleatório de até 10%
        if produto_nome in ['Mouse Vertical', 'Teclado Mecânico']:
            preco_unitario = produtos[produto_nome]['preco'] * np.random.uniform(0.9, 1.0)
        else:
            preco_unitario = produtos[produto_nome]['preco']

        # Adiciona um registro de venda à lista
        dados_vendas.append({
            'ID_Pedido': 1000 + i,
            'Data_Pedido': data_pedido,
            'Nome_Produto': produto_nome,
            'Categoria': produtos[produto_nome]['categoria'],
            'Preco_Unitario': round(preco_unitario, 2),
            'Quantidade': quantidade,
            'ID_Cliente': np.random.randint(100, 150),
            'Cidade': cidade,
            'Estado': cidades_estados[cidade]
        })
    
    # Mensagem final indicando que a geração terminou
    print("Geração de dados concluída.\n")

    # Retorna os dados no formato de DataFrame
    return pd.DataFrame(dados_vendas)


# Gera os dados chamando a função da célula anterior
df_vendas = dsa_gera_dados_ficticios(500)

# tipo da variavel df_vendas
print(type(df_vendas))
 
# Shape
print(df_vendas.shape)

# Exibe as 5 primeiras linhas do Dataframe
print(df_vendas.head())

# Exibe as 5 últimas linhas do Dataframe
print(df_vendas.tail())

# Exibe informações gerais sobre Dataframe (tipos de dados, valores não nulos)
print(df_vendas.info())

# Resumo estatístico
print(df_vendas.describe())

# Tipos de dados
print(df_vendas.dtypes)

# Limpeza, Pré-Processamento e Engenharia de Atributos

# Se a coluna 'Data_pedido' não estiver como tipo datetime, precisamos fazer a conversão explicíta
# A coluna pode ser usada para ánalise Temporal
df_vendas['Data_Pedido'] = pd.to_datetime(df_vendas['Data_Pedido'])

# Engenharia de atributos
# Criando a coluna 'Faturamento' (preço x unidade)
df_vendas['Faturamento'] = df_vendas['Preco_Unitario'] * df_vendas['Quantidade']

# Engenharia de atributos
# Usando uma função lambda para criar uma coluna de status de entrega
df_vendas['Status_Entrega'] = df_vendas['Estado'].apply(lambda estado: 'Rápida' if estado in ['SP','RJ','MG'] else 'Normal')

# Exibe informações gerais sobre o DataFrame (tipos de dados, valores não nulos)
print(df_vendas.info())

# Exibe as 5 primeiras Linhas novamente para ver as novas colunas
print(df_vendas.head())

# Análise 1 - Top 10 Produtos Mais Vendidos

# Agrupa por nome do produto, soma a quantidade e ordena para encontrar as mais vendidos
top_10_produtos =  df_vendas.groupby('Nome_Produto')['Quantidade'].sum().sort_values(ascending=False).head(10)

# Exibe o resultado
print(top_10_produtos)

# Define um estilo para os gráficos
sns.set_style("whitegrid")

# Cria a figura e os eixos
plt.figure(figsize=(12,7))

# Cria o gráfico de barras horizontais
top_10_produtos.sort_values(ascending=True).plot(kind='barh', color= 'skyblue')

# Adiciona títulos e labels
plt.title('Top 10 Produtos Mais Vendidos',fontsize = 16)
plt.xlabel('Quantidade Vendida',fontsize=12)
plt.ylabel('Produto',fontsize=12)

#Exibe o gráfico
plt.tight_layout()
plt.show()
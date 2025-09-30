# lendo um arquivo json
import json
import pandas as pd


file = open('dados/vendas.json')

data = json.load(file)

# print(data)

#criando o data frame com o dicionario 
df = pd.DataFrame.from_dict(data)

# print(df['Data da Compra'])

# mudando o tipo de uma variavel
df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')


file.close()

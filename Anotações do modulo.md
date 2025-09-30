Criando um ambiente virtual de desenvolvimento 

venv

python -m venv .venv
dentro da pasta venv tem o activate dentro o script, ativar ele 
.\.venv\Scripts\activate

sem o python na frente ele executa 

pip list

instalar as bibliotecas 

pip install pandas 
pip install plotly
pip install streamlit

---


Aula 2 - 

---

Aula 3 - 

---
Aula 4 -

Foram criadas colunas 
coluna2, coluna2 = st.columns(2)

e informado o que seria visualizado em cada coluna

with coluna1: (na coluna 1)
    (crie uma métrica utilizando soma)
      st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$'))

with coluna 2: (na coluna 2)
    (crie uma métrica mostrando a quantidade)
    st.metric('Quantidade de vendas', format_number(df.shape[0])) - df.shape[0] pega o numero de linha 

    df.shape(1) pega o numero de colunas

    



---
Construindo a tabela receita por Estado 

preparar os dados para criação dos dados

---
scatter_geo

grafico_map_estado = px.scatter_geo( #passar o dataframe
    df_rec_estado,
    lat='lat',
    lon='lon',
    scope = 'south america', 
    size = 'Preço',
    template = 'seaborn',
    hover_name = 'Local da compra',
    hover_data = {' lat': False, 'lon': False},
    title = 'Receita por Estado'

)

---
Receita por mês

criar o dataframe e cria o grafico e aloca no streamlit 



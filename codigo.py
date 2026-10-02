# Titulo - Sistema de Vendas
# Secao Cadastrar Vendas
    # Campo Data
    # Campo Vendedor - Ana, Bruno, Carla
    # Campo Produto - Notebook, Fone, Celular
    # Quantidade
    # Campo Valor
    # Botao Cadastrar Venda
        # Quando eu clicar no botao -> adcionar a venda na tabela
# Secao Vendas Cadastradas
    # Tabela com as vendas
# Secao Dashboard
    # Card/Metrica -> Faturamento Total
    # Grafico de Barra/Coluna -> Venda por vendedor
    # Grafico de Pizza -> Venda por produto

# pip install streamlit pandas plotly

import streamlit as st
import pandas as pd
import plotly.express as px

# carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")

# secao de cadastro de vendas
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Fone", "Celular"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# logica de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False) # serve para atualizar a tabela de vendas conforme vou cadastrando as vendas
    st.success("Venda cadastrada com sucesso!")

# secao de visualizar vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas) # tabela do pandas dataframe


# secao de dashboard
st.write("## Dashboard")

# Card/Metrica -> Faturamento Total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}")

# Grafico de Barra/Coluna -> Venda por vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

# Grafico de Pizza -> Venda por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5, title="Venda por Produto")
st.plotly_chart(grafico2)



# colocar site no ar, github, botao de +, novo repositorio, colocar titulo, tornar publico, criar, depois fazer upload dos arquivos arrastando para local
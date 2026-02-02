import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Função para buscar e limpar os dados
@st.cache_data
def fetch_data():
    html = requests.get("https://statisticstimes.com/tech/top-computer-languages.php").content
    soup = BeautifulSoup(html, 'html.parser')
    tabela = soup.find('table', {'id': 'table_id1'}).find('tbody')
    linhas = tabela.find_all('tr')
    
    linguagem = []
    pontos = []
    for linha in linhas:
        dado = linha.find_all('td')
        linguagem.append(dado[2].text)
        pontos.append(float(dado[3].text.replace('%', '').strip()))
    
    df = pd.DataFrame({'Linguagem': linguagem, 'Pontos': pontos})
    return df

dados = fetch_data()

# Configuração da interface Streamlit
st.title("Análise das Principais Linguagens de Programação")
st.info("👈 Selecione uma ou mais opções no menu lateral para visualizar os dados e gráficos.")
st.sidebar.header("Opções")

# Opções de exibição
table_option = st.sidebar.checkbox("Exibir Tabela de Dados")
graph_line = st.sidebar.checkbox("Gráfico de Linha")
graph_bar = st.sidebar.checkbox("Gráfico de Barras")
graph_pie = st.sidebar.checkbox("Top 3 - Gráfico de Pizza")

if table_option:
    st.subheader("Tabela de Linguagens e Pontos")
    st.write(dados)

if graph_line:
    st.subheader("Gráfico de Linha das Linguagens")
    plt.figure(figsize=(12, 6))
    plt.plot(dados['Linguagem'], dados['Pontos'], marker='o', linestyle='-', color='skyblue')
    plt.xticks(rotation=45)
    plt.xlabel("Linguagem")
    plt.ylabel("Pontos (%)")
    plt.title("Porcentagem por Linguagem")
    st.pyplot(plt)

if graph_bar:
    st.subheader("Gráfico de Barras das Linguagens")
    plt.figure(figsize=(10, 8))
    plt.barh(dados['Linguagem'], dados['Pontos'], color='skyblue')
    plt.xlabel("Pontos (%)")
    plt.ylabel("Linguagem")
    plt.title("Porcentagem por Linguagem")
    st.pyplot(plt)

if graph_pie:
    st.subheader("Top 3 Linguagens - Gráfico de Pizza")
    top_3 = dados.nlargest(3, 'Pontos')
    plt.figure(figsize=(8, 8))
    plt.pie(top_3['Pontos'], labels=top_3['Linguagem'], autopct='%1.2f%%',
            colors=['#a8d0e6', '#e0c3fc', '#ffd9a6'])
    plt.title("Top 3 Linguagens por Porcentagem")
    st.pyplot(plt)

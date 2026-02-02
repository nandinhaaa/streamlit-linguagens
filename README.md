
# 📊 Análise das Principais Linguagens de Programação

Este projeto é uma aplicação interativa desenvolvida com **Streamlit** que realiza a raspagem de dados das linguagens de programação mais populares a partir do site [Statistics Times](https://statisticstimes.com/tech/top-computer-languages.php), e apresenta os resultados de forma visual através de **tabelas e gráficos**.

## Projeto 
* acesse aqui: https://appe-linguagens-i5kgff2z6ym3b6rqq6ntmm.streamlit.app/

## 🚀 Funcionalidades

* 🔍 **Raspagem de dados** em tempo real usando `requests` + `BeautifulSoup`.
* 📑 Exibição dos dados em tabela interativa.
* 📈 Gráfico de linha com a evolução das linguagens.
* 📊 Gráfico de barras para comparação.
* 🥧 Gráfico de pizza destacando o **Top 3 linguagens**.
* ⚡ Interface simples e intuitiva feita com **Streamlit**.

---

## 🛠️ Tecnologias Utilizadas

* [Python 3](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [Requests](https://docs.python-requests.org/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
* [Matplotlib](https://matplotlib.org/)
* [Streamlit](https://streamlit.io/)

---

## 📥 Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/nandinhaaa/streamlite-linguagens.git
cd streamlite-linguagens
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

*As dependências do projeto estão listadas no arquivo `requirements.txt`.*

```bash
pip install requests beautifulsoup4 pandas matplotlib streamlit
```

### 4. Execute a aplicação

```bash
streamlit run app.py
```

O projeto rodará em: **[http://localhost:8501](http://localhost:8501)**

---

## 📸 Exemplos de Visualização

* **Tabela de Dados**
 <img width="1922" height="856" alt="image" src="https://github.com/user-attachments/assets/bc2724ec-eca5-4f93-9dfe-a5442ad610ab" />

* **Gráfico de Linha**
 <img width="1892" height="822" alt="image" src="https://github.com/user-attachments/assets/0478cad3-e12c-4196-9598-2ec9f7f79cc4" />

* **Gráfico de Barras**
  <img width="1914" height="893" alt="image" src="https://github.com/user-attachments/assets/adcbd792-4388-49c8-8f2b-0040c4aa218b" />

* **Top 3 - Gráfico de Pizza**
  <img width="1923" height="916" alt="image" src="https://github.com/user-attachments/assets/a2e9291a-90e4-4696-a88f-2381916f51a8" />

---

## 📂 Estrutura do Projeto

```
streamlite-linguagens/
│── app.py              # Código principal da aplicação
│── requirements.txt    # Dependências do projeto
│── README.md           # Documentação
│── .devcontainer/      # Configuração para Codespaces
```

---

## 👩‍💻 Autora

Feito com ❤️ por [@nandinhaaa](https://github.com/nandinhaaa)

---

# Previsão de Energia e Cluster - API de Regressão e Clusterização

## Descrição

Este projeto consiste em uma API desenvolvida com Flask que utiliza dois modelos de aprendizado de máquina: um modelo de Regressão para prever o percentual de energia renovável no futuro com base no consumo de energia renovável e de combustíveis fósseis, e um modelo de Clusterização para classificar os cenários energéticos com base em diferentes variáveis, como consumo de energia, investimentos em renováveis e PIB. A API permite que os usuários enviem dados por meio de requisições HTTP e obtenham previsões de energia e classificação em clusters.

## Tecnologias Utilizadas

- ![Flask](https://img.shields.io/badge/Flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) -> Framework para criação de APIs web.
- ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) -> Biblioteca para aprendizado de máquina (Machine Learning), utilizada para criar e treinar os modelos de Regressão e Clusterização.
- ![Pandas](https://img.shields.io/badge/Pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) -> Biblioteca para manipulação e análise de dados.
- ![NumPy](https://img.shields.io/badge/NumPy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) -> Biblioteca para cálculos numéricos.
- ![joblib](https://img.shields.io/badge/joblib-%23A7A8AA.svg?style=for-the-badge&logo=joblib&logoColor=white) -> Utilizada para salvar e carregar os modelos treinados.

## Funcionalidades

- **Previsão de Energia Renovável**: A API permite prever o percentual de energia renovável no futuro com base em dois parâmetros:
  - Consumo de energia renovável (%)
  - Consumo de energia de combustíveis fósseis (%)

- **Previsão de Cluster Energético**: A API também permite classificar um cenário energético em um dos clusters com base em variáveis como:
  - Energia Hidrelétrica (MW)
  - Energia Solar (MW)
  - Consumo Total de Energia (TWh)
  - Investimento em Renováveis (%)
  - PIB (US$ Bilhões)
  - Emissões de CO2 (Milhões de Toneladas)
  - Crescimento Econômico (%)

A previsão de cluster retorna um número representando o cluster ao qual o cenário pertence, com uma explicação associada para cada valor retornado (0, 1, 2, etc.).

## Como Usar

### Pré-requisitos

- Python 3.x
- Instalar as dependências do projeto

### Instalação

1. Clone este repositório para sua máquina local:
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use venv\Scripts\activate
    ```

3. Instale as dependências do projeto:
    ```bash
    pip install -r requirements.txt
    ```

### Executando a API

1. Inicie a aplicação Flask:
    ```bash
    python app.py
    ```

2. A API estará disponível no endereço:
    ```
    http://127.0.0.1:5000/
    ```

3. Inicie a inteface Streamlit executando:
    ```
    streamlit run app/app_streamlit.py
    ```

Após isso, a interface abrirá no seu navegador de preferência. Os campos já estarão preenchidos com informações pré-estabelecidas para testar a aplicação, entretanto, sinta-se a vontade para alterá-las!

# Obrigado!!

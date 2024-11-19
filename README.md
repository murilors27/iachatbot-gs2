Previsão de Energia e Cluster - API de Regressão e Clusterização
Descrição
Este projeto consiste em uma API desenvolvida com Flask que utiliza dois modelos de aprendizado de máquina: um modelo de Regressão para prever o percentual de energia renovável no futuro com base no consumo de energia renovável e de combustíveis fósseis, e um modelo de Clusterização para classificar os cenários energéticos com base em diferentes variáveis, como consumo de energia, investimentos em renováveis e PIB. A API permite que os usuários enviem dados por meio de requisições HTTP e obtenham previsões de energia e classificação em clusters.

Tecnologias Utilizadas
-> Framework para criação de APIs web.
-> Biblioteca para aprendizado de máquina (Machine Learning), utilizada para criar e treinar os modelos de Regressão e Clusterização.
-> Biblioteca para manipulação e análise de dados.
-> Biblioteca para cálculos numéricos.
-> Utilizada para salvar e carregar os modelos treinados.
Funcionalidades
Previsão de Energia Renovável: A API permite prever o percentual de energia renovável no futuro com base em dois parâmetros:

Consumo de energia renovável (%)
Consumo de energia de combustíveis fósseis (%)
Previsão de Cluster Energético: A API também permite classificar um cenário energético em um dos clusters com base em variáveis como:

Energia Hidrelétrica (MW)
Energia Solar (MW)
Consumo Total de Energia (TWh)
Investimento em Renováveis (%)
PIB (US$ Bilhões)
Emissões de CO2 (Milhões de Toneladas)
Crescimento Econômico (%)
A previsão de cluster retorna um número representando o cluster ao qual o cenário pertence, com uma explicação associada para cada valor retornado (0, 1, 2, etc.).

Como Usar
Pré-requisitos
Python 3.x
Instalar as dependências do projeto
Instalação
Clone este repositório para sua máquina local:

bash
Copiar código
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd iachatbot-gs2
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python -m venv venv
source venv/bin/activate  # No Windows, use venv\Scripts\activate
Instale as dependências do projeto:

bash
Copiar código
pip install -r requirements.txt
Executando a API
Inicie a aplicação Flask:

bash
Copiar código
python app.py
A API estará disponível no endereço:

arduino
Copiar código
http://127.0.0.1:5000/
Endpoint
POST /previsao_regressao
Este endpoint recebe um JSON com os dados de consumo de energia renovável e fósseis e retorna a previsão do percentual de energia renovável no futuro.

Exemplo de requisição:

json
Copiar código
{
  "renewables_consumption": 10.5,
  "fossil_fuel_consumption": 8.2
}
Exemplo de resposta:

json
Copiar código
{
  "previsao": 15.2,
  "mensagem": "A previsão é de que o percentual de energia renovável no futuro será 15.2%."
}
POST /previsao_cluster
Este endpoint recebe um JSON com as variáveis do cenário energético e retorna o número do cluster ao qual o cenário pertence, com uma explicação.

Exemplo de requisição:

json
Copiar código
{
  "hydroelectric_power": 50.3,
  "solar_energy": 20.1,
  "energy_consumption": 100,
  "investment_renewables": 5.2,
  "gdp": 300,
  "co2_emissions": 200,
  "economic_growth": 3.0
}
Exemplo de resposta:

json
Copiar código
{
  "cluster": 1
}
O cluster "1" significa que o cenário está em um grupo com equilíbrio entre energias renováveis e fósseis.

Como Treinar os Modelos
Treinamento do Modelo de Regressão
Execute o script para treinar o modelo de regressão:

bash
Copiar código
python treinamento_modelos.ipynb
O modelo será salvo como modelo_regressao.pkl no diretório /app.

Treinamento do Modelo de Clusterização
Execute o script para treinar o modelo de clusterização:

bash
Copiar código
python treinamento_modelos.ipynb
O modelo será salvo como modelo_cluster.pkl no diretório /app.

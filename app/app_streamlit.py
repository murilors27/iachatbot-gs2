import streamlit as st
import requests

# URL do seu servidor Flask, onde as APIs estão rodando
API_URL = 'http://127.0.0.1:5000'  # Modifique se estiver em outro IP ou porta

# Função para chamar a API de regressão
def previsao_regressao(renewables_consumption, fossil_fuel_consumption):
    url = f'{API_URL}/previsao_regressao'
    payload = {
        "renewables_consumption": renewables_consumption,
        "fossil_fuel_consumption": fossil_fuel_consumption
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data['previsao'], data['mensagem']
    else:
        return None, "Erro na API de Regressão."

# Função para chamar a API de cluster
def previsao_cluster(hidroeletrica, solar, consumo_energia, investimento_renovaveis, pib, emissao_co2, crescimento_economico):
    url = f'{API_URL}/previsao_cluster'
    payload = {
        "hydroelectric_power": hidroeletrica,
        "solar_energy": solar,
        "energy_consumption": consumo_energia,
        "investment_renewables": investimento_renovaveis,
        "gdp": pib,
        "co2_emissions": emissao_co2,
        "economic_growth": crescimento_economico
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data['cluster']
    else:
        return None, "Erro na API de Cluster."

# Interface Streamlit
st.title('Previsões de Energia e Cluster')
st.write(
    """
    Bem-vindo ao assistente de previsões! Escolha um tipo de previsão para ver os resultados baseados em inteligência artificial.

    - **Previsão de Regressão**: Informe os dados de consumo de energia renovável e de combustíveis fósseis para prever o percentual de energia renovável no futuro.
    - **Previsão de Cluster**: Informe informações sobre consumo de energia, investimentos em renováveis, PIB e outros fatores para descobrir a qual grupo (cluster) seu cenário pertence.
    """
)

# Opção de selecionar o tipo de previsão
opcao = st.selectbox('Escolha a previsão', ('Previsão de Regressão', 'Previsão de Cluster'))

if opcao == 'Previsão de Regressão':
    # Inputs para a regressão
    renovaveis_consumo = st.number_input('Consumo de Energia Renovável (%)', value=10.5)
    fossil_consumo = st.number_input('Consumo de Energia de Combustíveis Fósseis (%)', value=8.2)

    if st.button('Fazer Previsão de Regressão'):
        previsao, mensagem = previsao_regressao(renovaveis_consumo, fossil_consumo)
        if previsao:
            st.write(f'Previsão: {previsao} %')
            st.write(mensagem)
        else:
            st.write(mensagem)

elif opcao == 'Previsão de Cluster':
    # Inputs para o cluster
    hidroeletrica = st.number_input('Energia Hidrelétrica (MW)', value=50.3)
    solar = st.number_input('Energia Solar (MW)', value=20.1)
    consumo_energia = st.number_input('Consumo Total de Energia (TWh)', value=100)
    investimento_renovaveis = st.number_input('Investimento em Renováveis (%)', value=5.2)
    pib = st.number_input('PIB (US$ Bilhões)', value=300)
    emissao_co2 = st.number_input('Emissões de CO2 (Milhões de Toneladas)', value=200)
    crescimento_economico = st.number_input('Crescimento Econômico (%)', value=3.0)

    if st.button('Fazer Previsão de Cluster'):
        cluster = previsao_cluster(hidroeletrica, solar, consumo_energia, investimento_renovaveis, pib, emissao_co2, crescimento_economico)
        if cluster is not None:
            st.write(f'O cluster previsto é: {cluster}')
            
            # Explicação do que significa cada cluster
            if cluster == 0:
                st.write("O resultado 0 significa que o cenário está em um grupo com baixa sustentabilidade de energia renovável.")
            elif cluster == 1:
                st.write("O resultado 1 indica um grupo com equilíbrio entre energias renováveis e fósseis.")
            elif cluster == 2:
                st.write("O resultado 2 sugere que o cenário está em um grupo com grande investimento em energias renováveis.")
            else:
                st.write("Resultado inesperado. Tente ajustar os dados e tente novamente.")
        else:
            st.write("Erro ao fazer a previsão de cluster.")

'''
Api testada no POSTMAN.

Para o endpoint de regressão linear (/previsao_regressao):
{
  "renewables_consumption": 10.5,
  "fossil_fuel_consumption": 8.2,
  "greenhouse_gas_emissions": 5.7
}

Para o endpoint de cluster KMeans (/previsao_cluster):
{
  "hydroelectric_power": 50.3,
  "solar_energy": 20.1,
  "energy_consumption": 100.5,
  "investment_renewables": 5.2,
  "gdp": 20000,
  "co2_emissions": 350.5,
  "economic_growth": 2.3
}

Instalações necessárias:
pip install flask pandas numpy scikit-learn matplotlib

OBS.: CERTIFIQUE-SE QUE OS MODELOS ESTÃO NO MESMO DIRETÓRIO DESTE ARQUIVO (api.py)
'''

from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Carregar os modelos salvos
regressor = joblib.load('app/modelo_regressao_linear.pkl')
kmeans = joblib.load('app/modelo_kmeans.pkl')


@app.route('/previsao_regressao', methods=['POST'])
def previsao_regressao():
    # Recebe os dados via JSON
    dados = request.get_json()
    renovaveis_consumo = dados['renewables_consumption']
    fossil_consumo = dados['fossil_fuel_consumption']

    entrada = np.array([[renovaveis_consumo, fossil_consumo]])

    previsao = regressor.predict(entrada)

    # Formatar a previsão para 2 casas decimais
    previsao_formatada = "{:,.2f}".format(previsao[0])

    # Retorna a resposta com a previsão formatada
    return jsonify({
        'previsao': previsao_formatada,
        'mensagem': 'A previsão foi calculada com sucesso.'
    })


@app.route('/previsao_cluster', methods=['POST'])
def previsao_cluster():
    # Recebe os dados via JSON
    dados = request.get_json()
    
    # Atribui os valores das variáveis do JSON
    hidroeletrica = dados['hydroelectric_power']  # Energia gerada por hidrelétricas
    solar = dados['solar_energy']  # Energia gerada por energia solar
    consumo_energia = dados['energy_consumption']  # Consumo total de energia
    investimento_renovaveis = dados['investment_renewables']  # Investimento em fontes renováveis
    pib = dados['gdp']  # PIB do país ou região
    emissao_co2 = dados['co2_emissions']  # Emissões de CO2
    crescimento_economico = dados['economic_growth']  # Taxa de crescimento econômico
    
    # Prepara os dados para a previsão (formato de array para o modelo)
    entrada = np.array([[hidroeletrica, solar, consumo_energia, investimento_renovaveis, pib, emissao_co2, crescimento_economico]])

    # Faz a previsão de cluster com o modelo KMeans
    cluster = kmeans.predict(entrada)

    # Retorna o cluster previsto como resposta JSON
    return jsonify({'cluster': int(cluster[0])})


if __name__ == '__main__':
    app.run(debug=True)

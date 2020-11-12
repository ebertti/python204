import requests
response = requests.get('https://api.exchangeratesapi.io/latest')
dados = response.json()
print(dados['rates']['BRL'])

exemplo = {
    'rates' : {
        'BRL': 6.6
    }
}
print(exemplo['rates']['BRL'])

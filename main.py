import requests

def converter_moeda(valor, moeda_origem, moeda_destino):
    url = f"https://api.exchangerate-api.com/v4/latest/{moeda_origem.upper()}"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        raise Exception("Erro ao acessar API de câmbio")

    dados = resposta.json()
    taxas = dados.get("rates")

    if moeda_destino.upper() not in taxas:
        raise Exception("Moeda de destino não encontrada")

    taxa = taxas[moeda_destino.upper()]
    valor_convertido = valor * taxa
    return valor_convertido

    if name == "main":
        try:
            valor = float(input("Digite o valor: "))
            origem = input("Moeda de origem (ex: USD, BRL, EUR): ")
            destino = input("Moeda de destino (ex: USD, BRL, EUR): ")
    
            resultado = converter_moeda(valor, origem, destino)
            print(f"{valor:.2f} {origem.upper()} = {resultado:.2f} {destino.upper()}")
        except Exception as e:
            print("Erro:", e)

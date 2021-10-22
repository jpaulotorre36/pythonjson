import json

with open('C:/Users/joao.torre/Desktop/jogador.json') as f:
    jogador=json.load(f)


"""carros_json = '{"marca": "Honda","cor": "prata", "Modelo": "HRV"}'

carros = json.loads(carros_json)

print(carros["marca"])

for x in carros.values(): 
    print(x)


#for x in carros.items(): 
    print(x)

for x in carros: 
    print(x)


for k, x in carros.items(): 
    print(k, x)

for x in carros.values(): 
    print(k + "-" + x)"""



"""carro = {"marca": "Honda",
               "cor": "prata",  
               "Modelo": "HRV"
}

carro_json = json.dumps(carro)

print(carro)"""

"""carros_dictionary = {
    "marca": "honda",
    "modelo": "HRV",
    "cor": "prata"
 }

#dictionary -> objeto json  ->converte

carros_list=["honda", "volkswagem","ford", "fiat", "chevrolet"]
#list -> array json

carros_tupla=("honda", "volkwagem", "ford", "fiat", "chevrolet")
#tupla -> array json


carros_j=json.dumps(carros_dictionary, indent=4, separators=(":", "="), sort_keys=True)

print(carros_j)
print("-------------------------------------------------")
print(carros_list)
pritn("------------------------------------------------")"""

"""jogador_j = '{"nome": "JP", "time": "aviadores", "vivo": "True","energia": "100", "mochila": ["pederneira", "corda", "linha", "arame"], "aeronaves": [{"tipo": "transporte", "habilidade": "80"}, {"tipo": "ataque", "habilidade": "100"}]}'

jogador=json.loads(jogador_j)"""

print(jogador)

#chaves
for c in jogador:
    print(c)

#itens
for j in jogador.items():
    print(j)

for i in jogador.values():
    for j in range(0,1):
        print(i , j)


for a in jogador["aeronave"]:
    print(a)










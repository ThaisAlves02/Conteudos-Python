# Conversão de dic para json e vice versa
import json

# # abrindo um arquivo json
# # r(read) - leitura
# # "arquivo" é o nosso arquivo json
# # No json só aceita aspas duplas ""
 
# with open("json00.json", "r", encoding="utf-8") as arquivo:
#     dados = json.load(arquivo) # convertendo json para py.

# print(dados['nome'])

# convertendo de py para json
# dados = {'nome' : 'Júnior', 'idade' : 20, 'cidade': 'maranguape'}

# with open('novo_cadastro.json', 'w', encoding='utf-8') as arquivo:
#     json.dump(dados, arquivo, indent=4, ensure_ascii=False) 
#     #indent = para indentar o código
#     #ensure_ascii = ele permite a acentuação no arquivo json

# exercício
# 1 - ler o arquivo existente
with open("json00.json", "r", encoding="utf-8") as arquivo:
     dados = json.load(arquivo)

# 2 - Adicionar novo hobby na lista
dados['hobbies'].append('cozinhar')

# 3 - Salvar de volta no mesmo arquivo
with open('json00.json', 'w', encoding='utf-8') as arquivo:
     json.dump(dados, arquivo, indent=4, ensure_ascii=False) 
#listas









#dicionários
pessoa = {
    "nome": "Pedro",
    "idade": "13",
    "cidade": "Brasil"
}
print(pessoa["nome"])
pessoa["profissao"] = "programador"
pessoa["idade"] = 31


tarefa = {
    "descricao": "Estudar python",
    "pronta": False}

pessoas = {'nome': 'Gustavo',
'sexo': 'M',
'idade': 22}
del pessoas['sexo']
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')


status = "✅" if tarefa["pronta"] else " "
print(f"[{status}] {tarefa['descricao']}")


#Ex1:
alunos ={}
alunos['nome'] = str(input('nome: '))
alunos['média'] = float(input(f'Média de {alunos["nome"]}'))


if alunos['média'] >= 7:
    alunos['situação'] = 'Aprovado' 

elif  5 <= alunos['média']  < 7:
    alunos['situação'] = 'Recuperação'

elif alunos['média' ] < 5:
    alunos['situação'] = 'Reprovado'

print('-=' * 20)
for chave, valor in alunos.items():
    print(f'{chave} é igual a {valor}')

#Ex2:
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador 1': randint(1, 6), 
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}

ranking = sorted(jogo.items(), key=itemgetter(1), reverse= True)

for j, d in jogo.items():
    print(f'o {j} tirou {d}')
    sleep(2)
print('>--<'*20)
for i, v in enumerate(ranking):
    print(f'O {i+1} lugar é do {v[0]} com {v[1]}')
    sleep(1)
    





#listas de dicionários
# Começamos com uma lista vazia. O programa não sabe quantas tarefas vão existir.
lista_de_tarefas = []

while True: # Um loop infinito para o programa continuar a correr
    # O utilizador decide qual é a nova tarefa
    novo_titulo = input("Digita o nome da nova tarefa (ou 'sair' para terminar): ")
    
    if novo_titulo == 'sair':
        break
        
    # O Python constrói o dicionário NA HORA, usando o texto que o utilizador digitou
    nova_tarefa = {
        "titulo": novo_titulo,
        "pronta": False
    }
    
    # Colocamos o novo dicionário dentro da nossa lista vazia
    lista_de_tarefas.append(nova_tarefa)
    print("Tarefa adicionada!")
    print(lista_de_tarefas)

usuario = {}
usuario["email"] = "carlos@email.com"
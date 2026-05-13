#listas
valores = [['pedro', 25],['marcela', 18],['jefferson', 10]]
lista=[]
valores.append(lista)
print(valores[1][1])









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

#listas de dicionários

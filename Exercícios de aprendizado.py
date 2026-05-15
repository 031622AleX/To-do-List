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


#Ex:
alunos ={}
alunos['nome'] = str(input('nome: '))
alunos['média'] = float(input(f'Média de {alunos["nome"]}'))


if alunos['média'] >= 7:
    alunos['situação'] = 'Aprovado' 

elif  5 <= alunos['média']  < 7:
    alunos['situação'] = 'Recuperação'

elif alunos['média' ] < 5:
    alunos['situação'] = 'Reprovado'
print(alunos)
#listas de dicionários

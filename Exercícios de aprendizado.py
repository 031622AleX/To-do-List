
pessoas = [['pedro', 25],['marcela', 18],['jefferson', 10]]
lista=[]
pessoas.append(lista)
print(pessoas[1][1])


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
    "pronta": False


}
status = "✅" if tarefa["pronta"] else " "
print(f"[{status}] {tarefa['descricao']}")

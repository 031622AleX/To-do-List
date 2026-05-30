#Meta: Construir Programa totalmente funcional em Python
import json
import os
import time

def salvar_tarefa(lista_de_tarefas):
   # 'with' abre o arquivo e garante que ele será fechado com segurança mesmo se der erro
   # 'w' significa write (escrita). Se o arquivo não existir, o Pyrhon cria ele sozinho
  with open("tarefas.json", "w", encoding="utf-8") as arquivo:
   # dump: joga a lista dentro do arquivo.
   # indent=2 faz o arquivo ficar quebrado em linhas e bonito de ler
   json.dump(lista_de_tarefas, arquivo, indent=2, ensure_ascii=False)

def carrefar_tarefas():
   # Seo arquivo tarefas.json existir...
   if os.path.exists("tarefas.json"):
     # Abre o arquivo em modo 'r' (read - leitura)
     with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            # Carrega o texto e transforma de volta em lista do Python
            return json.load(arquivo)
# Se o arquivo não existir (primeira execução), retorna uma lista vazia
   return []

def cronometro ():
  horas = 0
  minutos = 0
  segundos = 0 
  print('Amassa filhote!')
  
  try:
  
    while True:
        print(f'{horas:02d}:{minutos:02d}:{segundos:02d}', end="\r")
        time.sleep(1)
        segundos += 1


        if segundos == 60:
            segundos = 0
            minutos += 1

        if minutos == 60:
            minutos = 0
            horas += 1
  except KeyboardInterrupt:
      print("\nCronômetro Finalizado!")


lista_de_tarefas = carregar_tarefas()
while True:
  try:
    menu = int(input("""Olá, senhor!
    Bem vindo ao guia de estudo e tarefas que fui programado para exercer!
    O que o senhor gostaria de fazer?
    [ 1 ] Escrever uma atividade
    [ 2 ] Ver suas atividades
    [ 3 ] Marcar alguma atividade como concluída
    [ 4 ] Colocar um cronômetro para uma das atividades
    [ 5 ] Terminar o programa""").strip())
  
  except ValueError:
    print("❌Descreva o que deseja de 1 a 5")
    continue

  if menu == 1:
    while True:
      atividade = input('Digite sua atividade')
      lista = {
        "tarefa": atividade,
        "pronta": False
      }
      lista_de_tarefas.append(lista)
      mais_atividade = input('Tem mais atividades? (s/n)').lower().strip()
      
      if mais_atividade == 'n':
        break
      

  elif menu == 2:
    
    if not lista_de_tarefas:
      print('Sem atividades no momento')
      continue

    else:
      print("\nSuas atividdes:")
      for i, tarefa in enumerate(lista_de_tarefas, 1):
          status = "✅" if tarefa["pronta"] else " "
          print(f"  [{status}] {i}. {tarefa['tarefa']}")


  elif menu == 3:
    
    if not lista_de_tarefas:
      print('Não há tarefas para concluir')
    
    else:
      print("\nSuas atividdes:")
      for i, tarefa in enumerate(lista_de_tarefas, 1):
          status = "✅" if tarefa["pronta"] else " "
          print(f"  [{status}] {i}. {tarefa['tarefa']}")

      try:
        numero = int(input("\nQual número deseja concluir? "))

        if 1 <= numero <= len(lista_de_tarefas):
          lista_de_tarefas[numero - 1]["pronta"] = True
          
          nome = lista_de_tarefas[numero -1]["tarefa"]
          print(f'✅"{nome}" marcada como concluída')

        
        else:
          print(f'❌ Digite um número entre 1 e {len(lista_de_tarefas)}')

      except ValueError:
        print('❌ Precisa digitar um número!')
      
                      


  elif menu == 4:
      
    cronometro()

  
  elif menu == 5:
    print('Okay, bom trabalho para ti')
    break    
        
        
  menu_ou_fim = input('Deseja voltar ao menu?(s/n)').lower().strip()
  if menu_ou_fim == 'n':
    print('Okay, bom trabalho para ti')
    break
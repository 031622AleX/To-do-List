#Meta: Construir Programa totalmente funcional em Python
import time
atividades = []
while True:
  menu = int(input("""Olá, senhor!
  Bem vindo ao guia de estudo e tarefas que fui programado para exercer!
  O que o senhor gostaria de fazer?
  [ 1 ] Escrever uma atividade
  [ 2 ] Ver suas atividades
  [ 3 ] Marcar alguma atividade como concluída
  [ 4 ] Colocar um cronômetro para uma das atividades
  [ 5 ] Terminar o programa""").strip())

  if menu == 1:
    while True:
      atividade = input('Digite sua atividade')
      atividades.append(atividade)
      print('=~'*20)
    
      mais_atividade = input('Tem mais atividades? (s/n)').lower().strip()
      
      if mais_atividade == 'n':
        break

  elif menu == 2:
    
    if not atividades:
      print('Sem atividades no momento')
      continue

    else:
      print(f'Suas atividades são: {atividades}')


  elif menu == 3:
    indice = int(input("Qual tarefa deseja concluir? "))
    if 0 <= indice < len(atividades):
        atividades[indice]["concluida"] = True
    else:
        print("Índice inválido")


  elif menu == 4:
    horas = 0
    minutos = 0
    segundos = 0 
    print('Amassa filhote!')
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

  elif menu == 5:
     print('Okay, bom trabalho para ti')
     break    
        
        
  menu_ou_fim = input('Deseja voltar ao menu?(s/n)').lower().strip()
  if menu_ou_fim == 'n':
    print('Okay, bom trabalho para vossa senhoria')
    break

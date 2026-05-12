# 🎓 APRENDENDO PYTHON DESDE ZERO
## Construindo um To Do List Passo a Passo

---

## 🎯 OBJETIVO FINAL
Você vai criar um **programa completo de To Do List** que:
- ✅ Adiciona e lista tarefas
- ✅ Marca tarefas como concluídas
- ✅ Usa cronômetro
- ✅ Salva dados

**Sem copiar código pronto - você vai entender CADA LINHA!**

---

## 📚 PRÉ-REQUISITOS

### O que você precisa saber?
- Variáveis e tipos de dados (int, str, list, dict)
- Loops (while, for)
- Condicionais (if, elif, else)
- Funções básicas

### Você não sabe? Não tem problema!
Vamos revisar conforme necessário.

---

## 🏗️ ESTRUTURA DO PROJETO

Vamos construir em **4 fases**:

```
FASE 1: Conceitos Básicos (30 min)
  └─ Entender listas e dicionários
  
FASE 2: Menu Simples (30 min)
  └─ Menu interativo no terminal
  
FASE 3: Adicionar Tarefas (45 min)
  └─ Criar, listar, marcar como pronta
  
FASE 4: Cronômetro Pomodoro (1h)
  └─ Implementar timer
```

**Tempo total: ~2h30min** ⏱️

---

## FASE 1️⃣: CONCEITOS BÁSICOS

### 1.1 - Entender Listas vs Dicionários

**Problema**: Como armazenar várias tarefas?

#### Tentativa 1: Usando Variáveis (❌ RUIM)
```python
tarefa1 = "Estudar Python"
tarefa2 = "Fazer exercício"
tarefa3 = "Ler livro"

# Problema: 100 tarefas = 100 variáveis 😞
```

#### Tentativa 2: Usando Lista (✅ BOM para dados simples)
```python
tarefas = ["Estudar Python", "Fazer exercício", "Ler livro"]

print(tarefas[0])  # Mostra: Estudar Python
print(tarefas)     # Mostra: ['Estudar Python', 'Fazer exercício', 'Ler livro']

# Problema: E se quisermos saber qual está pronta?
```

#### Tentativa 3: Usando Dicionários (✅ MELHOR para dados complexos)
```python
# Uma tarefa com mais informações
tarefa = {
    "nome": "Estudar Python",
    "pronta": False,
    "prioridade": "Alta"
}

# Acessar dados
print(tarefa["nome"])        # Mostra: Estudar Python
print(tarefa["pronta"])      # Mostra: False

# Modificar dados
tarefa["pronta"] = True
print(tarefa)  # Mostra: {'nome': 'Estudar Python', 'pronta': True, 'prioridade': 'Alta'}
```

#### Tentativa 4: Lista de Dicionários (✅ PERFEITO!)
```python
tarefas = [
    {"nome": "Estudar Python", "pronta": False, "prioridade": "Alta"},
    {"nome": "Fazer exercício", "pronta": True, "prioridade": "Média"},
    {"nome": "Ler livro", "pronta": False, "prioridade": "Baixa"}
]

# Adicionar nova tarefa
nova_tarefa = {"nome": "Estudar JavaScript", "pronta": False, "prioridade": "Alta"}
tarefas.append(nova_tarefa)

# Listar todas
for tarefa in tarefas:
    print(f"- {tarefa['nome']} (Pronta: {tarefa['pronta']})")

# Resultado:
# - Estudar Python (Pronta: False)
# - Fazer exercício (Pronta: True)
# - Ler livro (Pronta: False)
# - Estudar JavaScript (Pronta: False)
```

---

### 1.2 - SEU PRIMEIRO EXERCÍCIO

📝 **Crie um arquivo chamado `aula_01.py` e escreva:**

```python
# Sua lista de tarefas
tarefas = [
    {"nome": "Acordar cedo", "pronta": True},
    {"nome": "Tomar café", "pronta": True},
    {"nome": "Estudar Python", "pronta": False}
]

# Mostre todas as tarefas
print("Minhas tarefas:")
for tarefa in tarefas:
    # TODO: Complete o código abaixo
    # Dica: use a estrutura if/else para mostrar ✓ ou ✗
    print(f"  [ ] {tarefa['nome']}")

# Resultado esperado:
# Minhas tarefas:
#   [✓] Acordar cedo
#   [✓] Tomar café
#   [ ] Estudar Python
```

**Desafio**: Substitua `[ ]` por `[✓]` se a tarefa está pronta, `[ ]` se não está.

<details>
<summary>💡 Solução (clique para ver)</summary>

```python
for tarefa in tarefas:
    status = "✓" if tarefa["pronta"] else " "
    print(f"  [{status}] {tarefa['nome']}")
```

**Explicação:**
- `if tarefa["pronta"]` = verifica se é True
- `"✓" if ... else " "` = ternário (if em uma linha)

</details>

---

### 1.3 - Adicionando Tarefas (Introdução)

```python
# Começar com lista vazia
tarefas = []

# Adicionar tarefas
nova_tarefa = {
    "nome": "Estudar",
    "pronta": False
}
tarefas.append(nova_tarefa)

print(tarefas)  # [{'nome': 'Estudar', 'pronta': False}]
```

**Por que `append()`?**
- `append()` = adiciona um item ao final da lista
- Alternativa ruim: `tarefas = tarefas + [nova_tarefa]` (lento)

---

### 1.4 - Loop While para Repetir

Você quer adicionar várias tarefas, certo? Use `while`:

```python
tarefas = []

while True:
    nome = input("Digite uma tarefa (ou 'sair'): ")
    
    if nome == "sair":
        break  # Sai do loop
    
    tarefa = {"nome": nome, "pronta": False}
    tarefas.append(tarefa)
    print(f"✅ Tarefa '{nome}' adicionada!")

print(f"\nTotal de tarefas: {len(tarefas)}")
```

**Entendendo o código:**
- `while True` = loop infinito (até encontrar `break`)
- `input()` = pede texto do usuário
- `break` = sai do loop
- `len(tarefas)` = quantidade de tarefas

---

## ✅ CHECKPOINT 1

Você consegue:
- [ ] Criar uma lista de dicionários?
- [ ] Adicionar itens com `append()`?
- [ ] Usar `for` para listar tarefas?
- [ ] Usar `while True` para loops?
- [ ] Usar `if/else` para condições?

**Se respondeu SIM para todos**, está pronto para a FASE 2! 🚀

---

## FASE 2️⃣: MENU INTERATIVO

### 2.1 - Estrutura Básica do Menu

```python
while True:
    # Mostrar menu
    print("\n" + "="*40)
    print("MINHA TO DO LIST")
    print("="*40)
    print("[1] Adicionar tarefa")
    print("[2] Ver tarefas")
    print("[3] Sair")
    print("="*40)
    
    # Pedir escolha
    escolha = input("O que você quer fazer? ").strip()
    
    # Processar escolha
    if escolha == "1":
        print("Você escolheu ADICIONAR")
        # TODO: Adicionar código aqui
    
    elif escolha == "2":
        print("Você escolheu VER TAREFAS")
        # TODO: Adicionar código aqui
    
    elif escolha == "3":
        print("Até logo!")
        break
    
    else:
        print("❌ Opção inválida!")
```

**Conceitos novos:**
- `print("\n" + "="*40)` = pula linha + 40 "="
- `.strip()` = remove espaços antes/depois
- `elif` = "else if" (outra condição)

---

### 2.2 - SEU EXERCÍCIO: Complete o Menu

📝 **Crie `aula_02.py` com o menu acima e:**

1. Adicione um print quando escolher [2]
2. Faça o programa pedir "Qual tarefa você quer adicionar?" quando escolher [1]
3. Armazene essa tarefa em uma lista

<details>
<summary>💡 Dica</summary>

```python
elif escolha == "1":
    nome = input("Qual tarefa você quer adicionar? ")
    # TODO: Crie um dicionário e adicione na lista
```

</details>

---

### 2.3 - Melhorando o Menu com Funções

Conforme o código cresce, fica confuso. Use **funções**:

```python
def mostrar_menu():
    """Mostra o menu no terminal"""
    print("\n" + "="*40)
    print("MINHA TO DO LIST")
    print("="*40)
    print("[1] Adicionar tarefa")
    print("[2] Ver tarefas")
    print("[3] Sair")
    print("="*40)

def adicionar_tarefa(tarefas):
    """Adiciona uma nova tarefa à lista"""
    nome = input("Digite o nome da tarefa: ").strip()
    
    if not nome:  # Se estiver vazio
        print("❌ Tarefa não pode estar vazia!")
        return
    
    tarefa = {
        "nome": nome,
        "pronta": False
    }
    tarefas.append(tarefa)
    print(f"✅ Tarefa '{nome}' adicionada!")

def listar_tarefas(tarefas):
    """Mostra todas as tarefas"""
    if not tarefas:  # Se lista vazia
        print("📭 Nenhuma tarefa ainda!")
        return
    
    print("\n📋 SUAS TAREFAS:")
    for i, tarefa in enumerate(tarefas, 1):  # Começa em 1
        status = "✓" if tarefa["pronta"] else " "
        print(f"  [{status}] {i}. {tarefa['nome']}")

# Loop principal
tarefas = []

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ").strip()
    
    if escolha == "1":
        adicionar_tarefa(tarefas)
    elif escolha == "2":
        listar_tarefas(tarefas)
    elif escolha == "3":
        print("Até logo!")
        break
    else:
        print("❌ Opção inválida!")
```

**Benefícios das funções:**
- ✅ Código mais limpo
- ✅ Fácil de reutilizar
- ✅ Mais fácil de debugar
- ✅ Melhor organização

**Novos conceitos:**
- `def nomeFuncao():` = define função
- `return` = sai da função
- `enumerate(lista, 1)` = lista com índice (começando em 1)

---

### 2.4 - SEU EXERCÍCIO: Refatore com Funções

Pegue seu código de `aula_02.py` e:
1. Crie função `mostrar_menu()`
2. Crie função `adicionar_tarefa(tarefas)`
3. Crie função `listar_tarefas(tarefas)`
4. Organize o loop principal

---

## ✅ CHECKPOINT 2

Você consegue:
- [ ] Criar funções com `def`?
- [ ] Passar listas como argumentos?
- [ ] Usar `enumerate()` para numeração?
- [ ] Validar entrada vazia com `if not`?

**Se SIM**, pode ir para FASE 3! 🎉

---

## FASE 3️⃣: COMPLETAR TAREFAS

### 3.1 - Marcando como Pronta

**Novo requisito**: Você quer marcar tarefas como prontas!

```python
def marcar_pronta(tarefas):
    """Marca uma tarefa como pronta"""
    if not tarefas:
        print("📭 Nenhuma tarefa!")
        return
    
    # Mostrar tarefas
    listar_tarefas(tarefas)
    
    # Pedir qual marcar
    try:
        numero = int(input("\nQual tarefa completou? (número): "))
        
        # Verificar se número é válido
        if 1 <= numero <= len(tarefas):
            tarefas[numero - 1]["pronta"] = True
            print("✅ Tarefa marcada como pronta!")
        else:
            print(f"❌ Digite um número entre 1 e {len(tarefas)}")
    
    except ValueError:
        print("❌ Precisa ser um número!")

# Adicionar ao menu principal
elif escolha == "3":
    marcar_pronta(tarefas)
elif escolha == "4":
    print("Até logo!")
    break
```

**Novos conceitos:**
- `try/except` = trata erros (se usuário digitar texto em vez de número)
- `tarefas[numero - 1]` = acessa tarefa (índice começa em 0)
- `1 <= numero <= len(tarefas)` = valida se está no intervalo

---

### 3.2 - Deletando Tarefas

```python
def deletar_tarefa(tarefas):
    """Remove uma tarefa"""
    if not tarefas:
        print("📭 Nenhuma tarefa!")
        return
    
    listar_tarefas(tarefas)
    
    try:
        numero = int(input("\nQual tarefa quer deletar? (número): "))
        
        if 1 <= numero <= len(tarefas):
            nome = tarefas[numero - 1]["nome"]
            tarefas.pop(numero - 1)  # Remove
            print(f"🗑️  Tarefa '{nome}' deletada!")
        else:
            print(f"❌ Digite um número entre 1 e {len(tarefas)}")
    
    except ValueError:
        print("❌ Precisa ser um número!")
```

**Novo conceito:**
- `list.pop(índice)` = remove item da lista

---

### 3.3 - SEU EXERCÍCIO: Integre Tudo

📝 **Crie `aula_03.py` com:**
1. Função `mostrar_menu()` com opções 1-5
2. Função `adicionar_tarefa()`
3. Função `listar_tarefas()`
4. Função `marcar_pronta()`
5. Função `deletar_tarefa()`
6. Loop principal processando tudo

**Menu esperado:**
```
[1] Adicionar tarefa
[2] Ver tarefas
[3] Marcar como pronta
[4] Deletar tarefa
[5] Sair
```

---

## ✅ CHECKPOINT 3

Você consegue:
- [ ] Usar `try/except` para validação?
- [ ] Usar `list.pop()` para deletar?
- [ ] Validar índices (1 <= x <= len)?
- [ ] Integrar múltiplas funções?

**Se SIM**, pode ir para FASE 4! ⏱️

---

## FASE 4️⃣: CRONÔMETRO POMODORO

### 4.1 - Entendendo o Cronômetro

```python
import time  # Importa módulo para "dormir"

# Cronômetro simples (10 segundos)
print("Começando cronômetro de 10 segundos...")

for segundo in range(10, 0, -1):  # De 10 até 1
    print(f"⏳ {segundo} segundos...", end="\r")  # \r = volta pro início
    time.sleep(1)  # Espera 1 segundo

print("✅ Tempo acabou!")
```

**Entendendo:**
- `range(10, 0, -1)` = começa em 10, vai até 1 (indo para trás)
- `end="\r"` = volta pro início da linha (não cria nova linha)
- `time.sleep(1)` = espera 1 segundo

---

### 4.2 - Convertendo Minutos em Segundos

**Objetivo**: Pomodoro tem 25 minutos. Como fazer?

```python
def cronometro_pomodoro():
    """Cronômetro de 25 minutos"""
    import time
    
    minutos = 25
    segundos_totais = minutos * 60  # 25 * 60 = 1500 segundos
    
    print(f"🎯 Começando sessão de foco ({minutos} minutos)...")
    
    while segundos_totais > 0:
        # Converter para formato hh:mm:ss
        horas = segundos_totais // 3600
        mins = (segundos_totais % 3600) // 60
        segs = segundos_totais % 60
        
        print(f"⏳ {horas:02d}:{mins:02d}:{segs:02d}", end="\r")
        
        time.sleep(1)
        segundos_totais -= 1
    
    print("\n🎉 Sessão concluída!")

# Chamar
cronometro_pomodoro()
```

**Novas fórmulas:**
- `horas = segundos_totais // 3600` = quantas horas? (divisão inteira)
- `mins = (segundos_totais % 3600) // 60` = quantos minutos restantes?
- `segs = segundos_totais % 60` = quantos segundos restantes?
- `{horas:02d}` = formata para 2 dígitos com zeros à esquerda (01, 02, etc)

---

### 4.3 - Opções de Pomodoro

```python
def menu_pomodoro():
    """Menu para escolher duração do Pomodoro"""
    print("\n" + "="*40)
    print("⏱️  POMODORO")
    print("="*40)
    print("[1] Sessão de foco (25 min)")
    print("[2] Intervalo curto (5 min)")
    print("[3] Intervalo longo (15 min)")
    print("[4] Personalizado")
    print("="*40)
    
    escolha = input("Escolha uma opção: ").strip()
    
    if escolha == "1":
        iniciar_cronometro(25)
    elif escolha == "2":
        iniciar_cronometro(5)
    elif escolha == "3":
        iniciar_cronometro(15)
    elif escolha == "4":
        minutos = int(input("Quantos minutos? "))
        iniciar_cronometro(minutos)
    else:
        print("❌ Opção inválida!")

def iniciar_cronometro(minutos):
    """Inicia cronômetro por N minutos"""
    import time
    
    segundos_totais = minutos * 60
    
    print(f"\n🎯 Começando cronômetro de {minutos} minutos...")
    print("Pressione Ctrl+C para parar\n")
    
    try:
        while segundos_totais > 0:
            horas = segundos_totais // 3600
            mins = (segundos_totais % 3600) // 60
            segs = segundos_totais % 60
            
            print(f"⏳ {horas:02d}:{mins:02d}:{segs:02d}", end="\r")
            
            time.sleep(1)
            segundos_totais -= 1
        
        print("\n🎉 Tempo acabou!")
        
    except KeyboardInterrupt:
        print("\n⏸️  Cronômetro pausado!")
```

**Novo conceito:**
- `try/except KeyboardInterrupt` = pega quando usuário pressiona Ctrl+C

---

### 4.4 - SEU EXERCÍCIO: Integre o Pomodoro

📝 **Atualize `aula_03.py` com:**
1. Adicione opção [6] ao menu principal para "Pomodoro"
2. Implemente `menu_pomodoro()`
3. Implemente `iniciar_cronometro(minutos)`

---

## ✅ CHECKPOINT 4 - FINAL

Você consegue:
- [ ] Entender `range()` com passo negativo?
- [ ] Converter minutos em segundos?
- [ ] Usar `//` e `%` para cálculos?
- [ ] Formatar números com `{:02d}`?
- [ ] Tratar `KeyboardInterrupt`?

---

## 🎉 VOCÊ TERMINOU!

Parabéns! Você construiu um **To Do List completo**! 

Seu programa pode:
✅ Adicionar tarefas
✅ Listar tarefas
✅ Marcar como pronta
✅ Deletar tarefas
✅ Usar cronômetro Pomodoro

---

## 🚀 PRÓXIMOS PASSOS

### Melhorias que você pode fazer sozinho:
1. **Adicionar prioridades** (Alta/Média/Baixa)
2. **Salvar em arquivo** (JSON)
3. **Adicionar datas** (quando foi criada)
4. **Criar classes** (POO) - mais profissional

### Quer aprender essas melhorias?
Avance para `02_APRENDIZADO_PYTHON_AVANCADO.md` 👉

---

## 📚 REFERÊNCIA RÁPIDA

```python
# Listas
lista = [1, 2, 3]
lista.append(4)        # Adiciona
lista.pop(0)           # Remove índice 0
len(lista)             # Tamanho

# Dicionários
dicionario = {"nome": "João", "idade": 25}
dicionario["nome"]     # Acessa "João"
dicionario["nome"] = "Maria"  # Modifica

# Funções
def nome_funcao(parametro):
    return parametro * 2

# Loops
for item in lista:
    print(item)

while True:
    if condicao:
        break

# Try/Except
try:
    numero = int(input())
except ValueError:
    print("Erro!")

# Importar módulos
import time
time.sleep(1)
```

---

**Boa sorte! Qualquer dúvida, me chama! 🚀**

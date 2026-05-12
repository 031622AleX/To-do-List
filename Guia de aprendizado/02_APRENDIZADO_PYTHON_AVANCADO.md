# 🚀 APRENDENDO PYTHON AVANÇADO
## Melhorando seu To Do List com Conceitos Pro

---

## 📌 O QUE VOCÊ VAI APRENDER

Depois de completar a FASE 1-4, você vai adicionar:

1. **JSON** - Salvar dados permanentemente
2. **Classes (POO)** - Organizar código profissionalmente
3. **Prioridades** - Sistema inteligente de tarefas
4. **Datas** - Rastrear quando foi criada
5. **Relatórios** - Análises de produtividade

---

## FASE 5️⃣: SALVANDO EM JSON

### 5.1 - O que é JSON?

JSON = dados estruturados em arquivo `.json`

**Exemplo de `tarefas.json`:**
```json
[
  {
    "nome": "Estudar Python",
    "pronta": false,
    "prioridade": "Alta",
    "data": "21/04/2026"
  },
  {
    "nome": "Fazer exercício",
    "pronta": true,
    "prioridade": "Média",
    "data": "20/04/2026"
  }
]
```

**Por que JSON?**
- ✅ Organizado e legível
- ✅ Python consegue ler e escrever fácil
- ✅ Dados persistem (não perdem quando fecha)

---

### 5.2 - Escrevendo em JSON

```python
import json

# Suas tarefas (como listas de dicionários)
tarefas = [
    {"nome": "Estudar", "pronta": False, "prioridade": "Alta"},
    {"nome": "Exercício", "pronta": True, "prioridade": "Média"}
]

# SALVAR em arquivo
def salvar_tarefas(tarefas):
    """Salva tarefas no arquivo JSON"""
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent=2)
        # indent=2 = deixa bonito com 2 espaços

salvar_tarefas(tarefas)

# Resultado: arquivo "tarefas.json" é criado!
```

**Entendendo:**
- `open("tarefas.json", "w")` = abre arquivo para escrever
- `"w"` = write (escrever). Outras opções: "r" (ler), "a" (adicionar)
- `json.dump()` = converte Python em JSON
- `with ... as ...` = abre e fecha automaticamente
- `indent=2` = formata com 2 espaços (fica bonito)

---

### 5.3 - Lendo de JSON

```python
import json
import os  # Para verificar se arquivo existe

def carregar_tarefas():
    """Carrega tarefas do arquivo JSON"""
    # Verificar se arquivo existe
    if os.path.exists("tarefas.json"):
        with open("tarefas.json", "r") as arquivo:
            tarefas = json.load(arquivo)
            return tarefas
    else:
        # Se não existe, retorna lista vazia
        return []

# Usar
tarefas = carregar_tarefas()
print(tarefas)
```

**Entendendo:**
- `os.path.exists()` = verifica se arquivo existe
- `json.load()` = lê arquivo JSON e converte em Python

---

### 5.4 - Integrando ao Seu Programa

```python
import json
import os

# Inicializar
tarefas = []

def carregar_tarefas():
    """Carrega tarefas do arquivo"""
    if os.path.exists("tarefas.json"):
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    return []

def salvar_tarefas():
    """Salva tarefas no arquivo"""
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent=2)

# No começo do programa:
tarefas = carregar_tarefas()

# Sempre que adicionar/remover, salvar:
def adicionar_tarefa(tarefas):
    nome = input("Tarefa: ").strip()
    
    if not nome:
        print("❌ Vazio!")
        return
    
    tarefa = {"nome": nome, "pronta": False, "prioridade": "Média"}
    tarefas.append(tarefa)
    
    salvar_tarefas()  # 👈 SALVA!
    print(f"✅ Adicionada e salva!")

def deletar_tarefa(tarefas):
    # ... código ...
    tarefas.pop(numero - 1)
    salvar_tarefas()  # 👈 SALVA!

def marcar_pronta(tarefas):
    # ... código ...
    tarefas[numero - 1]["pronta"] = True
    salvar_tarefas()  # 👈 SALVA!
```

---

### 5.5 - SEU EXERCÍCIO: Integre JSON

📝 **Atualize `aula_04.py`:**
1. Importe `json` e `os`
2. Crie função `carregar_tarefas()`
3. Crie função `salvar_tarefas(tarefas)`
4. Chame `carregar_tarefas()` no início
5. Chame `salvar_tarefas()` em cada mudança

**Teste:**
- Adicione uma tarefa
- Feche o programa
- Abra novamente
- A tarefa ainda está lá? ✅

---

## ✅ CHECKPOINT 5

Você consegue:
- [ ] Entender estrutura JSON?
- [ ] Usar `json.dump()` e `json.load()`?
- [ ] Verificar se arquivo existe com `os.path.exists()`?
- [ ] Integrar persistência ao programa?

---

## FASE 6️⃣: CLASSES (POO)

### 6.1 - Por que Classes?

Seu código atual:
```python
def adicionar_tarefa(tarefas):  # Passa tarefas
    ...

def listar_tarefas(tarefas):    # Passa tarefas
    ...

def marcar_pronta(tarefas):     # Passa tarefas
    ...

# 😞 Muito repetitivo passar "tarefas" todo tempo
```

Com Classes:
```python
class TodoList:
    def __init__(self):
        self.tarefas = []  # Armazenado na classe
    
    def adicionar_tarefa(self):  # Sem passar tarefas!
        self.tarefas.append(...)
    
    def listar_tarefas(self):    # Acessa self.tarefas
        for t in self.tarefas:
            ...
```

**Benefícios:**
- ✅ Código mais profissional
- ✅ Menos repetição
- ✅ Mais fácil de entender

---

### 6.2 - Entendendo Classes

```python
# Classe simples
class Pessoa:
    def __init__(self, nome, idade):
        """Construtor - rodado quando cria objeto"""
        self.nome = nome      # Atributo
        self.idade = idade
    
    def apresentar(self):
        """Método - função dentro da classe"""
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos"

# Usando a classe
joao = Pessoa("João", 25)
print(joao.apresentar())  # Olá, meu nome é João e tenho 25 anos

maria = Pessoa("Maria", 30)
print(maria.apresentar())  # Olá, meu nome é Maria e tenho 30 anos
```

**Entendendo:**
- `class NomeDaClasse:` = cria classe
- `def __init__(self, ...)` = construtor (rodado ao criar `Pessoa()`)
- `self` = referência ao objeto atual
- `self.nome` = atributo (dado armazenado)
- `def metodo(self)` = método (função)

---

### 6.3 - Convertendo seu Programa para Classe

**Antes (funções soltas):**
```python
tarefas = []

def adicionar_tarefa(tarefas):
    nome = input("Tarefa: ")
    tarefas.append({"nome": nome, "pronta": False})

def listar_tarefas(tarefas):
    for t in tarefas:
        print(t["nome"])
```

**Depois (classe):**
```python
import json
import os

class TodoList:
    def __init__(self):
        """Construtor - rodado ao criar TodoList()"""
        self.tarefas = []
        self.arquivo = "tarefas.json"
        self.carregar()  # Carrega dados antigos
    
    def carregar(self):
        """Carrega tarefas do arquivo JSON"""
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r") as f:
                self.tarefas = json.load(f)
    
    def salvar(self):
        """Salva tarefas no arquivo JSON"""
        with open(self.arquivo, "w") as f:
            json.dump(self.tarefas, f, indent=2)
    
    def adicionar_tarefa(self):
        """Adiciona nova tarefa"""
        nome = input("Nome da tarefa: ").strip()
        
        if not nome:
            print("❌ Vazio!")
            return
        
        tarefa = {
            "nome": nome,
            "pronta": False,
            "prioridade": "Média"
        }
        
        self.tarefas.append(tarefa)
        self.salvar()  # Salva automaticamente
        print(f"✅ '{nome}' adicionada!")
    
    def listar_tarefas(self):
        """Lista todas as tarefas"""
        if not self.tarefas:
            print("📭 Nenhuma tarefa!")
            return
        
        print("\n📋 TAREFAS:")
        for i, t in enumerate(self.tarefas, 1):
            status = "✓" if t["pronta"] else " "
            print(f"  [{status}] {i}. {t['nome']}")
    
    def marcar_pronta(self):
        """Marca tarefa como pronta"""
        self.listar_tarefas()
        
        try:
            num = int(input("Qual completou? "))
            if 1 <= num <= len(self.tarefas):
                self.tarefas[num-1]["pronta"] = True
                self.salvar()
                print("✅ Marcada como pronta!")
            else:
                print(f"❌ Digite entre 1 e {len(self.tarefas)}")
        except ValueError:
            print("❌ Precisa ser número!")

# USAR A CLASSE:
app = TodoList()  # Cria objeto
app.adicionar_tarefa()  # Sem passar tarefas!
app.listar_tarefas()
app.marcar_pronta()
```

---

### 6.4 - Menu Principal com Classe

```python
def main():
    """Loop principal"""
    app = TodoList()  # Cria uma vez
    
    while True:
        print("\n" + "="*40)
        print("📚 TO DO LIST")
        print("="*40)
        print("[1] Adicionar tarefa")
        print("[2] Ver tarefas")
        print("[3] Marcar como pronta")
        print("[4] Deletar tarefa")
        print("[5] Sair")
        print("="*40)
        
        escolha = input("Escolha: ").strip()
        
        if escolha == "1":
            app.adicionar_tarefa()
        elif escolha == "2":
            app.listar_tarefas()
        elif escolha == "3":
            app.marcar_pronta()
        elif escolha == "4":
            app.deletar_tarefa()  # Você vai criar isso
        elif escolha == "5":
            print("Até logo!")
            break
        else:
            print("❌ Inválida!")

# Rodar programa
if __name__ == "__main__":
    main()
```

**Novo conceito:**
- `if __name__ == "__main__":` = roda só quando executa diretamente (não quando importa)

---

### 6.5 - SEU EXERCÍCIO: Converta para Classe

📝 **Crie `aula_05.py`:**
1. Crie classe `TodoList` com:
   - `__init__()` - inicializa
   - `carregar()` - carrega JSON
   - `salvar()` - salva JSON
   - `adicionar_tarefa()` - adiciona
   - `listar_tarefas()` - lista
   - `marcar_pronta()` - marca pronta
   - `deletar_tarefa()` - deleta (você cria!)
2. Crie função `main()` com menu
3. Use `if __name__ == "__main__"`

**Dica para `deletar_tarefa()`:**
```python
def deletar_tarefa(self):
    """Deleta uma tarefa"""
    self.listar_tarefas()
    
    try:
        num = int(input("Qual deletar? "))
        if 1 <= num <= len(self.tarefas):
            nome = self.tarefas[num-1]["nome"]
            self.tarefas.pop(num-1)
            self.salvar()
            print(f"🗑️  '{nome}' deletada!")
        else:
            print(f"❌ Digite entre 1 e {len(self.tarefas)}")
    except ValueError:
        print("❌ Precisa ser número!")
```

---

## ✅ CHECKPOINT 6

Você consegue:
- [ ] Criar classe com `class`?
- [ ] Entender `__init__()` e `self`?
- [ ] Criar métodos dentro de classe?
- [ ] Usar `if __name__ == "__main__"`?

---

## FASE 7️⃣: PRIORIDADES E DATAS

### 7.1 - Adicionando Prioridades

```python
from datetime import datetime

class TodoList:
    def __init__(self):
        self.tarefas = []
        self.prioridades = ["Alta", "Média", "Baixa"]
    
    def adicionar_tarefa(self):
        """Adiciona tarefa com prioridade"""
        nome = input("Nome: ").strip()
        
        if not nome:
            print("❌ Vazio!")
            return
        
        # Escolher prioridade
        print("\nPrioridade:")
        for i, p in enumerate(self.prioridades, 1):
            print(f"  [{i}] {p}")
        
        try:
            escolha = int(input("Qual? ")) - 1
            
            if 0 <= escolha < len(self.prioridades):
                prioridade = self.prioridades[escolha]
            else:
                prioridade = "Média"  # Padrão
        except ValueError:
            prioridade = "Média"
        
        # Adicionar com data
        tarefa = {
            "nome": nome,
            "pronta": False,
            "prioridade": prioridade,
            "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
        
        self.tarefas.append(tarefa)
        self.salvar()
        print(f"✅ Adicionada com prioridade {prioridade}!")
    
    def listar_tarefas(self):
        """Lista com cor de prioridade"""
        if not self.tarefas:
            print("📭 Sem tarefas!")
            return
        
        # Separar por status
        pendentes = [t for t in self.tarefas if not t["pronta"]]
        concluidas = [t for t in self.tarefas if t["pronta"]]
        
        # Mostrar pendentes
        if pendentes:
            print("\n🔄 PENDENTES:")
            self._listar_grupo(pendentes)
        
        # Mostrar concluídas
        if concluidas:
            print("\n✅ CONCLUÍDAS:")
            self._listar_grupo(concluidas)
    
    def _listar_grupo(self, tarefas):
        """Helper para listar grupo de tarefas"""
        for i, t in enumerate(tarefas, 1):
            emoji_prioridade = {
                "Alta": "🔴",
                "Média": "🟡",
                "Baixa": "🟢"
            }
            
            emoji = emoji_prioridade[t["prioridade"]]
            status = "✓" if t["pronta"] else " "
            
            print(f"  [{status}] {emoji} {t['nome']}")
            print(f"       Criada: {t['data_criacao']}")
```

**Novos conceitos:**
- `from datetime import datetime` = importa datetime
- `datetime.now()` = pega hora atual
- `.strftime()` = formata data (veja [formatos aqui](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes))
- List comprehension: `[t for t in tarefas if not t["pronta"]]` = filtra lista

---

### 7.2 - Relatórios de Produtividade

```python
def mostrar_relatorio(self):
    """Mostra estatísticas"""
    total = len(self.tarefas)
    concluidas = sum(1 for t in self.tarefas if t["pronta"])
    pendentes = total - concluidas
    
    print("\n📊 RELATÓRIO:")
    print("="*40)
    print(f"Total de tarefas: {total}")
    print(f"Concluídas: {concluidas}")
    print(f"Pendentes: {pendentes}")
    
    if total > 0:
        percentual = (concluidas / total) * 100
        print(f"Progresso: {percentual:.1f}%")
        
        # Barra visual
        barra = "█" * int(percentual // 10) + "░" * (10 - int(percentual // 10))
        print(f"[{barra}]")
    
    # Por prioridade
    print("\nPor prioridade:")
    for prioridade in self.prioridades:
        count = sum(1 for t in self.tarefas 
                   if t["prioridade"] == prioridade and not t["pronta"])
        emoji = {"Alta": "🔴", "Média": "🟡", "Baixa": "🟢"}[prioridade]
        print(f"  {emoji} {prioridade}: {count}")
```

---

### 7.3 - SEU EXERCÍCIO: Integre Prioridades

📝 **Atualize `aula_05.py`:**
1. Adicione `prioridades` ao `__init__()`
2. Atualize `adicionar_tarefa()` para pedir prioridade
3. Atualize `listar_tarefas()` para mostrar emoji
4. Crie método `mostrar_relatorio()`
5. Adicione opção ao menu para relatório

---

## ✅ CHECKPOINT 7

Você consegue:
- [ ] Usar `datetime.now()` e `.strftime()`?
- [ ] Usar list comprehension para filtrar?
- [ ] Usar `sum()` com condição?
- [ ] Criar barra visual com caracteres?

---

## 🎉 VOCÊ AGORA É PRO!

Seu programa agora:
✅ Salva e carrega dados
✅ Usa Classes (POO)
✅ Tem prioridades
✅ Rastreia datas
✅ Mostra relatórios

---

## 🚀 PRÓXIMOS PASSOS

### Você quer aprender JavaScript?
Vá para: `03_APRENDIZADO_JAVASCRIPT.md`

### Quer adicionar mais funcionalidades?
- [ ] Exportar para Excel
- [ ] Enviar email com lembretes
- [ ] Integrar com Google Calendar
- [ ] Criar web app (Django/Flask)

---

## 📚 REFERÊNCIA AVANÇADA

```python
# JSON
import json
json.dump(dados, arquivo)      # Escrever
dados = json.load(arquivo)     # Ler

# Classes
class Nome:
    def __init__(self, param):
        self.atributo = param
    
    def metodo(self):
        return self.atributo

# DateTime
from datetime import datetime, timedelta
agora = datetime.now()
agora.strftime("%d/%m/%Y")
amanha = agora + timedelta(days=1)

# List Comprehension
nova_lista = [x for x in lista if condicao]
nova_lista = [x*2 for x in lista]

# Filtros
filtrados = filter(lambda x: x > 5, lista)
mapeados = map(lambda x: x*2, lista)

# Sum com condição
total = sum(1 for x in lista if x > 5)
```

---

**Parabéns por chegar até aqui! 🎓**

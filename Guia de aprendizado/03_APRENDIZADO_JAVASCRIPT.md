# 🌐 APRENDENDO JAVASCRIPT DESDE ZERO
## Construindo um To Do List Web Interativo

---

## 🎯 OBJETIVO

Você vai construir uma **aplicação web** que:
- ✅ Adiciona tarefas dinamicamente
- ✅ Lista tarefas na tela
- ✅ Marca como pronta (visual!)
- ✅ Deleta tarefas
- ✅ Salva dados permanentemente

**Sem usar bibliotecas - apenas HTML, CSS e JavaScript puro!**

---

## 📋 PRÉ-REQUISITOS

Você precisa de:
- Um editor de texto (VS Code, Sublime, etc)
- Um navegador moderno (Chrome, Firefox, Edge)
- Conhecimento básico de HTML e CSS

---

## 🏗️ ESTRUTURA DO PROJETO

```
projeto/
├─ index.html          # Página (HTML)
├─ style.css           # Estilos (CSS)
└─ app.js              # Lógica (JavaScript)
```

---

## FASE 1️⃣: HTML BÁSICO

### 1.1 - Criar Arquivo HTML

📝 **Crie `index.html`:**

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To Do List</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>📚 Minha To Do List</h1>
        
        <!-- Formulário -->
        <div class="formulario">
            <input 
                type="text" 
                id="inputTarefa" 
                placeholder="Digite uma tarefa..."
            >
            <button id="btnAdicionar">Adicionar</button>
        </div>
        
        <!-- Lista de tarefas -->
        <ul id="listaTarefas" class="lista">
            <!-- Tarefas vão aparecer aqui -->
        </ul>
    </div>
    
    <!-- Importar JavaScript -->
    <script src="app.js"></script>
</body>
</html>
```

**Entendendo o HTML:**
- `id="inputTarefa"` = identificador único para acessar do JS
- `id="btnAdicionar"` = botão que vai disparar ação
- `id="listaTarefas"` = container onde mostrar tarefas
- `<script src="app.js">` = importa arquivo JavaScript

---

### 1.2 - Criar CSS Básico

📝 **Crie `style.css`:**

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.container {
    background: white;
    border-radius: 10px;
    padding: 30px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    width: 100%;
    max-width: 500px;
}

h1 {
    color: #667eea;
    margin-bottom: 20px;
    text-align: center;
}

.formulario {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
}

#inputTarefa {
    flex: 1;
    padding: 12px;
    border: 2px solid #e0e0e0;
    border-radius: 5px;
    font-size: 16px;
}

#inputTarefa:focus {
    outline: none;
    border-color: #667eea;
}

#btnAdicionar {
    padding: 12px 25px;
    background: #667eea;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    transition: background 0.3s;
}

#btnAdicionar:hover {
    background: #764ba2;
}

.lista {
    list-style: none;
}

.item-tarefa {
    background: #f8f9fa;
    padding: 15px;
    margin-bottom: 10px;
    border-radius: 5px;
    display: flex;
    align-items: center;
    gap: 10px;
    border-left: 4px solid #667eea;
}

.item-tarefa.pronta {
    opacity: 0.6;
    border-left-color: #27ae60;
}

.item-tarefa.pronta .nome {
    text-decoration: line-through;
    color: #999;
}

.checkbox {
    width: 20px;
    height: 20px;
    cursor: pointer;
}

.nome {
    flex: 1;
    font-weight: 500;
}

.btnDeletar {
    background: #e74c3c;
    color: white;
    border: none;
    padding: 8px 12px;
    border-radius: 3px;
    cursor: pointer;
    transition: background 0.3s;
}

.btnDeletar:hover {
    background: #c0392b;
}
```

---

## FASE 2️⃣: JAVASCRIPT - O BÁSICO

### 2.1 - Primeiros Passos

📝 **Crie `app.js`:**

```javascript
// Dados (como em Python)
const tarefas = [];

// Elementos do HTML (como em Python, "pegando" do DOM)
const inputTarefa = document.getElementById("inputTarefa");
const btnAdicionar = document.getElementById("btnAdicionar");
const listaTarefas = document.getElementById("listaTarefas");

// Quando clica no botão, chama função
btnAdicionar.addEventListener("click", adicionarTarefa);

function adicionarTarefa() {
    console.log("Botão foi clicado!");
}
```

**Entendendo:**
- `document.getElementById()` = pega elemento do HTML pelo `id`
- `.addEventListener()` = escuta quando algo acontece
- `"click"` = tipo de evento (também tem `"change"`, `"keypress"`, etc)
- `console.log()` = mostra no console do navegador

**Teste:**
1. Abra `index.html` no navegador
2. Pressione F12 para abrir DevTools
3. Vá em "Console"
4. Clique no botão
5. Veja a mensagem!

---

### 2.2 - Adicionar Tarefa

```javascript
function adicionarTarefa() {
    // 1. Pegar valor do input
    const nome = inputTarefa.value.trim();
    
    // 2. Validar se está vazio
    if (!nome) {
        alert("❌ Digite algo!");
        return;  // Sai da função
    }
    
    // 3. Criar objeto tarefa (como em Python)
    const tarefa = {
        id: Date.now(),        // ID único baseado na data
        nome: nome,
        pronta: false
    };
    
    // 4. Adicionar à lista
    tarefas.push(tarefa);
    
    // 5. Limpar input
    inputTarefa.value = "";
    
    // 6. Atualizar visual
    atualizarLista();
    
    console.log("Tarefa adicionada:", tarefa);
}
```

**Novos conceitos:**
- `.value` = pega o valor de um input
- `.trim()` = remove espaços
- `Date.now()` = timestamp único (tipo em Python)
- `.push()` = adiciona à lista (como em Python)

---

### 2.3 - Mostrar Tarefas na Tela

```javascript
function atualizarLista() {
    // Limpar lista antiga
    listaTarefas.innerHTML = "";
    
    // Se não há tarefas
    if (tarefas.length === 0) {
        listaTarefas.innerHTML = "<p>📭 Nenhuma tarefa ainda</p>";
        return;
    }
    
    // Para cada tarefa, criar um elemento
    tarefas.forEach(function(tarefa) {
        // Criar elemento <li>
        const li = document.createElement("li");
        li.className = "item-tarefa";
        
        // Se está pronta, adicionar classe
        if (tarefa.pronta) {
            li.classList.add("pronta");
        }
        
        // Criar HTML da tarefa
        li.innerHTML = `
            <input 
                type="checkbox" 
                class="checkbox"
                ${tarefa.pronta ? "checked" : ""}
                onchange="marcarPronta(${tarefa.id})"
            >
            <span class="nome">${tarefa.nome}</span>
            <button class="btnDeletar" onclick="deletarTarefa(${tarefa.id})">
                🗑️ Deletar
            </button>
        `;
        
        // Adicionar à lista
        listaTarefas.appendChild(li);
    });
}
```

**Entendendo:**
- `innerHTML = ""` = limpa o conteúdo
- `createElement()` = cria elemento HTML
- `innerHTML = "..."` = adiciona HTML
- `forEach()` = loop em cada item (como `for ... in` Python)
- `${variavel}` = template string (como f-string Python)
- `appendChild()` = adiciona elemento ao DOM

---

### 2.4 - Marcar como Pronta

```javascript
function marcarPronta(id) {
    // Encontrar tarefa com esse ID
    const tarefa = tarefas.find(t => t.id === id);
    
    if (tarefa) {
        // Inverter status
        tarefa.pronta = !tarefa.pronta;
        
        // Atualizar visual
        atualizarLista();
    }
}

function deletarTarefa(id) {
    // Filtrar (remover) tarefa com esse ID
    tarefas.filter(t => t.id !== id);
    
    // Atualizar visual
    atualizarLista();
}
```

**Novos conceitos:**
- `.find()` = encontra primeiro item que atende condição
- `.filter()` = cria nova lista sem item (não modifica original)
- `!variavel` = inverte boolean (True vira False)

**PROBLEMA**: `filter()` não modifica a lista! Solução:

```javascript
function deletarTarefa(id) {
    // Encontrar índice
    const indice = tarefas.findIndex(t => t.id === id);
    
    // Se encontrou
    if (indice !== -1) {
        tarefas.splice(indice, 1);  // Remove 1 item na posição
    }
    
    atualizarLista();
}
```

---

### 2.5 - SEU PRIMEIRO EXERCÍCIO

📝 **Complete `app.js` com:**
1. Função `adicionarTarefa()` ✅
2. Função `atualizarLista()` ✅
3. Função `marcarPronta(id)` ✅
4. Função `deletarTarefa(id)` ✅

**Teste no navegador:**
- Abra `index.html`
- Adicione uma tarefa
- Marque como pronta (checkbox)
- Delete uma tarefa

---

## ✅ CHECKPOINT 1

Você consegue:
- [ ] Usar `getElementById()` e `addEventListener()`?
- [ ] Manipular `.value` e `.innerHTML`?
- [ ] Usar `forEach()` e `find()`?
- [ ] Criar e adicionar elementos com `.createElement()`?
- [ ] Usar template strings com `${}`?

---

## FASE 3️⃣: SALVANDO DADOS

### 3.1 - localStorage em JavaScript

JavaScript tem um "disco rígido" local chamado **localStorage**:

```javascript
// SALVAR dados
const dados = { nome: "João", idade: 25 };
localStorage.setItem("usuario", JSON.stringify(dados));

// LER dados
const dados_lidos = JSON.parse(localStorage.getItem("usuario"));
console.log(dados_lidos);  // { nome: "João", idade: 25 }

// DELETAR dados
localStorage.removeItem("usuario");

// LIMPAR TUDO
localStorage.clear();
```

**Entendendo:**
- `JSON.stringify()` = converte objeto em texto (como `json.dump()` Python)
- `JSON.parse()` = converte texto em objeto (como `json.load()` Python)
- `localStorage.setItem()` = salva
- `localStorage.getItem()` = carrega

---

### 3.2 - Integrando localStorage

```javascript
// Carregar tarefas ao iniciar
function carregarTarefas() {
    const dados = localStorage.getItem("tarefas");
    
    if (dados) {
        // Se tem dados salvos, carrega
        const tarefasCarregadas = JSON.parse(dados);
        tarefas.push(...tarefasCarregadas);  // ... = "spread operator"
        atualizarLista();
    }
}

// Salvar tarefas
function salvarTarefas() {
    localStorage.setItem("tarefas", JSON.stringify(tarefas));
}

// Chamadas
carregarTarefas();  // No início

// E depois de CADA mudança:
function adicionarTarefa() {
    // ... código ...
    tarefas.push(tarefa);
    salvarTarefas();  // 👈
    atualizarLista();
}

function marcarPronta(id) {
    // ... código ...
    tarefa.pronta = !tarefa.pronta;
    salvarTarefas();  // 👈
    atualizarLista();
}

function deletarTarefa(id) {
    // ... código ...
    tarefas.splice(indice, 1);
    salvarTarefas();  // 👈
    atualizarLista();
}
```

---

### 3.3 - SEU EXERCÍCIO: Integre localStorage

📝 **Atualize `app.js`:**
1. Adicione `carregarTarefas()`
2. Adicione `salvarTarefas()`
3. Chame `carregarTarefas()` no início
4. Chame `salvarTarefas()` em cada mudança

**Teste:**
- Abra página
- Adicione tarefas
- Feche navegador
- Abra novamente
- Tarefas ainda estão lá? ✅

---

## ✅ CHECKPOINT 2

Você consegue:
- [ ] Usar `JSON.stringify()` e `JSON.parse()`?
- [ ] Usar `localStorage.setItem()` e `.getItem()`?
- [ ] Entender spread operator `...`?

---

## FASE 4️⃣: MELHORANDO A INTERFACE

### 4.1 - Adicionar Prioridades

**Atualize HTML:**
```html
<div class="formulario">
    <input 
        type="text" 
        id="inputTarefa" 
        placeholder="Digite uma tarefa..."
    >
    <select id="prioridade">
        <option value="Baixa">🟢 Baixa</option>
        <option value="Média" selected>🟡 Média</option>
        <option value="Alta">🔴 Alta</option>
    </select>
    <button id="btnAdicionar">Adicionar</button>
</div>
```

**Atualize JavaScript:**
```javascript
const prioridade = document.getElementById("prioridade");

function adicionarTarefa() {
    const nome = inputTarefa.value.trim();
    
    if (!nome) {
        alert("❌ Digite algo!");
        return;
    }
    
    const tarefa = {
        id: Date.now(),
        nome: nome,
        prioridade: prioridade.value,  // 👈 NOVO
        pronta: false,
        dataCriacao: new Date().toLocaleString("pt-BR")  // 👈 NOVO
    };
    
    tarefas.push(tarefa);
    inputTarefa.value = "";
    
    salvarTarefas();
    atualizarLista();
}

function atualizarLista() {
    listaTarefas.innerHTML = "";
    
    if (tarefas.length === 0) {
        listaTarefas.innerHTML = "<p>📭 Nenhuma tarefa</p>";
        return;
    }
    
    tarefas.forEach(tarefa => {
        const emoji = {
            "Alta": "🔴",
            "Média": "🟡",
            "Baixa": "🟢"
        }[tarefa.prioridade];
        
        const li = document.createElement("li");
        li.className = "item-tarefa";
        
        if (tarefa.pronta) {
            li.classList.add("pronta");
        }
        
        li.innerHTML = `
            <input 
                type="checkbox" 
                class="checkbox"
                ${tarefa.pronta ? "checked" : ""}
                onchange="marcarPronta(${tarefa.id})"
            >
            <span class="emoji">${emoji}</span>
            <span class="nome">${tarefa.nome}</span>
            <span class="data">${tarefa.dataCriacao}</span>
            <button class="btnDeletar" onclick="deletarTarefa(${tarefa.id})">
                🗑️
            </button>
        `;
        
        listaTarefas.appendChild(li);
    });
}
```

---

### 4.2 - Adicionar Filtros

```javascript
// Novo elemento no HTML
const filtroSelect = document.getElementById("filtro");

function filtrarTarefas(status) {
    let filtradas;
    
    if (status === "todas") {
        filtradas = tarefas;
    } else if (status === "pendentes") {
        filtradas = tarefas.filter(t => !t.pronta);
    } else if (status === "concluidas") {
        filtradas = tarefas.filter(t => t.pronta);
    }
    
    atualizarListaFiltrada(filtradas);
}

function atualizarListaFiltrada(tarefasFiltradas) {
    // ... mesmo código de atualizarLista mas com tarefasFiltradas
}
```

---

### 4.3 - SEU EXERCÍCIO: Melhore a Interface

📝 **Atualize seu projeto:**
1. Adicione `<select>` de prioridade
2. Atualize `adicionarTarefa()` para coletar prioridade
3. Atualize `atualizarLista()` para mostrar emoji
4. Adicione data de criação com `new Date().toLocaleString()`

---

## ✅ CHECKPOINT 3

Você consegue:
- [ ] Usar `<select>` e pegar o valor?
- [ ] Usar template strings com emojis?
- [ ] Usar `.toLocaleString()` para datas?
- [ ] Usar `.filter()` para filtros?

---

## 🎉 PARABÉNS!

Você construiu uma **aplicação web profissional** que:
✅ Adiciona tarefas dinamicamente
✅ Marca como pronta com visual
✅ Deleta tarefas
✅ Salva dados permanentemente
✅ Mostra prioridades
✅ Tem data de criação

---

## 🚀 PRÓXIMOS PASSOS

### Ainda quer aprender mais JavaScript?
- [ ] Usar classes (muito parecido com Python!)
- [ ] Fazer requisições HTTP (fetch)
- [ ] Integrar com API
- [ ] Usar bibliotecas (React, Vue)

### Quer comparar com Python?
Veja como seria em Python em `02_APRENDIZADO_PYTHON_AVANCADO.md`

---

## 📚 REFERÊNCIA RÁPIDA

```javascript
// DOM
document.getElementById("id")
document.querySelector(".class")
.addEventListener("click", funcao)
.innerHTML = "..."
.value = "..."

// Arrays
array.push(item)
array.splice(indice, 1)  // Remove
array.find(item => item.id === 5)
array.filter(item => item.pronta)
array.forEach(item => {...})

// Objetos
objeto = { chave: valor }
objeto.chave
objeto["chave"]

// localStorage
localStorage.setItem("chave", JSON.stringify(dados))
JSON.parse(localStorage.getItem("chave"))

// Datas
new Date()
.toLocaleString("pt-BR")
Date.now()

// Template strings
`Texto ${variavel} mais texto`

// Operadores
!condicao      // NOT
condicao1 && condicao2  // AND
condicao1 || condicao2  // OR
```

---

**Bom desenvolvimento! 🚀**

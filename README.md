# 🌐 Minirrede Social — Teoria dos Grafos na Prática

Projeto desenvolvido como atividade prática da disciplina de Estruturas de Dados Não Lineares, aplicando a teoria dos grafos para modelar uma rede social simples com recomendação de conexões.

---

## 📌 Definição do Problema

O objetivo é mapear relações de amizade entre usuários e oferecer três funcionalidades principais:

- Listar os amigos diretos de um usuário
- Calcular o grau de separação entre dois usuários
- Recomendar "amigos de amigos"

---

## 🧮 Modelagem Matemática

O problema foi abstraído como um **Grafo Não-Direcionado sem peso**, utilizando a biblioteca **NetworkX**.

| Elemento | Representa |
|---|---|
| Vértice (nó) | Usuário da rede social |
| Aresta | Amizade entre dois usuários |
| Direção | Não-direcionado (amizade é mútua) |
| Peso | Sem peso (cada aresta = 1 grau de separação) |

**Estrutura da rede utilizada nos testes:**

```
Ana — Bia
Ana — Carlos
Bia — Daniel
Bia — Antonio
Carlos — Gabriel
Daniel — Gabriel
```

---

## ⚙️ Algoritmos Aplicados

### Listar Amigos
Utiliza `G.neighbors()` do NetworkX para retornar os vizinhos diretos de um nó.

### Grau de Separação (BFS)
Utiliza `nx.shortest_path()` e `nx.shortest_path_length()`, que internamente aplicam **Busca em Largura (BFS)**. Como o grafo não tem pesos, cada aresta vale 1 grau — a BFS garante o menor número de arestas entre dois nós.

### Recomendação de Amigos de Amigos
Percorre os amigos dos amigos do usuário com um loop duplo, filtrando:
- A própria pessoa
- Quem já é amigo direto
- Duplicatas (usando `set`)

---

## 🖥️ Como Executar

### Pré-requisitos
- Python 3.x instalado
- Biblioteca NetworkX

### Instalação
```bash
pip install networkx
```

### Execução
```bash
python index.py
```

### Menu da Aplicação
```
=== Minirrede Social ===
1. Listar amigos
2. Grau de separação
3. Recomendar amigos
4. Sair
```

---

## 🗂️ Estrutura do Projeto

```
mini-rede-social/
│
└── index.py        # Código principal
└── README.md       # Documentação
```

---

## 🧪 Exemplos de Uso

**Listar amigos da Ana:**
```
Amigos de Ana: ['Bia', 'Carlos']
```

**Grau de separação entre Ana e Gabriel:**
```
Caminho: ['Ana', 'Carlos', 'Gabriel']
Grau de separação: 2
```

**Recomendações para Daniel:**
```
Recomendações para Daniel: ['Antonio', 'Carlos']
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **NetworkX** — instanciação do grafo e algoritmos de travessia

---

## 👤 Antônio Ribeiro Santiago Bisneto

Desenvolvido como trabalho prático da disciplina de Estruturas de Dados.

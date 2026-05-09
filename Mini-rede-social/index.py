import networkx as nx

G = nx.Graph()

G.add_node("Ana")
G.add_node("Bia")
G.add_node("Carlos")
G.add_node("Daniel")
G.add_node("Gabriel")
G.add_node("Antonio")

G.add_edge("Ana", "Bia")
G.add_edge("Ana", "Carlos")
G.add_edge("Bia", "Daniel")
G.add_edge("Carlos", "Gabriel")
G.add_edge("Antonio", "Bia")
G.add_edge("Daniel", "Gabriel")

def recomendar_amigos(G, usuario):
    amigos = list(G.neighbors(usuario))
    recomendacoes = set()
    for amigo in amigos:
        amigos_do_amigo = list(G.neighbors(amigo))
        for amigo_do_amigo in amigos_do_amigo:
            if amigo_do_amigo not in amigos and amigo_do_amigo != usuario:
                recomendacoes.add(amigo_do_amigo)
    print(f"Recomendações para {usuario}: {list(recomendacoes)}")

def listar_amigos(G, usuario):
    amigos = list(G.neighbors(usuario))
    print(f"Amigos de {usuario}: {amigos}")

def grau_de_separacao(G, usuario1, usuario2):
    caminho = nx.shortest_path(G, usuario1, usuario2)
    print(f"Caminho: {caminho}")
    grau = nx.shortest_path_length(G, usuario1, usuario2)
    print(f"Grau de separação: {grau}")
   
while True:
    print("=== Minirrede Social ===")
    print("1. Listar amigos")
    print("2. Grau de separação")
    print("3. Recomendar amigos")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        print("Você escolheu Listar Amigos")
        usuario = input("Digite o nome do usuário: ")
        listar_amigos(G, usuario)  
    elif opcao == "2":
        print("Você escolheu grau de separação")
        usuario1 = input("Digite o nome do primeiro usuário: ")
        usuario2 = input("Digite o nome do segundo usuário: ")
        grau_de_separacao(G, usuario1, usuario2)
    elif opcao == "3":
        print("Você escolheu recomendar amigos")
        usuario = input("Digite o nome do usuário: ")
        recomendar_amigos(G, usuario)
    elif opcao == "4":
        break
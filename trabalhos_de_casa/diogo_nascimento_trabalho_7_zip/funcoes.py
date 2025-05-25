from globais import produtos, vendas

def cadastrar_produto(nome, preco, quantidade):
    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": quantidade
    }
    produtos.append(produto)
    print(f"--- SUCESSO! Produto '{nome}' cadastrado! ---")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    
    print("\n--- LISTA DE PRODUTOS ---")
    for i, produto in enumerate(produtos):
        print(f"{i+1}. {produto['nome']} - €{produto['preco']:.2f} ({produto['estoque']} unidades)")

def editar_produto():
    if not produtos:
        print("Nenhum produto cadastrado para editar.")
        return
    
    listar_produtos()
    try:
        indice = int(input("\nNúmero do produto a editar: ")) - 1
        if indice < 0 or indice >= len(produtos):
            print("Produto inválido.")
            return
        
        produto = produtos[indice]
        print(f"\nEditando produto: {produto['nome']}")
        
        novo_nome = input(f"Novo nome (atual: {produto['nome']}): ").strip()
        if novo_nome:
            produto['nome'] = novo_nome
        
        novo_preco = input(f"Novo preço (atual: €{produto['preco']:.2f}): ").strip()
        if novo_preco:
            produto['preco'] = float(novo_preco)
        
        nova_quantidade = input(f"Nova quantidade (atual: {produto['estoque']}): ").strip()
        if nova_quantidade:
            produto['estoque'] = int(nova_quantidade)
        
        print("--- PRODUTO EDITADO COM SUCESSO! ---")
    
    except (ValueError, IndexError):
        print("Entrada inválida.")

def apagar_produto():
    if not produtos:
        print("Nenhum produto cadastrado para apagar.")
        return
    
    listar_produtos()
    try:
        indice = int(input("\nNúmero do produto a apagar: ")) - 1
        if indice < 0 or indice >= len(produtos):
            print("Produto inválido.")
            return
        
        produto_removido = produtos.pop(indice)
        print(f"--- PRODUTO '{produto_removido['nome']}' REMOVIDO COM SUCESSO! ---")
    
    except (ValueError, IndexError):
        print("Entrada inválida.")

def vender_produto(indice, quantidade):
    if indice < 0 or indice >= len(produtos):
        print("Produto inválido.")
        return
    
    produto = produtos[indice]
    if produto["estoque"] < quantidade:
        print(f"Estoque insuficiente. Disponível: {produto['estoque']} unidades")
        return
    
    produto["estoque"] -= quantidade
    total = produto["preco"] * quantidade
    
    venda = {
        "produto": produto["nome"], 
        "quantidade": quantidade, 
        "total": total,
        "preco_unitario": produto["preco"]
    }
    vendas.append(venda)
    
    print(f"--- VENDA REALIZADA! ---")
    print(f"{quantidade}x {produto['nome']} - Total: €{total:.2f}")

def realizar_venda():
    if not produtos:
        print("Nenhum produto cadastrado para vender.")
        return
    
    listar_produtos()
    try:
        indice = int(input("\nNúmero do produto a vender: ")) - 1
        quantidade = int(input("Quantidade: "))
        
        if quantidade <= 0:
            print("Quantidade deve ser maior que zero.")
            return
        
        vender_produto(indice, quantidade)
    
    except (ValueError, IndexError):
        print("Entrada inválida.")

def listar_vendas():
    if not vendas:
        print("Nenhuma venda registrada.")
        return
    
    print("\n--- HISTÓRICO DE VENDAS ---")
    total_geral = 0
    for i, venda in enumerate(vendas, 1):
        print(f"{i}. {venda['quantidade']}x {venda['produto']} "
              f"(€{venda['preco_unitario']:.2f} cada) - Total: €{venda['total']:.2f}")
        total_geral += venda['total']
    
    print(f"\nTOTAL GERAL DE VENDAS: €{total_geral:.2f}")


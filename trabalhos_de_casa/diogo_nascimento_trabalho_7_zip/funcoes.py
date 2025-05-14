from globais import produtos, vendas

def cadastrar_produto(nome, preco, estoque):
    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }
    produtos.append(produto)
    print(f"Produto '{nome}' cadastrado com sucesso!")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    for i, produto in enumerate(produtos):
        print(f"{i+1}. {produto['nome']} - R$ {produto['preco']} ({produto['estoque']} unidades)")

def vender_produto(indice, quantidade):
    if indice < 0 or indice >= len(produtos):
        print("Produto inválido.")
        return
    produto = produtos[indice]
    if produto["estoque"] < quantidade:
        print("Estoque insuficiente.")
        return
    produto["estoque"] -= quantidade
    total = produto["preco"] * quantidade
    vendas.append({"produto": produto["nome"], "quantidade": quantidade, "total": total})
    print(f"Venda realizada: {quantidade}x {produto['nome']} - Total: R$ {total:.2f}")

def listar_vendas():
    if not vendas:
        print("Nenhuma venda registrada.")
    for venda in vendas:
        print(f"{venda['quantidade']}x {venda['produto']} - Total: R$ {venda['total']:.2f}")

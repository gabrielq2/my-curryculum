def ticket():
    # Solicitar a quantidade de clientes
    clientes = int(input('Insira a quantidade de clientes: '))

    # Inicializar variáveis
    compras_por_pessoa = {}
    pess = []
    qnt_vends = 0

    # Coletar informações de compras
    for i in range(clientes):
        compras = int(input(f'Insira a quantidade de compras do {i + 1}° cliente: '))
        compras_ = []

        for j in range(compras):
            preco = float(input(f'Insira o valor da {j + 1}ª compra: '))
            compras_.append(preco)
            pess.append(i + 1)  # Adiciona o cliente à lista de pessoas

        # Armazena as compras do cliente
        compras_por_pessoa[f"pessoa{i + 1}"] = compras_

    # Calcula o total de vendas
    vendas_ = [sum(compras[:4]) for compras in compras_por_pessoa.values()]  # Considera apenas as 4 primeiras compras
    total_vendas = sum(vendas_)

    # Calcula o ticket médio
    if len(pess) > 0:
        ticket_medio = total_vendas / len(pess)
    else:
        ticket_medio = 0

    # Verifica as vendas abaixo de 30% do ticket médio nas 4 primeiras compras
    vends_inf = 0
    for pessoa, compras in compras_por_pessoa.items():
        for compra in compras[:4]:  # Considera apenas as 4 primeiras compras
            if compra < 0.30 * ticket_medio:
                vends_inf += 1

    # Exibir os resultados
    print("\n--- Resultados ---")
    print(f"Total de vendas (considerando as 4 primeiras compras por pessoa): R$ {total_vendas:.2f}")
    print(f"Ticket médio: R$ {ticket_medio:.2f}")
    print(f"Quantidade de vendas abaixo de 30% do ticket médio (nas 4 primeiras compras): {vends_inf}")
    print(f"Detalhamento das compras por pessoa: {compras_por_pessoa}")

# Chamar a função
ticket()
def ticket():
   clientes=int(input('insira a quantidade de clientes:'))
   compras_por_pessoa={}
   pess=[]
   for i in range(clientes):
       compras=int(input(f'insira a quantidade de compras do {i+1}° cliente:'))
       compras_=[]
   
       for j in range(compras):
         preço=float(input(f'insira o preço da {j+1}° compra:'))
         compras_.append(preço)
         pess.append(i+1)
        
         compras_por_pessoa[f"pessoa{i+1}"]=compras_
   
   
   vendas_=[sum(compras[:4]) for compras in compras_por_pessoa.values()]
   
   total_vendas=sum(vendas_)
   
   ticket_medio=total_vendas/len(pess)

   vends_inf=0
   for pessoa, compras in compras_por_pessoa.items():
      for compra in compras[:4]:
         if compra < 0.30*ticket_medio:
            vends_inf+=1
    

   print("\n--- Resultados ---")
   print(f"Ticket médio: R$ {ticket_medio:.2f}")
   print(f"Quantidade de vendas abaixo de 30% do ticket médio (nas 4 primeiras compras): {vends_inf}")
   print(f"Detalhamento das compras por pessoa: {compras_por_pessoa}")

ticket()
def inss(idade,contribuição,sexo):
   if sexo == 'm' or sexo == 'M' :
     if idade >= 65 and contribuição >=10 or idade >= 63 and contribuição >=15:
         return 'você possui aposentadoria'
     else:
        return 'você não possui aposentadoria'
   elif sexo == 'f' or sexo == 'F' :
     if idade >= 63 and contribuição >=10 or idade >= 61 and contribuição >=15:
         return 'você possui aposentadoria'
     else:
        return 'você não possui aposentadoria'
while True:
 sexo=input('insira seu sexo M ou F:')
 
 if sexo != 'm' and sexo != 'M' and sexo != 'f' and sexo != 'F':
    while  sexo != 'm' and sexo != 'M' and sexo != 'f' and sexo != 'F':
       print('resposta errada necessita ser M ou F')
       sexo=input('insira seu sexo M ou F:')
 
 idade=int(input('insira sua idade:'))  
 contribuição=int(input('insira o tempo de contribuiçã0:'))
 print(inss(idade,contribuição,sexo))
 pergunta=input('gostaria de refazer (s/n):')
 
 if pergunta == 'n':
    break
 
 elif pergunta != 'n' and pergunta != 's':
   while  pergunta != 'n' and pergunta != 's':
    print('resposta errada necessita ser s ou n')
    pergunta=input('gostaria de refazer (s/n):')
import math
a=int(input('insira o valor de a:'))
if a<=0:
    while a<=0:
        print('a não pode ser negtivo e nem 0')
        a=int(input('insira o valor de a:'))
b=int(input('insira o valor de b:'))
c=int(input('insira o valor de c:'))
delta=b**2-4*a*b
if delta<0:
    print('delta não pode ser menor de 0')
elif delta>=0:
    x1=(-b+math.sqrt(delta))/2*a
    x2=(-b-math.sqrt(delta))/2*a
    print(f'o x1 é {x1} e o x2 {x2}')
n=int(input('insira a quantidade de números na lista:'))
lista=[]
for i in range(n):
    lista.append(int(input(f'insira o {i+1}° número:')))
menor=int(input('insira o limite mínimo:'))
maior=int(input('insira o limite máximo:'))

for numeros in lista:
    if numeros >= menor and numeros <= maior:
        print(numeros)
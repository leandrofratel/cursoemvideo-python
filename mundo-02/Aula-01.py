# Contagem regressiva para os fogos.
'''
from time import sleep
for c in range(10, -1, -1):
    sleep(1)
    print(c)
sleep(1)
print('\033[1;31mBOOOOMMMMM!!!\033[m')
'''
# Imprima os numeros pares de 1 a 50.
'''
for c in range(2, 51, 2):
    print('.', end='')
    print(c, end=' ')
'''
# Soma dos numeros impares multiplos de 3 no intervalo de 1 a 500.
'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # OU soma += c
        soma = soma + c # Ou soma += soma
print(f'A soma de todos os {cont} valores solicitados é {soma}.')
'''
# Faça uma tabuada igual ao exercio 009 utilizando laço.
'''
t = int(input('Digite um valor para ver sua tabuada: '))
for c in range(0, 11):
    print(f'{t} X {c:2} = {t*c}')
'''
# Faça um programa que leia e some 6 numeros pares, se for impar desconsiderar.
'''
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} pares e a soma deu {soma}.')
'''
# Progressão aritmetica?
'''
'''
# Um programa que leia um número inteiro e diga se é ou não um primo.
'''
primo = []
num = int(input('Digite um número inteiro: '))
for c in range(1, num):
    primo.append(c)
    print(primo)
    if num % 1 == 0 and num % num == 0 and num in primo:
        print(f'O número {num} é primo.')
    else:
        print(f'O número {num} não é um número primo.') 
'''
# Faça um progrma que leia uma frase e diga se ela é um palindromoo.
'''
'''
# Um programa que leia o ano de nascimento e diga quantos são maoir de idade e quantos não (21 anos).
'''
'''
# Um programa que leia o peso de 5 pessoas e diga qual é o maior e qual é o menor.
'''
'''
# Um programa que leia o Nome, Idade e o Sexo de 4 pessoas e diga:
# A média de idade do grupo;
# Qual o nome do homem mais velho;
# Quantas mulheres tem menos de 20 anos.
'''
'''
# Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo; qual é o nome do homem mais velho; quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome:')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4

print(f'A média de idade do grupo é de {mediaidade}.')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'No total são {totmulher20} mulher(es) com menos de 20 anos')
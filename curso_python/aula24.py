# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5 
# n a n d a a
# -6-5-4-3-2-1
#nome = 'Nandaa'
#print(nome[2])
#print(nome[-4])
#print('daa'in nome)
#print('zero' in nome)
#print(10 * '-')
#print('daa' not in nome)
#print('zero'not in nome)

nome = input('digite seu nome:')
encontrar = input('digite o que deseja encontrar:')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
"""
Exercício
peça ao usuário para digitar seu nome
peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
       exiba:
       Seu nome é {nome}
       Seu nome invertido é {nome invertido}
       Seu nome contém {ou não} espaços
       Seu nome tem {n} letras
       A primeira letra do seu nome é:
       A ultima letra do seu nome é:
Se nada for digitado em nome ou idade:
     exiba:"Desculpe, você deixou campos vazios."
"""
nome = input('Digite o seu nome:')
idade = input('Digite a sua idade:')

if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
else:
    print('desculpe voce deixou campos vazios.')
    
    if ' ' in nome:
       print('Seu nome contém espaços')
    else:
      print('Seu nome NÃO contem espaços')
 
print(f'Seu nome tem {len(nome)} letras')
print(f'A primeira letra do seu nome é {nome[0]}')
print(f'A ultima letra do seu nome é {nome[-1]}')



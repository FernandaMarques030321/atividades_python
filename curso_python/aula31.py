"""
Flag (Bandeira) - Marcar um local
Nome = Não valor 
Is e Is not = é ou não é (tipo, valor, identidade)
id = identidade

""" 
condicao = True
passou_no_if = None

if condicao: 
    passou_no_if = True
    print('Faça algo')
else:
   print('Não faça algo')
  
if passou_no_if is None:
    print('não passou no if')

else:
    print(' passou no if')
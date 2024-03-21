# and (e) or (ou) not (não)
# and - todas as condições precisam ser
# verdadeiras.
# se qualquer valor for considerado falso,
# a expressão inteira sera avaliada naquele valor.
# são considerados falsy (que você ja viu)
# 0 0.0 '' false
# também existe o tipo none que é 
#usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

#avaliação de curto circuito

senha = input('Senha:') or 'Sem senha'
print(senha)
from Fila import *

filaSPrdd = Fila()
filaPrdd = FilaPrdd()

# Abaixo a função responsavel por gerar as senhas com e sem prioridade
def gerarSenha(senha, prdd):
    if prdd == 1:
        filaPrdd.inserir(senha)
        print('Senha Gerada! Nº :',senha,'\n')
        print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨ PROXIMAS SENHAS ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
        filaPrdd.mostrarSenha()
        filaSPrdd.mostrarSenha()
        print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')

    elif prdd == 0:
        filaSPrdd.inserir(senha)
        print('Senha Gerada! Nº :',senha,'\n')
        print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨ PROXIMAS SENHAS ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
        filaPrdd.mostrarSenha()
        filaSPrdd.mostrarSenha()
        print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')


    else:
        print('Favor digitar a prioridade [0 ou 1]')

# abaixo segue a função responsavel por chamar a senha, mostrando com prioridade e sem!
def chamarSenha():
    if filaPrdd.vazia() and filaSPrdd.vazia():
        print('Não há senhas para chamar!')
    else:
        if not filaPrdd.vazia():
            print('Senha Nº : ', filaPrdd.excluir(), 'Comparecer ao caixa')
        else:
            print('Senha Nº : ', filaSPrdd.excluir(), 'Comparecer ao caixa')
        print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨ PROXIMAS SENHAS ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
        filaPrdd.mostrarSenha()
        filaSPrdd.mostrarSenha()
        print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')

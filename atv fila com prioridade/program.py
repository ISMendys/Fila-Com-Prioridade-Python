from FilaPrdd import *

# Abaixo segue todo codigo "front end" do cliente

menu = 1

while menu != 0:
    print('#' * 15, ' MENU ', '#' * 15)
    menu = int(input(
        'Para gerar uma senha Digite [1]\nPara chamar uma senha Digite [2]\nsair digite [0]\n'))
    if menu == 1:
        senha = int(input('Digite a senha'))
        prdd = int(input('Digite a prioridade - Sendo [1] Prioridade maxima e [0] minima'))
        gerarSenha(senha, prdd)
    elif menu == 2:
        chamarSenha()
    else:
        print('Digite uma opção valida!')

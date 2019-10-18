####################################################################
# abaixo segue o codigo responsavel por gerar a fila sem prioridade#
####################################################################
class Fila:
    def __init__(self):
        self.fila = []

    # def que insere a senha em uma lista sem prioridade
    def inserir(self,n):
        self.fila.append(n)
    # def que tira  a senha em uma lista sem prioridade
    def excluir(self):
        if not self.vazia():
            return self.fila.pop(0)
    # def que busca o tamanho da lista sem prioridade
    def tamanho(self):
        return len(self.fila)
    # def que verifica se esta vazia a lista sem prioridade
    def vazia(self):
        return self.tamanho() == 0
    # def que mostra as senhas da lista sem prioridade
    def mostrarSenha(self):
        for n in self.fila:
            print("senha N° - ",n," - Prioridade Minima")


####################################################################
# abaixo segue o codigo responsavel por gerar a fila com prioridade#
####################################################################


class FilaPrdd:
    def __init__(self):
        self.filaprdd = []
    # def que insere a senha em uma lista com prioridade
    def inserir(self,n):
        self.filaprdd.append(n)
    # def que tira  a senha em uma lista com prioridade
    def excluir(self):
        if not self.vazia():
            return self.filaprdd.pop(0)

    # def que busca o tamanho da lista com prioridade
    def tamanho(self):
        return len(self.filaprdd)

    # def que verifica se esta vazia a lista com prioridade
    def vazia(self):
        return self.tamanho() == 0

    # def que mostra as senhas da lista com prioridade
    def mostrarSenha(self):
        for n in self.filaprdd:
            print("senha N° - ",n," - Prioridade Maxima")


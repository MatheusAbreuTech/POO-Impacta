# Exercício 3: Uso de Property

# Modifique a classe Lampada do Exercício 2 para usar o
# decorator property. Reescreva os getters e setters usando a
# sintaxe de property. Certifique-se de que a funcionalidade de
# ligar e desligar a lâmpada permaneça a mesma.

class Lampada:
    def __init__(self, estadoInicial):
        self.estado = estadoInicial

    @property
    def estado(self):
        return self.__estado 

    @estado.setter
    def estado(self, novoEstado):
        if(novoEstado == 'desligado' or novoEstado == 'ligado'):
            self.__estado = novoEstado
        else:
            print('valor inválido')
    
lampadaNova = Lampada('desligado')
lampadaNova.estado = 'teste'
lampadaNova.estado = 'ligado'
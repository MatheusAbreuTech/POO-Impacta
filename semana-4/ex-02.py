# Exercício 2: Getters e Setters Simples

# Crie uma classe Lampada com um atributo privado estado
# (ligado/desligado). Implemente métodos getters e setters para o
# atributo estado. O setter deve aceitar apenas os valores
# "ligado" ou "desligado" e alterar o estado da lâmpada de
# acordo.
class Lampada:
    def __init__(self):
        self.__estado = 'desligado'

    def set_Estado(self, estado):
        if(estado == 'desligado' or estado == 'ligado'):
            self.__estado = estado
        else:
            print('valor inválido')

    def get_Estado(self):
        print(self.__estado)

lampadaNova = Lampada()
lampadaNova.get_Estado()
lampadaNova.set_Estado('teste')
lampadaNova.set_Estado('ligado')
lampadaNova.get_Estado()
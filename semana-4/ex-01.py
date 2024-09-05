# Exercício 1: Básico de Membros Públicos e Privados

# Crie uma classe ContaBancaria que tenha um atributo
# privado saldo e um atributo público titular. Inicialize ambos
# os atributos no método __init__. Em seguida, crie um método
# para depositar dinheiro e outro para exibir o saldo, garantindo
# que o saldo não possa ser acessado diretamente de fora da
# classe.

class ContaBancaria:
    def __init__(self, titular):
        self.__saldo = 0
        self.titular = titular
    
    def depositarDinheiro(self, valor):
        if(valor > 0):
            self.__saldo += valor
            print('deposito concluido')
        else:
            print("tu quer depositar oq carai?")
    
    def exibirSaldo(self):
        print(f'Saldo do {self.titular}: {self.__saldo}')



conta = ContaBancaria('André')
conta.exibirSaldo()
conta.depositarDinheiro(100)
conta.exibirSaldo()
conta.depositarDinheiro(-100)

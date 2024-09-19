class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = self.set_idade(idade)

    def set_idade(self, idade):
        if(idade < 18):
            novaIdade = int(input(f"Informe uma idade maior ou igual a 18 anos para o/a {self.nome}: "))
            self.set_idade(novaIdade)
        else:
            self.idade = idade
        return self.idade

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.__salario = salario
    
    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    def calcular_salario_anual(self):
        return self.__salario * 12

class Departamento():
    def __init__(self):
        self.funcionarios = []
    
    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)
    
    def calcular_total_salarios(self):
        return sum(func.calcular_salario_anual() for func in self.funcionarios)
    
    def listar_funcionarios(self):
        for func in self.funcionarios:
            print(f"Nome: {func.nome}, Idade: {func.idade} anos, Salário anual: R$ {func.calcular_salario_anual()}")       

def main():
    func1 = Funcionario("Aline", 17, 1000)
    func2 = Funcionario("João", 19, 4600)
    func3 = Funcionario("Marcelo", 24, 8200.43)

    departamento1 = Departamento()
    departamento1.adicionar_funcionario(func1)
    departamento1.adicionar_funcionario(func2)
    departamento1.adicionar_funcionario(func3)
    print(f'total de salários anuais: R$ {departamento1.calcular_total_salarios()}')
    
    print(departamento1.listar_funcionarios())
            
if(__name__ == "__main__"):
    main()
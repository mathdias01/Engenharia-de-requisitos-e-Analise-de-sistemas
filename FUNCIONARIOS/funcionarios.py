funcionarios = []
escolha = True
max = 100
    

def adicionarFuncionario(funcionarios):
    if len(funcionarios)>= max:
        print("Limite de funcionários atingido!")
        return
    nome = input('Nome: ')
    cargo = input('Cargo: ')
    salario = float(input('Salario: '))
    funcionario = {
    'nome': nome,
    'cargo': cargo,
    'salario': salario
    }
    funcionarios.append(funcionario)
    print('\n Funcionário cadastrado!')
    

def listarFuncionarios(funcionarios):
    if not funcionarios:
        print('\nNenhum funcionário cadastrado.')
        return
    for i, f in enumerate(funcionarios): 
        print(f'{i + 1}) {f['nome']} - {f['cargo']} - R$ {f['salario']:.2f}')


def buscarFuncionario(funcionarios):
    buscar = input('Nome do funcionário: ')
    for i in funcionarios:
        if buscar == i['nome']:
            print(f'cargo: {i['cargo']} | salário: R${i['salario']:.2f}')
            return
    else: 
        print('\nFuncionario não encontrado.')


while escolha:
    print("\n=== SISTEMA DE FUNCIONÁRIOS ===")
    print("1 - Adicionar funcionário")
    print("2 - Listar funcionários")
    print("3 - Buscar funcionário")
    print("0 - Sair")
    escolha = input('Escolha uma opção: ')
    if escolha == '1':
        adicionarFuncionario(funcionarios)
    elif escolha == '2':
        listarFuncionarios(funcionarios)
    elif escolha == '3':
        buscarFuncionario(funcionarios)
    elif escolha == '0':
        escolha = False





listaNomes = {}

opcao = -1


def adicionarAluno(listaNomes):
    nome = input('Nome do aluno: ')
    nota = input('Nota final: ')
    listaNomes[nome] = nota
    return nome, nota
                        
def listarAlunos(listaNomes):
    if len(listaNomes) == 0:
        print('Nenhum aluno cadastrado.')
    else:
        print('\nLista de alunos')
        for nome, nota in listaNomes.items():
            print(f'- {nome} | Nota:{nota}') 
        
def buscarNota():
    name = input('Nome do aluno:')
    if nome == name:
        print(f'Nota de {nome}: {nota}')
    else:
        print('Aluno não encontrado.')






while opcao != 0:
    print('\n=== SISTEMA DE ALUNOS ===')
    print('1 - Adicionar aluno')
    print('2 - Listar alunos')
    print('3 - Buscar nota')
    print('0 - Sair')
    opcao = int(input('Opção: '))
    if opcao == 1:
        nome, nota = adicionarAluno(listaNomes)
        print('Aluno cadastrado com sucesso!')
    if opcao == 2:
        listarAlunos(listaNomes)
    if opcao == 0:
        print('Encerrando...')
    if opcao == 3:
        buscarNota()




    



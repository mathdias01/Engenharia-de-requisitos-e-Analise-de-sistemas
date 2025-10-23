alunos = []

def adicionarAlunos(alunos):
    print('=== SISTEMA DE CADASTRO DE ALUNOS ===')
    for i in range(5):
        nome = input('\nDigite o nome do aluno: ')
        nota = float(input(f'Digite a nota de {nome}: '))
        aluno = {
            'nome': nome,
            'nota': nota
        }
        alunos.append(aluno)

def calcularMedia(alunos):
    soma = 0
    for i in alunos:
        soma += i['nota']
    media = soma/len(alunos)
    return media

def listarAlunos(alunos):
    for i in alunos:
        print(f'{i['nome']} | {i['nota']}')
  

adicionarAlunos(alunos)
listarAlunos(alunos)
md = calcularMedia(alunos)
print(f'Média da turma: {md:.2f}')

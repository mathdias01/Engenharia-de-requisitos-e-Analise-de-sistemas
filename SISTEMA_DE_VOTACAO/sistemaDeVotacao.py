opcoes = ['Opção 1', 'Opção 2', 'Opção 3']
votos = [0, 0, 0]
votacaoAtiva = True
print("=== SISTEMA DE VOTAÇÃO ===")
print('As opções são: ')
for i  in range(len(opcoes)):
    print(f'{i+ 1} - {opcoes[i]}')
    
while votacaoAtiva:
    escolha = input(f'\nEscolha uma opção (1-{len(opcoes)}) ou 0 pra encerrar: ')
    if escolha.isdigit():
        escolha_int = int(escolha)
        if escolha_int == 0:
            votacaoAtiva = False
        elif escolha_int == 1:
            votos[0] += 1
            print(f'Você votou na {opcoes[0]}')
        elif escolha_int == 2:
            votos[1] += 1
            print(f'Você votou na {opcoes[1]}')
        elif escolha_int == 3:
            votos[2] += 1
            print(f'Você votou na {opcoes[2]}')
    else:
        print('Entrada inválida, digite apenas números.')
            
print(f'\n=== RESULTADOS FINAIS ===')
for i  in range(len(opcoes)):
    print(f'{opcoes[i]}: {votos[i]}')


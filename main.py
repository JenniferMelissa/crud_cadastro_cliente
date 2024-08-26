

nomes = {    
    'Nome Completo':'', 
    'Data de Nascimento':'',
    'CPF':'',
    'Profissão':'',
    'E-mail':'',
    'Endereço':'',
    'Telefone':'',
}


while True:
    print(f'{'='*10} Cadastro {'='*10}')
    print('1 - Cadastrar usuário.')
    print('2 - Listar todos os usuários.')
    print('3 - Alterar os dados do usuário.')
    print('4 - Excluir usuário.')
    print('5 - Sair do programa.')



    opcao = input('Informe opção desejada: ')

    match opcao:
        case '1':
            nomes['Nome Completo'] = input('Informe nome completo: ')
            nomes['Data de Nascimento'] = input('Informe data de nascimento: ')
            nomes['CPF'] = input('Informe CPF: ')
            nomes['Profissão'] = input('Informe profissão: ')
            nomes['E-mail'] = input('Informe e-mail: ')
            nomes['Endereço'] = input('Informe endereço: ')
            nomes['Telefone'] = input('Informe telefone: ')


            #exibir dicionario 
            for chave in nomes:
                print(f'{chave}: {nomes.get(chave)}')
            continue
            
        case '2':
            for chave in nomes:
                print(f'{chave}: {nomes.get(chave)}')
                continue

        case '3':
            nomes['Nome Completo'] = input('Informe novo nome completo: ')
            nomes['Data de Nascimento'] = input('Informe nova data de nascimento: ')
            nomes['CPF'] = input('Informe novo CPF: ')
            nomes['Profissão'] = input('Informe nova profissão: ')
            nomes['E-mail'] = input('Informe novo e-mail: ')
            nomes['Endereço'] = input('Informe novo endereço: ')
            nomes['Telefone'] = input('Informe novo telefone: ')
            continue

        case '4':
            del nomes['Nome Completo']
            del nomes['Data de Nascimento']
            del nomes['CPF']
            del nomes['Profissão']
            del nomes['E-mail']
            del nomes['Endereço']
            del nomes['Telefone']
            continue

        case '5':
            print('Saindo do programa.')
            break

        case _:
            print('Opção inválida!')
            continue
            
lista_tarefa = list()

def mostraTarefa(lista_tarefa):
    if lista_tarefa == []:
        print('Sua Lista de Tarefas Esta Vazia.')

    else:
        for indice, valor in enumerate(lista_tarefa):
            print(f'{indice+1} - {valor}')

def criarTarefa(lista_tarefa):
    nova_tarefa = str(input('Digite Sua Nova Tarefa: '))
    lista_tarefa.append(nova_tarefa)

def concluirTarefa(lista_tarefa):
    while True:
        pergunta = input('1 - Concluir Uma Tarefa\n2 - Voltar Para o Menu' \
                    '\nO que quer fazer?: ')

        if pergunta == "1":
            print(25 * '=')
            nome_tarefa = input('Digite o Nome da Tarefa: ')
            if nome_tarefa in lista_tarefa:
                lista_tarefa.remove(nome_tarefa)
                print(25 * '=')
                print(f'A Tarefa {nome_tarefa} Foi Concluida!.')
                break

            else:
                print(25 * '=')
                print('Digite o Nome Exato da Tarefa.')
                print(25 * '=')
                mostraTarefa(lista_tarefa)
                print(25 * '=')

        elif pergunta == "2":
            print(25 * '=')
            print('Voltando...')
            break

        else:
            print('Digite Apenas Numeros de 1 a 2')

def mostraMenu(lista_tarefa):
    while True:
        print(25 * '=')
        pergunta = input('1 - Mostrar Lista de Tarefas\n2 - Criar Uma Tarefa\n3 - Concluir Uma Tarefa\n4 - Sair do Programa\nO que quer fazer?: ')

        if pergunta == "1":
            print(25 * '=')
            mostraTarefa(lista_tarefa)

        elif pergunta == "2":
            print(25 * '=')
            criarTarefa(lista_tarefa)

        elif pergunta == "3":
            if lista_tarefa == []:
                print(25 * '=')
                print('Sua Lista de Tarefas Esta Vazia.')

            else:
                print(25 * '=')
                mostraTarefa(lista_tarefa)
                print(25 * '=')
                concluirTarefa(lista_tarefa)

        elif pergunta == "4":
            print(25 * '=')
            print('Saindo...')
            break

        else:
            print(25 * '=')
            print('Digite Apenas Numeros de 1 a 4')

mostraMenu(lista_tarefa)
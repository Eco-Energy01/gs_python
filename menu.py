from crud_operations import *
from utils import exportar_para_json

def exibir_menu():
    print("\nMenu de Opções:")
    print("1 - Cadastrar Cliente")
    print("2 - Excluir Cliente")
    print("3 - Alterar Cliente")
    print("4 - Consultar Clientes")
    print("5 - Cadastrar Dúvida")
    print("6 - Exportar Consulta para JSON")
    print("7 - Fazer Investimento")
    print("8 - Sair")

def exibir_menu_inicial():
    print("\nBem-vindo ao Sistema!")
    print("1 - Fazer Login")
    print("2 - Cadastrar Cliente")
    print("3 - Sair")

def executar_menu():
    cliente_logado = None
    
    while not cliente_logado:
        exibir_menu_inicial()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            email = input("Email: ")
            senha = input("Senha: ")
            cliente_logado = login(email, senha)
            
            if not cliente_logado:
                print("Login ou senha inválidos. Tente novamente.")
        
        elif opcao == '2':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            cpf = input("CPF: ")
            email = input("Email: ")
            senha = input("Senha: ")
            endereco = input("Endereço: ")
            cadastrar_cliente(nome, telefone, cpf, email, senha, endereco)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

    print("Login bem-sucedido!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            cpf = input("CPF: ")
            email = input("Email: ")
            senha = input("Senha: ")
            endereco = input("Endereço: ")
            cadastrar_cliente(nome, telefone, cpf, email, senha, endereco)
        
        elif opcao == '2':
            id_cliente = input("ID do cliente: ")
            excluir_cliente(id_cliente)
        
        elif opcao == '3':
            id_cliente = input("ID do cliente: ")
            nome = input("Novo Nome: ")
            telefone = input("Novo Telefone: ")
            cpf = input("Novo CPF: ")
            email = input("Novo Email: ")
            senha = input("Nova Senha: ")
            endereco = input("Novo Endereço: ")
            alterar_cliente(id_cliente, nome, telefone, cpf, email, senha, endereco)
        
        elif opcao == '4':
            filtro = input("Digite o filtro para a consulta (ex: nome = 'João'): ")
            clientes = consultar_clientes(filtro)
            for cliente in clientes:
                print(cliente)
        
        elif opcao == '5':
            mensagem = input("Mensagem da dúvida: ")
            assunto = input("Assunto da dúvida: ")
            cadastrar_duvida(cliente_logado, mensagem, assunto)
        
        elif opcao == '6':
            filtro = input("Digite o filtro para exportação (ex: nome = 'João'): ")
            clientes = consultar_clientes(filtro)
            exportar_para_json(clientes)
        
        elif opcao == '7':
            area_de_interesse = input("Área de Interesse: ")
            empresa = input("Nome da Empresa: ")
            setor = input("Setor da Empresa: ")
            telefone = input("Telefone da Empresa: ")
            valor_investimento = float(input("Valor do Investimento: "))
            cadastrar_investimento(area_de_interesse, empresa, setor, telefone, valor_investimento)
        
        elif opcao == '8':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


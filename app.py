from getpass import getpass
import os


def menu():
    print('Bem-vindo ao sistema')
    print('Escolha uma opção')
    print('[1] - Fazer Login')
    print('[2] - Cadastrar novo usuário')


def receber_usuario():
    usuario = input('Nome para novo usuário: ')
    password = getpass('Senha para novo usuário: ')
    return usuario, password


def validar_login():
    with open('usuarios.txt', 'r') as arquivo:
        for linha in arquivo:
            if login == linha:
                print(f'Bem vindo {usuario}, login efetuado com sucesso')
            else:
                print('Usuário ou senha não existem')


def recebe_dados_cadastro():
    nome = input('Nome para novo usuário: ')
    senha = getpass('Senha para novo usuário: ')
    return nome, senha


def cadastrando_usuario():
    with open('usuarios.txt', 'a', newline='', encoding='utf-8') as arquivo:
        arquivo.write(nome + ',' + senha + os.linesep)
        print(f'Usuário {nome} foi cadastrado com sucesso')


while True:
    menu()
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        usuario, password = receber_usuario()
        login = usuario + ',' + password + '\n'
        validar_login()
    elif opcao == 2:
        nome, senha = recebe_dados_cadastro()
        cadastrando_usuario()
        break
    else:
        print('Tente novamente')

usuarios = []
try:
    with (open("arquivo.txt", "r") as arquivo):
        for linha in arquivo:
            linha = linha.strip()
            if linha == "":
                continue
            dados = linha.split(",")
            nome = dados[0]
            email = dados[1]
            senha = dados[2]

            usuario = {
                "nome": nome,
                "email": email,
                "senha": senha
            }
            usuarios.append(usuario)
except FileNotFoundError:
    pass

def menu ():
    print("Escolha uma das opções abaixo: ")
    print("1- Cadastrar")
    print("2- Fazer Login")
    print("3- Sair")

def cadastro_usuarios():
    nome = input("Nome completo: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    if len(senha) < 4:
        print("Digite uma senha maior!")
        return
    novo_cadastro = {
        "nome": nome,
        "email": email,
        "senha": senha
    }
    for usuario in usuarios:
        if email == usuario["email"]:
            print(f"Este email já está cadastrado no nome de: {usuario['nome']}!")
            break
    else:
        usuarios.append(novo_cadastro)
        print("Cadastro realizado com sucesso!")
        with open("arquivo.txt", "a") as arquivo:
            linha = f"{nome},{email},{senha}\n"
            arquivo.write(linha)

def login():
    email_digitado = input("E-mail: ")
    senha_digitado = input("Senha: ")
    usuario_encontrado = False
    for usuario in usuarios:
        if email_digitado == usuario["email"]:
            usuario_encontrado = True
            if senha_digitado == usuario["senha"]:
               print("Usuario logado com sucesso!")
               print(f"Bem-vindo, {usuario['nome']}!")
               break
            else:
                print("Senha incorreta")
                break
    if not usuario_encontrado:
        print("Este email não está cadastrado")

while True:
    menu()
    try:
        opcoes = int(input("Digite a opção escolhida: "))
        if opcoes == 1:
            cadastro_usuarios()
        elif opcoes == 2:
            login()

        elif opcoes == 3:
            print("Saindo do sistema!")
            break
        else:
            print("Número inválido, tente novamente!")

    except ValueError:
        print("Error: Digite um número válido.")

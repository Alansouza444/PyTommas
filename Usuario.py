opc=0; usuario=[]

def incluirUsuario():
    nome=[]
    print("Digite o seu nome: ")
    nome.append(input())
    usuario.append(nome)
    cpf=[]
    print("Digite seu CPF/CNPJ: ")
    cpf.append(int(input()))
    usuario.append(cpf)
    endereco=[]
    print("Digite o seu endereço: ")
    endereco.append(input())
    usuario.append(endereco)
    telefone=[]
    print("Digite o seu telefone: ")
    telefone.append(input())
    usuario.append(telefone)
    email=[]
    print("Digite o seu email: ")
    email.append(input())
    usuario.append(email)
    data=[]
    print("Digite sua data de nascimento: ")
    data.append(input())
    usuario.append(data)

def consultarUsuario():
    print(usuario)

#def alterarUsuario():

def excluirUsuario():
    usuario_deletar=[]
    usuario_deletar.append(input("Qual usuário você deseja deletar? "))
    if(usuario_deletar in usuario):
        usuario.remove(usuario_deletar)
        print("Usuário deletado!")
    else:
        print("Usuário não encontrado!")

while(opc != 5):
    print("\n1 - Incluir Usuário\n")
    print("\n2 - Consultar Usuário\n")
    print("\n3 - Alterar Usuário\n")
    print("\n4 - Excluir Usuário\n")
    print("\n5 - Fim\n")
    print("\nDigite uma opção")
    opc=int(input())
    if(opc == 1):
        incluirUsuario()
    elif(opc == 2):
        consultarUsuario()
    elif (opc == 3):
        alterarUsuario()
    elif (opc == 4):
        excluirUsuario()
    elif (opc == 5):
        print("Fim do programa.")
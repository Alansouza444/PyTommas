produtos = []
opc=0
def incluirProduto():
	novo_produto = []

	print("Digite o id do Produto: ")
	id_produto = int(input())
	novo_produto.append(id_produto)

	print("Digite o nome do produto: ")
	nome_do_produto = input()
	novo_produto.append(nome_do_produto)

	print("Digite o valor do produto: ")
	preco = float(input())
	novo_produto.append(preco)

	print("Digite a descricao do produto: ")
	descricao = input()
	novo_produto.append(descricao)

	produtos.append(novo_produto)

def consultarProduto():
	print("Digite o id do produto: ")
	id = int(input())
	for item in produtos:
		if(item[0] == id):
			print("\nNome: " + item[1])
			print("\nValor: " + str(item[2]))
			print("\nDescricao: " + str(item[3]))
			
def alterarProduto():
	novo_produto = []
	
	print("Digite o id do Produto: ")
	id_produto = int(input())
	novo_produto.append(id_produto)

	print("Digite o nome do produto: ")
	nome_do_produto = input()
	novo_produto.append(nome_do_produto)

	print("Digite o valor do produto: ")
	preco = float(input())
	novo_produto.append(preco)

	print("Digite a descricao do produto: ")
	descricao = input()
	novo_produto.append(descricao)
	
	for item in produtos:
		if(item[0] == id_produto):
			produtos[produtos.index(item)]=novo_produto
			print("Produto alterado!")
	  

def excluirProduto():
	print("Qual o id que deseja deletar do produto?")
	id = int(input())
	for item in produtos:
		if(item[0] == id):
			produtos.remove(item)
			print("Deletado com sucesso!")
    
while(opc !=5):
	print("\nMenu de Opcoes:\n\n")
	print("\n1- Incluir")
	print("\n2- Consultar")
	print("\n3- Alterar")
	print("\n4- Excluir")
	print("\n5- Fim")
	print("\nDigite uma opcao")
	opc=int(input())
	if(opc==1):
		incluirProduto()
	elif(opc==2):
		consultarProduto()
	elif(opc==3):
		alterarProduto()
	elif(opc==4):
		excluirProduto()
	elif(opc==5):
		print("Fim do Programa ......")
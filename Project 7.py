print("Agenda de Contatos")
print("\n1 - Adicionar\n2 - Pesquisar \n3 - Listar\n4 - Sair")

contatos = {}
comando = "" 

def add_contact():
    nome = input("\nNome: ")
    telefone = input("Telefone: ")
    email = input("Email:")

    contatos[nome] = {"telefone": telefone, "email": email} 
    print(f"Contato {nome} Adicionado!")

def search_contact():
    nome = input("Digite o nome para buscar: ")
    if nome in contatos:
        print(f"Telefone: {contatos[nome]['telefone']}")
        print(f"Email: {contatos[nome]['email']}")
    else:
        print("Contato não encontrado")

def list_contacts():
    if contatos:
        for nome, info in contatos.items():
            print(f"{nome} (Tel: {info['telefone']} | Email: {info['email']})")
    else:
        print("Nenhum contato salvo ainda.")

while True:
    comando = input("\nDigite um comando: ").strip()

    if comando == "1":
        add_contact()
    elif comando == "2":
        search_contact()
    elif comando == "3":
        list_contacts()
    elif comando == "4":
        print("Encerrando programa...")
        break
    else:
        print("Comando inválido!")

    


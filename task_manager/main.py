from gerenciador import Gerenciador

def menu():
    print("\nSistema de Gerenciamento de Tarefas")
    print("1. Cadastrar usuário")
    print("2. Cadastrar tarefa")
    print("3. Listar usuários")
    print("4. Listar tarefas")
    print("5. Sair")
    return input("Escolha uma opção: ")

def main():
    gerenciador = Gerenciador()
    
    while True:
        opcao = menu()
        
        if opcao == "1":
            nome = input("Nome do usuário: ")
            email = input("Email do usuário: ")
            usuario = gerenciador.cadastrar_usuario(nome, email)
            print(f"Usuário cadastrado com ID {usuario.id}.")
        
        elif opcao == "2":
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            usuario_id = int(input("ID do usuário responsável: "))
            try:
                tarefa = gerenciador.cadastrar_tarefa(titulo, descricao, usuario_id)
                print(f"Tarefa cadastrada com ID {tarefa.id}.")
            except ValueError as e:
                print(f"Erro: {e}")
        
        elif opcao == "3":
            usuarios = gerenciador.listar_usuarios()
            if usuarios:
                print("\nUsuários cadastrados:")
                for u in usuarios:
                    print(f"ID: {u.id}, Nome: {u.nome}, Email: {u.email}")
            else:
                print("Nenhum usuário cadastrado.")
        
        elif opcao == "4":
            tarefas = gerenciador.listar_tarefas()
            if tarefas:
                print("\nTarefas cadastradas:")
                for t in tarefas:
                    print(f"ID: {t.id}, Título: {t.titulo} , Status: {t.status}, Usuário: {t.usuario.nome}")
            else:
                print("Nenhuma tarefa cadastrada.")
        
        elif opcao == "5":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

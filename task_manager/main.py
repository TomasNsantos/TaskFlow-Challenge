from gerenciador import Gerenciador

def menu():
    gerenciador = Gerenciador()
    
    while True:
        print("\n1. Cadastrar usuário")
        print("2. Cadastrar tarefa")
        print("3. Listar todas as tarefas")
        print("4. Atualizar status de uma tarefa")
        print("5. Filtrar tarefas")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do usuário: ")
            email = input("E-mail do usuário: ")
            try:
                usuario = gerenciador.cadastrar_usuario(nome, email)
                print(f"Usuário {usuario.nome} cadastrado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            usuario_id = int(input("ID do usuário responsável: "))
            try:
                tarefa = gerenciador.cadastrar_tarefa(titulo, descricao, usuario_id)
                print(f"Tarefa '{tarefa.titulo}' cadastrada com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "3":
            tarefas = gerenciador.listar_tarefas()
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            else:
                for t in tarefas:
                    print(f"[{t.id}] {t.titulo} - {t.status} (Usuário: {t.usuario.nome})")
                    print(f"   Descrição: {t.descricao}")

        elif opcao == "4":
            tarefa_id = int(input("ID da tarefa: "))
            print("Escolha o novo status:")
            print("1. Pendente")
            print("2. Em Andamento")
            print("3. Concluído")
            status_opcao = input("Digite o número do novo status: ")
            status_map = {"1": "Pendente", "2": "Em Andamento", "3": "Concluído"}
            novo_status = status_map.get(status_opcao)

            if not novo_status:
                print("Opção inválida.")
            else:
                try:
                    gerenciador.atualizar_status_tarefa(tarefa_id, novo_status)
                    print("Status atualizado com sucesso!")
                except ValueError as e:
                    print(f"Erro: {e}")

        elif opcao == "5":
            print("Opções de filtro:")
            print("1. Listar apenas tarefas Pendentes")
            print("2. Listar apenas tarefas Em Andamento")
            print("3. Listar apenas tarefas Concluídas")
            print("4. Listar tarefas por usuário")
            
            filtro_opcao = input("Escolha uma opção: ")
            if filtro_opcao in ["1", "2", "3"]:
                status_map = {"1": "Pendente", "2": "Em Andamento", "3": "Concluído"}
                status_filtro = status_map[filtro_opcao]
                tarefas = gerenciador.listar_tarefas(status_filtro=status_filtro)
            elif filtro_opcao == "4":
                usuario_id = int(input("ID do usuário: "))
                tarefas = gerenciador.listar_tarefas(usuario_id=usuario_id)
            else:
                print("Opção inválida.")
                continue
            
            if not tarefas:
                print("Nenhuma tarefa encontrada com esse filtro.")
            else:
                for t in tarefas:
                    print(f"[{t.id}] {t.titulo} - {t.status} (Usuário: {t.usuario.nome})")
                    print(f"   Descrição: {t.descricao}")

        elif opcao == "6":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

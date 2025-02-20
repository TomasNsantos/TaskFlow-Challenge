from usuario import Usuario

class Tarefa:
    contador_id = 1  # Para gerar IDs automaticamente
    
    def __init__(self, titulo: str, descricao: str, usuario: Usuario):
        self.id = Tarefa.contador_id
        self.titulo = titulo
        self.descricao = descricao
        self.status = "Pendente"  # Status inicial
        self.usuario = usuario  # Associa a um usuário
        Tarefa.contador_id += 1  # Incrementa o ID para a próxima tarefa
    
    def atualizar_status(self, novo_status: str):
        if novo_status in ["Pendente", "Em Andamento", "Concluído"]:
            self.status = novo_status
        else:
            raise ValueError("Status inválido. Escolha entre: Pendente, Em Andamento, Concluído.")
    
    def __repr__(self):
        return f"Tarefa(ID: {self.id}, Título: {self.titulo}, Status: {self.status}, Usuário: {self.usuario.nome})"
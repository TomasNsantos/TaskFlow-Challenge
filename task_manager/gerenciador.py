from usuario import Usuario
from tarefa import Tarefa
from persistencia import Persistencia

class Gerenciador:
    def __init__(self):
        self.usuarios = Persistencia.carregar_usuarios()
        self.tarefas = Persistencia.carregar_tarefas(self.usuarios)

    def cadastrar_usuario(self, nome: str, email: str):
        if any(u.email == email for u in self.usuarios):
            raise ValueError("Usuário com este e-mail já existe.")
        
        usuario = Usuario(nome, email)
        self.usuarios.append(usuario)
        Persistencia.salvar_usuarios(self.usuarios)
        return usuario

    def cadastrar_tarefa(self, titulo: str, descricao: str, usuario_id: int):
        usuario = next((u for u in self.usuarios if u.id == usuario_id), None)
        if not usuario:
            raise ValueError("Usuário não encontrado.")
        
        if any(t.titulo == titulo and t.descricao == descricao and t.usuario.id == usuario_id for t in self.tarefas):
            raise ValueError("Tarefa já cadastrada para este usuário.")
        
        tarefa = Tarefa(titulo, descricao, usuario)
        self.tarefas.append(tarefa)
        Persistencia.salvar_tarefas(self.tarefas)
        return tarefa

    def atualizar_status_tarefa(self, tarefa_id: int, novo_status: str):
        tarefa = next((t for t in self.tarefas if t.id == tarefa_id), None)
        if not tarefa:
            raise ValueError("Tarefa não encontrada.")
        
        if novo_status not in ["Pendente", "Em Andamento", "Concluído"]:
            raise ValueError("Status inválido.")
        
        tarefa.status = novo_status
        Persistencia.salvar_tarefas(self.tarefas)

    def listar_usuarios(self):
        return self.usuarios

    def listar_tarefas(self, status_filtro=None, usuario_id=None):
        tarefas_filtradas = self.tarefas
        if status_filtro:
            tarefas_filtradas = [t for t in tarefas_filtradas if t.status == status_filtro]
        if usuario_id:
            tarefas_filtradas = [t for t in tarefas_filtradas if t.usuario.id == usuario_id]
        return tarefas_filtradas

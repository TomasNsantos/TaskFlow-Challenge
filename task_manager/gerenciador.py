import json
from usuario import Usuario
from tarefa import Tarefa

class Gerenciador:
    def __init__(self):
        self.usuarios = self.carregar_usuarios()
        self.tarefas = self.carregar_tarefas()

    def cadastrar_usuario(self, nome: str, email: str):
        # Verifica se o usuário já existe
        if any(u.email == email for u in self.usuarios):
            raise ValueError("Usuário com este e-mail já existe.")
        
        usuario = Usuario(nome, email)
        self.usuarios.append(usuario)
        self.salvar_usuarios()
        return usuario

    def cadastrar_tarefa(self, titulo: str, descricao: str, usuario_id: int):
        usuario = next((u for u in self.usuarios if u.id == usuario_id), None)
        if not usuario:
            raise ValueError("Usuário não encontrado.")
        
        # Verifica se a tarefa já existe para o mesmo usuário
        if any(t.titulo == titulo and t.descricao == descricao and t.usuario.id == usuario_id for t in self.tarefas):
            raise ValueError("Tarefa já cadastrada para este usuário.")
        
        tarefa = Tarefa(titulo, descricao, usuario)
        self.tarefas.append(tarefa)
        self.salvar_tarefas()
        return tarefa

    def salvar_usuarios(self):
        with open("usuarios.json", "w") as f:
            json.dump([vars(u) for u in self.usuarios], f, indent=4)

    def salvar_tarefas(self):
        with open("tasks.json", "w") as f:
            json.dump([{
                "id": t.id,
                "titulo": t.titulo,
                "descricao": t.descricao,
                "status": t.status,
                "usuario": {"id": t.usuario.id, "nome": t.usuario.nome, "email": t.usuario.email}
            } for t in self.tarefas], f, indent=4)

    def carregar_usuarios(self):
        try:
            with open("usuarios.json", "r") as f:
                return list({u["email"]: Usuario(**u) for u in json.load(f)}.values())  # Remove duplicatas pelo e-mail
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def carregar_tarefas(self):
        try:
            with open("tasks.json", "r") as f:
                tarefas = json.load(f)
                tarefas_unicas = []
                seen = set()
                for t in tarefas:
                    key = (t["titulo"], t["descricao"], t["usuario"]["id"])
                    if key not in seen:
                        seen.add(key)
                        tarefas_unicas.append(Tarefa(t["titulo"], t["descricao"], self.buscar_usuario_por_id(t["usuario"]["id"])))
                return tarefas_unicas
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def buscar_usuario_por_id(self, usuario_id: int):
        return next((u for u in self.usuarios if u.id == usuario_id), None)

    def listar_usuarios(self):
        return self.usuarios

    def listar_tarefas(self):
        return self.tarefas

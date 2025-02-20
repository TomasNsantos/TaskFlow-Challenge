import json
from usuario import Usuario
from tarefa import Tarefa

class Persistencia:
    @staticmethod
    def salvar_usuarios(usuarios, arquivo="usuarios.json"):
        with open(arquivo, "w") as f:
            json.dump([vars(u) for u in usuarios], f, indent=4)

    @staticmethod
    def salvar_tarefas(tarefas, arquivo="tasks.json"):
        with open(arquivo, "w") as f:
            json.dump([
                {
                    "id": t.id,
                    "titulo": t.titulo,
                    "descricao": t.descricao,
                    "status": t.status,
                    "usuario": {
                        "id": t.usuario.id, 
                        "nome": t.usuario.nome, 
                        "email": t.usuario.email
                    }
                } for t in tarefas
            ], f, indent=4)

    @staticmethod
    def carregar_usuarios(arquivo="usuarios.json"):
        try:
            with open(arquivo, "r") as f:
                return list({u["email"]: Usuario(**u) for u in json.load(f)}.values())  # Remove duplicatas pelo e-mail
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def carregar_tarefas(usuarios, arquivo="tasks.json"):
        try:
            with open(arquivo, "r") as f:
                tarefas = json.load(f)
                tarefas_unicas = []
                seen = set()
                for t in tarefas:
                    key = (t["titulo"], t["descricao"], t["usuario"]["id"])
                    if key not in seen:
                        seen.add(key)
                        usuario = next((u for u in usuarios if u.id == t["usuario"]["id"]), None)
                        if usuario:
                            tarefas_unicas.append(Tarefa(t["titulo"], t["descricao"], usuario, t["status"]))
                return tarefas_unicas
        except (FileNotFoundError, json.JSONDecodeError):
            return []

class Usuario:
    contador_id = 1  # Para gerar IDs automaticamente
    
    def __init__(self, nome: str, email: str):
        self.id = Usuario.contador_id
        self.nome = nome
        self.email = email
        Usuario.contador_id += 1  # Incrementa o ID para o próximo usuário
    
    def __repr__(self):
        return f"Usuario(ID: {self.id}, Nome: {self.nome}, Email: {self.email})"
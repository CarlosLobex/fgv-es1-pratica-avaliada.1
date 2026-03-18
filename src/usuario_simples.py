import hashlib


class Usuario:
    """Classe simplificada de usuário (seguindo YAGNI)"""

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = self._hash_senha(senha)

    def _hash_senha(self, senha: str) -> str:
        return hashlib.sha256(senha.encode()).hexdigest()

    def validar_senha(self, senha: str) -> bool:
        return self._hash_senha(senha) == self.senha


class GerenciadorUsuarios:
    """Gerenciador simplificado (apenas o necessário)"""

    def __init__(self):
        self.usuarios = []

    def cadastrar(self, nome: str, email: str, senha: str):

        # validar email duplicado
        for u in self.usuarios:
            if u.email == email:
                raise ValueError("Email já cadastrado")

        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)
        return usuario

    def fazer_login(self, email: str, senha: str):

        for u in self.usuarios:
            if u.email == email and u.validar_senha(senha):
                return u

        return None

    def listar_todos(self):
        return self.usuarios

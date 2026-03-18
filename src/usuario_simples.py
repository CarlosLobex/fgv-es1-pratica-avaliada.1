import hashlib


class Usuario:
    """Classe simplificada de usuário (seguindo YAGNI)"""

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = self._hash_senha(senha)

    def _hash_senha(self, senha: str) -> str:
        """Gera hash da senha"""
        return hashlib.sha256(senha.encode()).hexdigest()

    def validar_senha(self, senha: str) -> bool:
        """Valida a senha informada"""
        return self._hash_senha(senha) == self.senha


class GerenciadorUsuarios:
    """Gerenciador simplificado (apenas o necessário)"""

    def __init__(self):
        self.usuarios: list[Usuario] = []

    def cadastrar(self, nome: str, email: str, senha: str):
        """Cadastra um novo usuário se o email não estiver em uso."""

        if any(u.email == email for u in self.usuarios):
            raise ValueError("Email já cadastrado")

        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)
        return usuario

    def fazer_login(self, email: str, senha: str):
        """Realiza login verificando email e senha."""

        for u in self.usuarios:
            if u.email == email and u.validar_senha(senha):
                return u

        return None

    def listar_usuarios(self):
        """Retorna a lista de usuários cadastrados."""
        return self.usuarios

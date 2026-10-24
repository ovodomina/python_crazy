import os 

def validar_email(email: str) -> bool:
    """Verifica se existe um '@' e um '.' no e-mail."""
    return "@" in email and "." in email

def eh_maior_de_idade(idade: int) -> bool:
    """Verifica se o usuário tem 18 anos ou mais."""
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    return idade >= 18
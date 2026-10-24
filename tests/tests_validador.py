import pytest
from src.validador import validar_email, eh_maior_de_idade

def test_validar_email_correto():
    assert validar_email("contato@fatec.edu.br") is True

def test_maioridade_sucesso():
    # ERRO DE LÓGICA: O teste espera um resultado errado
    assert eh_maior_de_idade(20) is False 

def test_idade_negativa():
    with pytest.raises(ValueError):
        eh_maior_de_idade(-5)
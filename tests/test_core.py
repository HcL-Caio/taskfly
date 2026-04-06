from src.core import TaskFlyCore


def test_criacao_usuario_novo():
    # Teste 1: Caminho feliz (Garante que um usuário novo começa zerado)
    sistema = TaskFlyCore(None)
    assert sistema.user_data['xp'] == 0
    assert sistema.user_data['level'] == 1
    assert len(sistema.user_data['medals']) == 0


def test_conclusao_tarefa_dificuldade_invalida():
    # Teste 2: Entrada inválida (O edital exige testar algo inválido)
    sistema = TaskFlyCore(None)
    xp_antes = sistema.user_data['xp']
    
    # Mandando uma dificuldade que não existe
    sistema.complete_task("Estudar", "super_dificil") 
    
    # Como é inválido, o sistema deve assumir 'medium' (20 XP)
    assert sistema.user_data['xp'] == xp_antes + 20


def test_subida_de_nivel():
    # Teste 3: Caso limite / Variação importante (Subir de nível ao passar de 100 XP)
    sistema = TaskFlyCore(None)
    
    # Forçando o XP para 90 (Nível 1)
    sistema.user_data['xp'] = 90 
    
    # Completando tarefa média (ganha 20 XP, vai para 110 XP)
    sistema.complete_task("Ler livro", "medium")
    
    # O nível tem que ter subido para 2 e o XP restante deve ser 10
    assert sistema.user_data['level'] == 2
    assert sistema.user_data['xp'] == 10

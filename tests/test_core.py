from src.core import TaskFlyCore


def test_criacao_usuario_novo():
    sistema = TaskFlyCore(None)
    assert sistema.user_data['xp'] == 0
    assert sistema.user_data['level'] == 1
    assert len(sistema.user_data['medals']) == 0


def test_conclusao_tarefa_dificuldade_invalida():
    sistema = TaskFlyCore(None)
    xp_antes = sistema.user_data['xp']
    sistema.complete_task("Estudar", "super_dificil")
    assert sistema.user_data['xp'] == xp_antes + 20


def test_subida_de_nivel():
    sistema = TaskFlyCore(None)
    sistema.user_data['xp'] = 90
    sistema.complete_task("Ler livro", "medium")
    assert sistema.user_data['level'] == 2
    assert sistema.user_data['xp'] == 10

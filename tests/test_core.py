from src.core import TaskFlyCore


def test_criacao_usuario_novo():
    sistema = TaskFlyCore(None)
    assert sistema.user_data['xp'] == 0
    assert sistema.user_data['level'] == 1


def test_conclusao_tarefa():
    sistema = TaskFlyCore(None)
    sistema.complete_task("Teste", "easy")
    assert sistema.user_data['xp'] == 10


def test_subida_nivel():
    sistema = TaskFlyCore({'xp': 90, 'level': 1, 'medals': []})
    sistema.complete_task("Teste", "medium")
    assert sistema.user_data['level'] == 2
    assert sistema.user_data['xp'] == 10

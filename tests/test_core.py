from src.core import TaskFlyCore


def test_gain_xp():
    system = TaskFlyCore()
    result = system.complete_task("Academia", "hard")
    assert system.user_data["xp"] == 50
    assert "Tarefa 'Academia' concluída" in result


def test_level_up():
    system = TaskFlyCore({"xp": 90, "level": 1, "medals": []})
    result = system.complete_task("Estudar", "medium")  # +20 XP = 110 total
    assert system.user_data["level"] == 2
    assert "subiu para o nível 2" in result


def test_invalid_difficulty_fallback():
    system = TaskFlyCore()
    system.complete_task("Tarefa", "invalid")
    assert system.user_data["xp"] == 10  # Fallback para easy

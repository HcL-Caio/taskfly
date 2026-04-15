import json
from src.core import TaskFlyCore
from src.api import get_advice


def load_data():
    try:
        with open('taskfly_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'xp': 0, 'level': 1, 'medals': []}


def save_data(data):
    with open('taskfly_data.json', 'w') as f:
        json.dump(data, f)


def main():
    user_data = load_data()
    core = TaskFlyCore(user_data)
    print("--- Bem-vindo ao TaskFly ---")
    while True:
        print(f"\nNível: {core.user_data['level']} | XP: {core.user_data['xp']}")
        print("1. Adicionar Tarefa\n2. Ver Medalhas\n3. Sair")
        op = input("Escolha: ")
        if op == '1':
            desc = input("Tarefa: ")
            diff = input("Dificuldade (easy/medium/hard): ")
            core.complete_task(desc, diff)
            save_data(core.user_data)
        elif op == '2':
            print(f"Medalhas: {', '.join(core.user_data['medals'])}")
        elif op == '3':
            break


if __name__ == '__main__':
    main()

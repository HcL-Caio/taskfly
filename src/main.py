import json
import os
from src.core import TaskFlyCore


DATA_FILE = "taskfly_data.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def main():
    print("=== Bem-vindo ao TaskFly! 🚀 ===")
    user_data = load_data()
    system = TaskFlyCore(user_data)

    while True:
        xp = system.user_data['xp']
        lvl = system.user_data['level']
        medals = len(system.user_data['medals'])
        print(f"\n[ Nível: {lvl} | XP: {xp} | Medalhas: {medals} ]")
        print("1. Concluir uma Tarefa")
        print("2. Ver minhas Medalhas")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            tarefa = input("Qual tarefa você concluiu? ")
            dificuldade = input("Dificuldade (easy/medium/hard): ").lower()
            if dificuldade not in ['easy', 'medium', 'hard']:
                print("Dificuldade inválida. Usando 'medium' por padrão.")
                dificuldade = 'medium'

            msg = system.complete_task(tarefa, dificuldade)
            print(f"\n✅ {msg}")

            medalha_msg = system.check_medals()
            if medalha_msg:
                print(f"🎉 {medalha_msg}")

            save_data(system.user_data)

        elif escolha == '2':
            print("\n--- Suas Medalhas ---")
            if not system.user_data['medals']:
                print("Você ainda não tem medalhas. Continue focado!")
            else:
                for m in system.user_data['medals']:
                    print(f"🏅 {m}")

        elif escolha == '3':
            print("\nAté a próxima! Voe alto! 🦅\n")
            break
        else:
            print("\nOpção inválida. Tente novamente.")
            
if __name__ == "__main__":
    main()

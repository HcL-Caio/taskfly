class TaskFlyCore:
    def __init__(self, user_data=None):
        self.user_data = user_data or {"xp": 0, "level": 1, "medals": []}

    def complete_task(self, task_name, difficulty="medium"):
        # Regra de negócio: XP baseado na dificuldade
        xp_map = {"easy": 10, "medium": 20, "hard": 50}
        gain = xp_map.get(difficulty, 10)
        
        self.user_data["xp"] += gain
        
        # Lógica de Level Up (Simples: cada 100 XP sobe um nível)
        new_level = (self.user_data["xp"] // 100) + 1
        if new_level > self.user_data["level"]:
            self.user_data["level"] = new_level
            return f"Parabéns! Você subiu para o nível {new_level}!"
        
        return f"Tarefa '{task_name}' concluída! +{gain} XP."

    def check_medals(self):
        # Exemplo: Medalha de Iniciante ao chegar no Level 2
        if self.user_data["level"] >= 2 and "Iniciante Alado" not in self.user_data["medals"]:
            self.user_data["medals"].append("Iniciante Alado")
            return "Nova Medalha Desbloqueada: Iniciante Alado! 🎖️"
        return None
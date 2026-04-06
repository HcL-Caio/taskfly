class TaskFlyCore:
    def __init__(self, user_data):
        self.user_data = user_data or {'xp': 0, 'level': 1, 'medals': []}

    def complete_task(self, description, difficulty):
        xp_map = {'easy': 10, 'medium': 20, 'hard': 50}
        gain = xp_map.get(difficulty.lower(), 10)
        self.user_data['xp'] += gain
        self._check_level_up()

    def _check_level_up(self):
        if self.user_data['xp'] >= 100:
            self.user_data['level'] += 1
            self.user_data['xp'] -= 100
            self._award_medal()

    def _award_medal(self):
        m = f"Medalha Nível {self.user_data['level']}"
        if m not in self.user_data['medals']:
            self.user_data['medals'].append(m)

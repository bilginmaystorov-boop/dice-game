class Player:
    def __init__(self, name: str):
        self.rolled_1 = 0
        self.rolled_2 = 0
        self.rolled_3 = 0
        self.rolled_4 = 0
        self.rolled_5 = 0
        self.rolled_6 = 0
        self.total_rolls = 0
        self.name = name

    def get_name(self):
        return self.name

    def update_stats(self, roll):
        if roll == 1:
            self.rolled_1 += 1
            self.total_rolls += 1
        if roll == 2:
            self.rolled_2 += 1
            self.total_rolls += 1
        if roll == 3:
            self.rolled_3 += 1
            self.total_rolls += 1
        if roll == 4:
            self.rolled_4 += 1
            self.total_rolls += 1
        if roll == 5:
            self.rolled_5 += 1
            self.total_rolls += 1
        if roll == 6:
            self.rolled_6 += 1
            self.total_rolls += 1

    def get_stats(self):
        return {
            "rolled_1": self.rolled_1,
            "rolled_2": self.rolled_2,
            "rolled_3": self.rolled_3,
            "rolled_4": self.rolled_4,
            "rolled_5": self.rolled_5,
            "rolled_6": self.rolled_6,
            "total_rolls": self.total_rolls,
        }

    def load_stats(self, stats_dict):
        self.rolled_1 = stats_dict.get("rolled_1", 0)
        self.rolled_2 = stats_dict.get("rolled_2", 0)
        self.rolled_3 = stats_dict.get("rolled_3", 0)
        self.rolled_4 = stats_dict.get("rolled_4", 0)
        self.rolled_5 = stats_dict.get("rolled_5", 0)
        self.rolled_6 = stats_dict.get("rolled_6", 0)
        self.total_rolls = stats_dict.get("total_rolls", 0)


class StakeCalculator:
    
    def __init__(self, rank: str, progress: float):
        self.rank = rank
        self.progress = progress
        self.rank_conditions = {
            "bronze": 10000,
            "silver": 50000,
            "gold": 100000,
            "platinum": 250000,
            "platinum2": 500000,
            "platinum3": 1000000,
            "platinum4": 2500000,
            "platinum5": 5000000,
            "platinum6": 10000000,
            "diamond": 25000000,
        }

        self.rank_percent = {
            "bronze": 100,
            "silver": 500,
            "gold": 1000,
            "platinum": 2500,
            "platinum2": 5000,
            "platinum3": 10000,
            "platinum4": 25000,
            "platinum5": 50000,
            "platinum6": 100000,
            "diamond": 250000,
        }

        self.rank_reward = {
            "bronze": 15,
            "silver": 50,
            "gold": 110,
            "platinum": 200,
            "platinum2": 400,
            "platinum3": 800,
            "platinum4": 1600,
            "platinum5": 3200,
            "platinum6": 6400,
            "diamond": 12800,
        }

    def calc(self):
        rank = self.rank
        required_percent = 100 - self.progress
        required_dollars = required_percent * self.rank_percent[rank]
        return required_percent, required_dollars

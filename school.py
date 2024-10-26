import pandas as pd
from utility import calc_utility

class School():
    def __init__(self, name: str, q_total: int, q_male: int, q_female: int):
        self.name = name
        self.q_total = q_total
        self.q_female = q_female 
        self.q_male = q_male
        self.q_either = q_total - q_female - q_male
        self.students = pd.DataFrame(columns=["rank", "sex", "ability"], dtype=int)
    
    def update_utility(self):
        self.ability_sum, self.diversity_factor, self.utility = calc_utility(self.students)

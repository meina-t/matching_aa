import numpy as np
import pandas as pd

from unique_school import select_aa
from utility import calc_utility
from utils import make_applicants_df

def run_unique_school_with_quota(male_a, female_a, q, q_f_range, trials=3):
    results = []
    for q_f in q_f_range:
        results_q_f = []
        for seed in range(trials):
            applicants_df = make_applicants_df(male_a, female_a, seed)
            top_q_df, selected_df= select_aa(applicants_df, q, q_f)
            ability_sum, diversity_factor, utility = calc_utility(selected_df)
            results_q_f.append((seed, utility, ability_sum, diversity_factor))
        results_q_f_df = pd.DataFrame(results_q_f, columns=['seed', 'utility', 'ability_sum', 'diversity_factor'])

        # それぞれの平均を追加
        results.append((q_f, results_q_f_df['utility'].mean(), results_q_f_df['ability_sum'].mean(), results_q_f_df['diversity_factor'].mean()))
    results_df = pd.DataFrame(results, columns=['q_f', 'utility', 'ability_sum', 'diversity_factor'])
    return results_df

def run_unique_school_with_quota_female(a, q, a_p_range, q_f_range, trials=3):
    results = pd.DataFrame({'female_proportion': [], 'q_f': [], 'utility': [], 'ability_sum': [], 'diversity_factor': []})
    for a_prop in a_p_range:
        female_a = int(a * a_prop)
        male_a = a - female_a
        
        results_a = run_unique_school_with_quota(male_a, female_a, q, q_f_range, trials)
        results_a["female_proportion"] = a_prop
        results = pd.concat([results, results_a])
    return results


        
def calc_utility(df):
    """
    args:
    df: DataFrame, selected people. (columns: sex, ability)

    return:
    ability_sum: float, sum of the ability of the selected people
    diversity_factor: float, diversity factor of the selected people
    utility: float, utility of the selected people
    """
    total_count = len(df)
    female_ratio = len(df[df['sex'] == 'female']) / total_count
    male_ratio = len(df[df['sex'] == 'male']) / total_count

    diversity_factor = female_ratio * male_ratio

    ability_sum = df['ability'].sum()

    utility = diversity_factor * ability_sum

    return ability_sum, diversity_factor, utility


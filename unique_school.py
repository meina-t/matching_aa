import pandas as pd

def select_aa(df, q, q_f):
    """
    args:
    df: DataFrame (columns: sex, ability)
    q: int, the number of people to select
    q_f: int, the lower limit of the female's number

    return: 
    top_q_df: DataFrame, the originally selected people
    selected_df: DataFrame, the selected people
    len(top_woman_df): int, the number of woman originally selected
    """
    sorted_df = df.sort_values(by='ability', ascending=False)
    top_q_df = sorted_df.head(q)

    top_female_df = top_q_df[top_q_df['sex'] == 'female']
    top_male_df = top_q_df[top_q_df['sex'] == 'male']

    female_count = len(top_female_df)
    # 女子がq_f人に満たない場合、女子の追加分を選ぶ
    if female_count < q_f:
        deficit = q_f - female_count

        remaining_female_df = sorted_df[(sorted_df['sex'] == 'female') & (~sorted_df.index.isin(top_female_df.index))]
        additional_female_df = remaining_female_df.head(deficit)

        top_male_df = top_male_df.head(len(top_male_df) - deficit)
        selected_df = pd.concat([top_female_df, additional_female_df, top_male_df])
    else:
        selected_df = top_q_df

    return top_q_df, selected_df
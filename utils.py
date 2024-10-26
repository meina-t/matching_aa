import numpy as np
import pandas as pd
import random
import plotly.express as px
import plotly.graph_objects as go


def make_applicants_df(male_a, female_a, seed):
    np.random.seed(seed)
    sex = ['female'] * female_a + ['male'] * male_a
    ability = np.random.normal(50, 10, female_a + male_a)
    df = pd.DataFrame({'sex': sex, 'ability': ability})
    return df


def plot_ability_distribution_by_sex(df):
    fig = go.Figure()

    # Adding histogram for males
    fig.add_trace(go.Histogram(
        x=df[df['sex'] == 'male']['ability'],
        name='Male',
        opacity=0.75
    ))

    # Adding histogram for females
    fig.add_trace(go.Histogram(
        x=df[df['sex'] == 'female']['ability'],
        name='Female',
        opacity=0.75
    ))

    # Update layout
    fig.update_layout(
        title='Ability Distribution by Sex',
        xaxis_title='Ability',
        yaxis_title='Count',
        barmode='overlay'  # Overlay both histograms in the same graph
    )

    # Fix x-axis range
    fig.update_xaxes(range=[0, 100])

    # Show plot
    fig.show()

def make_applicants_df_with_preferences(male_a, female_a, school_names, seed):
    applicants_df = make_applicants_df(male_a, female_a, seed)
    applicants_df['school_preference'] = applicants_df.apply(lambda x: random.sample(school_names, len(school_names)), axis=1)
    return applicants_df
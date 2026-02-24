import pandas as pd

def run_step(context):
    print('Normalizing data...')
    df = context['population']
    total_pop = context['pop_new']
    df['pop_share'] = (df['pop'] / df['pop'].sum()).astype(float)
    df['pop_normalized'] = (df['pop_share'] * total_pop).astype(float)
    context['population'] = df
    return context
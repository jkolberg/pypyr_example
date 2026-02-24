import pandas as pd
from iteround import saferound

def run_step(context):
    print('Rounding data...')
    df = context['population']
    df['pop_rounded'] = saferound(df['pop_normalized'], 0)
    df['pop_rounded'] = df['pop_rounded'].astype(int)
    context['population'] = df
    return context
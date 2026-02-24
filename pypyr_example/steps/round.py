import pandas as pd
from iteround import saferound

def run_step(context):
    print('Rounding data...')
    df = context['employment_normalized'].copy()
    df['jobs_rounded'] = saferound(df['jobs_normalized'], 0)
    df['jobs_rounded'] = df['jobs_rounded'].astype(int)
    context['employment_rounded'] = df
    return context
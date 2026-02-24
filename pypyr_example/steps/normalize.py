import pandas as pd

def run_step(context):
    print('Normalizing data...')
    df = context['employment'].copy()
    total_jobs = context['total_jobs_new']
    df['jobs_share'] = (df['jobs'] / df['jobs'].sum()).astype(float)
    df['jobs_normalized'] = (df['jobs_share'] * total_jobs).astype(float)
    context['employment_normalized'] = df
    return context
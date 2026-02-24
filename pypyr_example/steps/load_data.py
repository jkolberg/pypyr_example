import pandas as pd

def load_data(data_dir):
    df = (
        pd.read_csv(f'{data_dir}/Employment 2020.csv')
        .rename(columns={'Emp_Total': 'jobs'})
    )[['control_id','control_name','jobs']]
    return df

def run_step(context):
    data_dir = context['data_dir']
    print(f'Loading data from {data_dir}...')
    context['employment'] = load_data(data_dir)
    return context
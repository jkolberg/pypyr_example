import pandas as pd

def create_block_group_id(df):
    df['block_group_id'] = (
        df['state'].astype(str)
        + df['county'].astype(str).str.zfill(3)
        + df['tract'].astype(str).str.zfill(6)
        + df['block group'].astype(str)
    )
    return df

def load_data(data_dir):
    df = (
        pd.read_csv(f'{data_dir}/ofm_control_totals.csv')
        .rename(columns={'POP2018': 'pop'})
    )
    df = create_block_group_id(df)
    return df[['block_group_id', 'pop']]

def run_step(context):
    data_dir = context['data_dir']
    print(f'Loading data from {data_dir}...')
    context['population'] = load_data(data_dir)
    return context
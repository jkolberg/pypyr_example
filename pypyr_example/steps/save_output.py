import pandas as pd

def run_step(context):
    output_dir = context['output_dir']
    print(f'Saving output to {output_dir}...')
    context['population'].to_csv(f'{output_dir}/population.csv', index=False)
    return context
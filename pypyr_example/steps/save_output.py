import pandas as pd

def run_step(context):
    output_dir = context['output_dir']
    print(f'Saving output to {output_dir}...')
    context['employment'].to_csv(f'{output_dir}/employment.csv', index=False)
    context['employment_normalized'].to_csv(f'{output_dir}/employment_normalized.csv', index=False)
    context['employment_rounded'].to_csv(f'{output_dir}/employment_rounded.csv', index=False)
    return context
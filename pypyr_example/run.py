from pypyr import pipelinerunner

pipelinerunner.run(
    pipeline_name='settings', 
    dict_in={
        'data_dir': 'data',
        'output_dir': 'output',
        'pop_new':4200000
    }
)

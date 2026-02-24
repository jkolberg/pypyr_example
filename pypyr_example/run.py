from pypyr import pipelinerunner

pipelinerunner.run(
    'settings', 
    dict_in={
        'data_dir': 'data',
        'output_dir': 'output'
    }
)

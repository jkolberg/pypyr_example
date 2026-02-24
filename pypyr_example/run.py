from pypyr import pipelinerunner

pipelinerunner.run(
    pipeline_name='settings', 
    dict_in={
        'data_dir': 'data',
        'output_dir': 'output',
        'total_jobs_new':2400000
    }
)

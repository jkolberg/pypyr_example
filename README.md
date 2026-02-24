# Pypyr pipeline example
------------
Pypyr runs .py files in order specified by a yaml file, in this example settings.yaml.

# Installation
------------
1. Install uv
    1. Open Powershell as administrator
    2. Enter the following:    
    ```
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

2. Switch to CMD and clone the repository
```
git clone https://github.com/jkolberg/pypyr_example.git
```

3. Run the example with uv
```
cd pypyr_example/pypyr_example
uv run run.py
```
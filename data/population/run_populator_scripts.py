import subprocess

def run_script(script_path):
    result = subprocess.run(['python', script_path], check=True, text=True, capture_output=True)
    print(f"Output from {script_path}:")
    print(result.stdout)
    if result.stderr:
        print(f"Errors from {script_path}:")
        print(result.stderr)

# asos dataset

## Run setup if needed
try:
    run_script('population/asos/setup.py')

## Run population
finally:
    run_script('population/asos/data_to_db.py')
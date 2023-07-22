import subprocess

# Run the first script and wait for it to finish
subprocess.run(['python3', 'main.py'])

# Run the second script
subprocess.run(['python', 'ytsearch.py'])

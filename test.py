import os

# Get the list of environment variables
env_vars = os.environ

# Print each environment variable
for key, value in env_vars.items():
    print(f'{key}: {value}')
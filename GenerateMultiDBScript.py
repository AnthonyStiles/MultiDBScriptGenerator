import os
import yaml

print('CHECKING CONFIG FILE...')
config_file_name = 'config.yaml'

with open(config_file_name, 'r') as config_file:
    config = yaml.safe_load(config_file)

databases = config['databases']
scripts = config['scripts']

print(f'FOUND {len(databases)} DATABASE(S) AND {len(scripts)} SCRIPT(S)')

print('GENERATING SCRIPT...')

script_name = 'output.sql'

with open (script_name, 'w') as output:
    for db in databases:
        output.write(f'USE {db}\n\n')
        output.write(f'GO\n\n')
        for script in scripts:
            output.write(f':r {script}\n')
        output.write('\n\n')

    output.write("--Now just open this in SQL Server Management Studio, Click the Query tab and select SQLCMD Mode (its near the bottom) and send it!\n")
    output.write("--You're welcome...")

print('DONE!')

input()

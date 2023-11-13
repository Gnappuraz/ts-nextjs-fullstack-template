import os

project_name = '{{ cookiecutter.project_name }}'

os.system(f'''npm create t3-app@latest {project_name}''')
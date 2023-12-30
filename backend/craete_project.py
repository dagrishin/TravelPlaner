import os
from pathlib import Path

PROJECT_NAME = 'travel_planner'

# Директории
directories = [
    'src',
    'src/auth',
    'src/trips',
    'src/optimization',
    'tests',
    'tests/auth',
    'tests/trips',
]

# Файлы в корне проекта
root_files = [
    '.env',
    '.gitignore',
    'alembic.ini',
    'main.py',
]

# Файлы конфигурации
configs = [
    'src/config.py',
    'src/database.py',
]

# Пустые файлы в директориях
empty_init_files = [
    'src/__init__.py',

    'tests/__init__.py',
    'tests/auth/__init__.py',
    'tests/trips/__init__.py',

    'src/auth/__init__.py',
    'src/auth/routers.py',
    'src/auth/schemas.py',
    'src/auth/dependencies.py',
    'src/auth/utils.py',

    'src/trips/__init__.py',
    'src/trips/routers.py',
    'src/trips/schemas.py ',
    'src/trips/models.py',
    'src/trips/services.py',
    'src/trips/utils.py',

    'src/optimization/__init__.py',
    'src/optimization/services.py',
]
files = root_files + configs + empty_init_files
def create_dir(dir):
    os.makedirs(dir, exist_ok=True)
    Path(f'{dir}/__init__.py').touch()

def create_file(file):
    Path(file).touch()

if __name__ == '__main__':
    os.mkdir(PROJECT_NAME)
    os.chdir(PROJECT_NAME)

    for dir in directories:
        create_dir(dir)

    for file in files:
        create_file(file)
    print('Project structure created!')
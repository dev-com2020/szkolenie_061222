import shutil
from pathlib import Path

base_path = Path('example')
if base_path.exists() and base_path.is_dir():
    shutil.rmtree(base_path)

base_path.mkdir()
path_b = base_path / 'A' / 'B'
path_c = base_path / 'A' / 'C'
path_b.mkdir(parents=True)
path_c.mkdir()
shutil.move(path_c, path_b)

for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(path_b / filename, 'w') as stream:
        stream.write(f'Coś zapisujemy do plików, w pliku {filename}')

ex1 = path_b / 'ex1.txt'
ex1.rename(ex1.parent / 'ex1renamed.log')
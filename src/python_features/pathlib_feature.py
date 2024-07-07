#  pathlib - удобный пакет стандартной библиотеки python для простой работы с файловыми путями.

from pathlib import Path

home_dir = Path.home()
print(home_dir)

script_dir1 = home_dir / 'scripts'
script_dir2 = home_dir / 'my_file.py'

print(script_dir1, script_dir2)
print(script_dir1.name, script_dir2.name)
print(script_dir1.exists(), script_dir2.exists())
print(script_dir1.is_dir(), script_dir2.is_dir())
print(script_dir1.is_file(), script_dir2.is_file())
print(script_dir1.is_symlink(), script_dir2.is_symlink())
print(script_dir1.is_mount(), script_dir2.is_mount())

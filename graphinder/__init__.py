# pylint: skip-file

from datetime import date

__version__ = '1.0.30'

print(
    r"""
    ____                 _     _           _           
   / ___|_ __ __ _ _ __ | |__ (_)_ __   __| | ___ _ __ 
  | |  _| '__/ _` | '_ \| '_ \| | '_ \ / _` |/ _ \ '__|
  | |_| | | | (_| | |_) | | | | | | | | (_| |  __/ |   
   \____|_|  \__,_| .__/|_| |_|_|_| |_|\__,_|\___|_|   
                  |_|                                  

"""
)

print('    Maintainer   https://escape.tech')
print('    Blog         https://blog.escape.tech')
print('    DockerHub    https://hub.docker.com/r/escapetech/graphinder')
print('    Contribute   https://github.com/Escape-Technologies/graphinder')
print('')
print(f'   (c) 2021 - { date.today().year } Escape Technologies - Version: {__version__}')
print('\n' * 2)

from graphinder.main import main  # noqa

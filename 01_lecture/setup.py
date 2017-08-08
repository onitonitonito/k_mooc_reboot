from cx_Freeze import setup, Executable

setup(
    name = 'program name',
    version = '1.0',
    description = '..file description...',
    author = '!Kay SuparX!',
    executables = [Executable('02-7_class_OOP_drill.py')])

""" Execute on CMD -->  python setup.py build """    

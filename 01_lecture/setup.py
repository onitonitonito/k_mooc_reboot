from cx_Freeze import setup, Executable

F_NAME = '02-7_class_OOP_drill.py'

setup(
        name = 'program name',
        version = '1.0',
        description = '..This si file description...',
        author = '!OnitonitonitO!',
        executables = [Executable(F_NAME)])

""" Execute on CMD -->  python setup.py build """

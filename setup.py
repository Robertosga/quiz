import cx_Freeze

executables = [cx_Freeze.Executable('jogo.py')]

cx_Freeze.setup(
     name='quiz',
     options= {'build_exe':{'packages': ['pygame'],
                       'include_files':['imagens','som']}},
     executables = executables
) 
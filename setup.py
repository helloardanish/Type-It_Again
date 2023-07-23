from cx_Freeze import setup, Executable

#exe = Executable(script='Main.py',icon='icon.ico')
exe = Executable(script='Main.py')

setup(
    name="Type It Again",
    version="1.0",
    description="A software to type same thing again and again wherever you want.",
    executables=[exe]
)

'''

For macOS

python3 setup.py bdist_mac

python3 setup.py build > also


For Windows

python3 setup.py bdist_msi

'''
from cx_Freeze import setup, Executable

base = None


executables = [Executable("deletecopies.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Delete File Copies",
    options = options,
    version = "1.0",
    description = 'Deletes file copies based on Windows naming convention',
    executables = executables
)

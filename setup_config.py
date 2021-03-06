import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

build_options = {"include_msvcr":True, "includes" : [ "re", "atexit"], "packages": ["PyQt4.QtCore", "PyQt4.QtGui"]}
#build_options = {"packages": ["os"], "excludes": ["tkinter"]}

setup(  name = "Q3 Config util",
        version = "0.1",
        description = "Q3 config util",
        options = {"build_exe" : build_options},
        executables = [Executable("q3fixitconfig.py", base=base)])

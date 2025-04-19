from distutils.core import setup
import py2exe

setup(
    console=[{
        'script': 'main.py',  # The name of your script
        'dest_base': 'weather'  # This sets the name of the executable to weather.exe
    }]
)

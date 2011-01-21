#!/usr/bin/env python3

from distutils.core import setup
import os, shutil

# Build UI code
os.system('make')
shutil.copyfile('priscasms.py', 'priscasms/priscasms')

setup(name='PriscaSMS',
        version="0.01",
        description="QT GUI to send SMS using gammu",
        author="Tobias Quinn",
        author_email="tobias@tobiasquinn.com",
        url="http://tobiasquinn.com/code/priscasms.html",
        packages=['priscasms', 'priscasms.ui'],
        scripts=['priscasms/priscasms']
        data_files=[('share/applications', ['priscasms.desktop'])]
        )

# Cleanup
os.system('make clean')
os.remove('priscasms/priscasms')


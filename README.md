# Gas Blender

## Introduction

We are 6 students on Blekinge Tekniska Högskola currently going the Project in Systemtechnic course an part of this course was to solve an actual problem or request. For this request we were tasked with building an app for gas blending and you will find all all our files here.

## Architecture Overview

In the backend folder we have all the python files used for the backend of the app.
In the kv folder we have all the kivy files used for the frontend of the app.
In the pic folder we have all the pictures used by the kv folder in the frontend of the app.
In the test folder we have python code for unittests and just regular tests for the different parts of the app.
Outside the folders we have the programs that will tie it all together.

## How to Use

1. Download the folder of the "builds" branch linked here: https://github.com/Skymtes/Systemteknik/tree/builds
2. Open the file and locate the main.exe in the main folder and run that file.
3. Done.

### Requirements

Install Python dependencies: `pip3 install -r requirements.txt`
or install the dependencies manually with `pip install kivy`

### Build

To build an executable build for Windows do the following:

Download the project of the "main" branch linked here: https://github.com/Skymtes/Systemteknik (and put it in a map you can easily locate for easier use)
With the help of PIP install kivy dependencies using the pip install requirements.txt command in the terminal to be able to run the program.
Then do pip install pyinstaller (which is a module that allows you to create an executable for windows)
locate the map in the terminal using the cd command
Use the command "pyinstaller main.py -w (this creates a spec file, which we have to change in the next step)
Open up the "main.spec" file and paste this in:
@@ -1,54 +0,0 @@
from kivy_deps import sdl2, glew

-- mode: python ; coding: utf-8 --
block_cipher = None

a = Analysis(['main.py'],
pathex=[],
binaries=[],
datas=[],
hiddenimports=[],
hookspath=[],
hooksconfig={},
runtime_hooks=[],
excludes=[],
win_no_prefer_redirects=False,
win_private_assemblies=False,
cipher=block_cipher,
noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
cipher=block_cipher)

a.datas += [('Code\main.kv',
'C:\Uppgifter\Systemteknik\main.kv',
'DATA')]

exe = EXE(pyz,
a.scripts,
[],
exclude_binaries=True,
name='main',
debug=False,
bootloader_ignore_signals=False,
strip=False,
upx=True,
console=False,
disable_windowed_traceback=False,
target_arch=None,
codesign_identity=None,
entitlements_file=None )
coll = COLLECT(exe,
Tree('C:\Uppgifter\Systemteknik\'),
a.binaries,
a.zipfiles,
a.datas,
*[Tree(p) for p in
(sdl2.dep_bins +
glew.dep_bins)],
strip=False,
upx=True,
upx_exclude=[],
name='main')

You will also have to edit the Tree() with your own filepath, as well as a.datas with your the updated filepath on your PC
Use "pyinstaller main.spec -y" to create the executable file in the dist folder.
You are now done, to run the file find "main.exe" in the dist folder.

To "come close" to creating an application for Android do the following.

You have to be on Linux or macOS, I would recommend using Git Bash, but as it has technically nothing to do with building the app for Android i will link it here: https://gitforwindows.org/
Open Git Bash
Make sure you have python
Download the project of the "main" branch linked here: https://github.com/Skymtes/Systemteknik
With the help of PIP install kivy dependencies using the pip install requirements.txt command in the terminal to be able to run the program.
git clone https://github.com/kivy/buildozer.git
cd buildozer
sudo python setup.py install
Now, locate the map where the project you downloaded is located with the help of cd.
buildozer init (creates buildozer.spec file)
Plug in the android advice into the computer
buildozer android debug deploy run (will hopefully start the application on your device)

### Test

Download the files and run the db_test.py file in the test folder to run tests for the database.
Download the files and run the test_belnding.py file in the test folder to run tests for the beldningg algorithm.
Do `python3 -m unittest discover` to run all the tests.

## License

All content belongs to the developers.
TODO: Add license and copyright notice.

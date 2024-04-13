from setuptools import setup
APP = ['sarcasticizer.py']
DATA_FILES = []
OPTIONS = {
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps','pyperclip']
}
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
# python setup.py py2app
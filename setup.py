import pathlib
from setuptools import setup

__version__ = '1.0'
__author__ = 'Jeff Barfield'
__author_email__ = 'noprobelm@protonmail.com'

HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()

setup(
    name='pwea',
    version=__version__,
    description='A simple tool for displaying weather data in the command line.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/noprobelm/pwea',
    author=__author__,
    author_email=__author_email__,
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['pwea'],
    include_package_data=True,
    install_requires=['requests', 'rich', 'argparse'],
    entry_points={'console_scripts': ['pwea=pwea.__main__:main']},
    python_requires=">=3.6"
)

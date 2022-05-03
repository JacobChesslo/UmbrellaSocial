"""UmbrellaSocial: Social Media Site Clone Project

Created alongside Jose Portilla's course:
    https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/
"""

from pathlib import Path
from setuptools import find_packages, setup

# Metadata for project
__encoding__ = ENCODING = 'utf-8'
this_directory = Path.cwd()
project_directory = Path(__file__).absolute().parent
NAME = 'UmbrellaSocial'
MAJOR = 0
MINOR = 1
MICRO = 0
BUG = 0
__version__ = VERSION = '{}.{}.{}'.format(MAJOR, MINOR, MICRO)
DESCRIPTION = (__doc__ or '')
try:
    with open(project_directory / 'README.md', 'r', encoding=__encoding__) as file:
        LONG_DESCRIPTION = file.read()
except FileNotFoundError:
    LONG_DESCRIPTION = DESCRIPTION

# Credits
LICENSE = __license__ = None
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Other Audience',
    'Natural Language :: English',
    'Operating System :: Unix',
    'Programming Language :: Python :: 3',
    'Topic :: Internet',
]

AUTHOR = 'Jacob Chesslo'
AUTHOR_EMAIL = 'jacobchesslo@gmail.com'
URL = DOWNLOAD_URL = 'www.github.com/jacobchesslo/UmbrellaSocial'

# Requirements
REQUIRES_PYTHON = '>=3.6.5'
try:
    with open(project_directory / 'requirements.txt', 'r', encoding=__encoding__) as file:
        REQUIRED = file.readlines()
except FileNotFoundError:
    REQUIRED = ['django', 'misaka', 'django-braces']


def setup_umbrella_social():
    setup(
        name=NAME,
        version=__version__,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        python_requires=REQUIRES_PYTHON,
        url=URL,
        download_url=DOWNLOAD_URL,
        packages=find_packages(exclude=['tests', '*.tests', '*.tests.*', 'tests.*']),
        install_requires=REQUIRED,
        install_package_data=True,
        license=LICENSE,
        classifiers=CLASSIFIERS,
    )


if __name__ == '__main__':
    setup_umbrella_social()

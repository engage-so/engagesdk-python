import pathlib
from setuptools import setup, find_packages
from engagesdk.version import __version__

DESCRIPTION = 'Engage python SDK'

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README.md file
README = (HERE / "README.md").read_text()

# Setting up
setup(
        name="engagesdk", 
        version=__version__,
        author="Francis Onyishi",
        author_email="francis@engage.so",
        description=DESCRIPTION,
        long_description=README,
        long_description_content_type="text/markdown",
        packages=find_packages(exclude=['test']),
        install_requires=['requests'],
        
        keywords=['engagesdk', 'engage python'],
        classifiers= [
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            'License :: OSI Approved :: MIT License',

            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
        ]
)
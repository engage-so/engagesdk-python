from setuptools import setup, find_packages
from engagesdk.version import __version__

DESCRIPTION = 'Engage python SDK'
LONG_DESCRIPTION = 'Engage SDK to capture and send user attributes and events to Engage'

# Setting up
setup(
        name="engagesdk", 
        version=__version__,
        author="Francis Onyishi",
        author_email="francis@engage.so",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
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
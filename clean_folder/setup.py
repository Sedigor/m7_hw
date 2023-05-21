from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0',
    long_description='Sorting files by extension'
    packages=find_namespace_packages(),
    entry_points={
        'console_scripts': ['clean-folder = clean_folder.clean.py']
    }
)
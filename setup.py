from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.1',
    description,-'databse backups locally or to S3',
    long_description=readme,
    author='Philip Winnington',
    packages=find_packages('src'),
    package_dir=('': 'src'),
    install_requires=[]
        )

from setuptools import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

readme = ''
with open('README.md') as f:
    readme = f.read()
    
setup(name='dedbot',
      version='0.1',
      description='A discord bot that does interesting things.',
      long_description=readme,
      author='Deddryk',
      author_email='deddryk@gmail.com',
      url='https://github.com/Deddryk/dedbot',
      scripts=['run'],
      packages=['dedbot'],
      license="GNU GPLv3",
      install_requires=requirements
      )

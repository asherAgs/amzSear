from setuptools import setup, find_packages
setup(
  name = 'amzsear',
  packages = find_packages(),
  version = '1.9.16',
  description = 'The unofficial Amazon search CLI & Python API',
  author = "Asher Silvers",
  author_email = "ashersilvers@gmail.com",
  license='MIT',
  url = 'https://github.com/asherAgs/amzSear_staging', 
  keywords = 'amazon search product products python',
  classifiers = [],
  entry_points={
    'console_scripts': [
      'amzsear = amzsear.cli.cli:run',
     ],
  },
)

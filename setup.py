from distutils.core import setup
setup(
  name = 'amzsear',
  packages = ['amzsear'], 
  version = '1.0.5',
  description = 'The unofficial Amazon search CLI & Python API',
  author = "Asher Silvers",
  author_email = "ashersilvers@gmail.com",
  license='MIT',
  url = 'https://github.com/asherAgs/amzSear', 
  keywords = 'amazon search product products python',
  classifiers = [],
  entry_points={
    'console_scripts': [
      'amzsear = amzsear.cli:run',
     ],
  },
  install_requires = ['lxml==3.8.0','requests==2.18.1'],

)

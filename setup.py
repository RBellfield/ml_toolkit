from setuptools import setup, find_packages

setup(name='ml_toolkit',
      version='0.0.1',
      description='A toolkit to store functions to carry out standard machine learning (ML) tasks to simplify the approach',
      # long_description=open('README.rst').read(),
      url='https://github.com/RBellfield/ml_toolkit',
      author='Ryan AA Bellfield',
      author_email='r.a.bellfield@ljmu.ac.uk',
      # license='MIT',
      packages=find_packages(),
      install_requires=['numpy>=1.14.5', 'scikit-learn>=0.20.0',
                        'matplotlib>=2.2.2', 'scipy>=0.19.1']
      )

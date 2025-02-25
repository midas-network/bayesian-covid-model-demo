from setuptools import find_packages, setup

setup(
    name='covid',
    version="0.0.1",
    description='Bayesian COVID-19 models',
    packages=find_packages(include=['covid', 'covid.*']),
    url='https://github.com/dsheldon/covid-19',
    author='Dan Sheldon',
    author_email='sheldon@cs.umass.edu',
    install_requires=[
        'patsy>=0.5.1',
        'numpyro==0.6.0',
        'jax>=0.2.3',
	'pandas==1.1.5',
	'cachetools',
	'matplotlib==3.3.4'
    ],
    keywords='machine learning bayesian statistics',
    license='MIT'
)

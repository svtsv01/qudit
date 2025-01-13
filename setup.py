from setuptools import setup, find_packages

setup(
    name='qudit',
    version='0.1.0',
    author='Svyatoslav Kushnarev, Hassan Asghar',
    author_email='',
    description='This library extends Cirq framework to support **qudits**.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/svtsv01/qudit.git',  
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
     install_requires=[
        'cirq>=0.14',      
        'numpy>=1.21',     
        'sympy>=1.7.1',  
     ],
)

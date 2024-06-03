from setuptools import setup, find_packages

setup(
    name='six_sigma_project',
    version='1.0.0',
    description='A project for calculating Six Sigma quality indices from SQL Server data',
    author='Tu Nombre',
    author_email='tu.email@example.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'pyodbc',
    ],
    entry_points={
        'console_scripts': [
            'six_sigma=six_sigma_project.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

from setuptools import setup, find_packages

setup(
    name='isrmltoolkit',
    version='0.1.5',
    packages=find_packages(),  # <--- Esto encuentra automáticamente isrmltoolkit/
    install_requires=[
        'pandas',
        'matplotlib',
        'seaborn',
        'scikit-learn'
    ],
    author='Isra',
    author_email='ismael@email.com',
    description='Funciones y utilidades útiles para proyectos de Machine Learning',
    url='https://github.com/Israelamat/pip_install',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
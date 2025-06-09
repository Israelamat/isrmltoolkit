from setuptools import setup, find_packages

setup(
    name='isrmltoolkit',  # Nombre que usará pip install
    version='0.1.5', 
    author='Isra',
    author_email='ismael@email.com',
    description='Funciones y utilidades útiles para proyectos de Machine Learning',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Israelamat/pip_install',  # Actualízalo si es necesario
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)

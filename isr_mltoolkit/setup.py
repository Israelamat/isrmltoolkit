from setuptools import setup, find_packages

setup(
    name='isr_mltookit',  # Nombre que usará pip install
    version='0.1.0',
    author='Isra',
    author_email='ismael@email.com',
    description='Funciones y utilidades útiles para proyectos de Machine Learning',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tuusuario/isr-mltookit',  # Pon la URL de tu repo o elimínala si no tienes
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

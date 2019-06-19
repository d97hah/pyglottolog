from setuptools import setup, find_packages


setup(
    name='pyglottolog',
    version='2.0.1.dev0',
    author='Robert Forkel',
    author_email='forkel@shh.mpg.de',
    description='python package for glottolog data curation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='data linguistics',
    license='Apache 2.0',
    url='https://github.com/clld/pyglottolog',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    platforms='any',
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['glottolog=pyglottolog.__main__:main'],
    },
    install_requires=[
        'six>=1.9',
        'csvw',
        'clldutils>=2.8.0',
        'purl',
        'pycldf>=1.6.4',
        'sqlalchemy',
        'tqdm',
        'pybtex>=0.22',
        'latexcodec',
        'unidecode',
        'whoosh',
        'attrs>=18.1',
        'pycountry>=18.12.8',
        'termcolor',
        'newick',
        'markdown',
        'bs4',
        'requests',
        'nameparser',
    ],
    extras_require={
        'dev': ['tox>=2.9', 'flake8', 'pep8-naming', 'wheel', 'twine'],
        'test': ['mock>=2', 'pytest>=3.6', 'pytest-mock', 'pytest-cov'],
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

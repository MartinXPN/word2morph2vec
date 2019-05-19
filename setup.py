from setuptools import find_packages, setup


setup(
    name='word2morph2vec',
    version='1.0.0',
    description='End to end pipeline for extracting morphological vectors from a given word',
    author='Martin Mirakyan',
    author_email='mirakyanmartin@gmail.com',
    python_requires='>=3.6.0',
    url='https://github.com/MartinXPN/word2morph2vec',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'nltk>=3.4',
        'sentence2tags @ git+https://www.github.com/MartinXPN/sentence2tags@master',
        'word2morph @ git+https://www.github.com/MartinXPN/word2morph@master',
        'morph2vec @ git+https://www.github.com/MartinXPN/morph2vec@master',
    ],
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Full list of Trove classifiers: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)

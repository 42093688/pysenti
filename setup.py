# -*- coding: utf-8 -*-
"""
@author:XuMing（xuming624@qq.com)
@description:
"""
from __future__ import print_function

import sys

from setuptools import setup, find_packages

from sentiment_classifier import __version__

if sys.version_info < (3,):
    sys.exit('Sorry, Python3 is required for sentiment_classifier_zh.')

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE', 'r', encoding='utf-8') as f:
    license = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f:
    reqs = f.read()

setup(
    name='sentiment_classifier_zh',
    version=__version__,
    description='Chinese Sentiment Classification',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='XuMing',
    author_email='xuming624@qq.com',
    url='https://github.com/shibing624/sentiment-classifier-zh',
    license="Apache 2.0",
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='NLP,sentiment-classifier,sentiment-classification',
    install_requires=reqs.strip().split('\n'),
    packages=find_packages(exclude=['tests']),
    package_dir={'sentiment_classifier': 'sentiment_classifier'},
    package_data={
        'sentiment_classifier': ['*.*', '../LICENSE', '../README.*', '../*.txt', 'data/*'],
    },
    test_suite='tests',
)
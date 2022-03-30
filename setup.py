#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'neon-tokenization-plugin-nltk=neon_tokenization_plugin_nltk:NltkTokenizer'

setup(
    name='neon-tokenization-plugin-nltk',
    version='0.0.1',
    description='A word tokenization plugin for mycroft',
    url='https://github.com/NeonGeckoCom/neon-tokenization-plugin-nltk',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['neon_tokenization_plugin_nltk'],
    install_requires=["ovos-plugin-manager", "nltk"],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'intentbox.tokenization': PLUGIN_ENTRY_POINT
    }
)

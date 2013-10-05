#! /usr/bin/env python

from setuptools import setup

setup(
    name = 'pygments-gcc',
    version = '0.1',
    py_modules = ['pygments_gcc'],

    install_requires = ['pygments'],

    entry_points = {
        'pygments.lexers': 'gcclexer = pygments_gcc:GCCLexer',
    },

    author = 'Pierre-Marie de Rodat',
    author_email = 'pmderodat@kawie.fr',
    description = 'Pygments lexer for GCC\'s internal trees',
    keywords = 'pygments gcc',
)

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# import version of PyGCGOpt
from pygcgopt import __version__


# -- Project information -----------------------------------------------------

project = 'PyGCGOpt'
copyright = '2021, Operations Research, RWTH Aachen University'
author = 'Operations Research, RWTH Aachen University'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_copybutton', # for copybuttons
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    'myst_parser', # for markdown in docs
    'nbsphinx', # for jupyter notebooks
    'sphinx.ext.githubpages', # for githubpages
]

# allow also markdown files and jupyter notebooks
source_suffix = ['.rst', '.md']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Changing sidebar title
html_title = 'PyGCGOpt' + ' ' + __version__

# set favicon path
html_favicon = '_static/favicon.ico'

# set logo path
#html_logo = '_static/rwth_operations_research_rgb.png'

myst_enable_extensions = [
    "amsmath" #latex extensions
]
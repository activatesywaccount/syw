# Configuration file for the Sphinx documentation builder.
# This file only contains a selection of the most common options.
# For a full list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example:
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Syw.accountonline.com Login – activate.syw.account'
copyright = '2025, Syw.accountonline.com'
author = 'Syw.accountonline.com Help Center'

# Full version (release)
release = '1.0.0'

# Favicon path
html_favicon = 'favicon.ico'

# -- General configuration ---------------------------------------------------

# Add Sphinx extension modules here if needed:
# extensions = []

# Template paths
# templates_path = ['_templates']

# Ignore patterns for source files
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme for HTML pages
# html_theme = 'sphinx_rtd_theme'

# Custom static files path (CSS, JS)
# html_static_path = ['_static']

# Hide "View page source"
html_show_sourcelink = False

# Theme Options
html_theme_options = {
    'show_powered_by': False,
}


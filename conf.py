# Configuration file for the Sphinx documentation builder.
# For full options, see:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Path setup --------------------------------------------------------------

# If your modules are in another directory, add them to sys.path here.
# Example:
# sys.path.insert(0, os.path.abspath('../src'))


# -- Project information -----------------------------------------------------

project = 'Syw.accountonline.com Login – activate.syw.account'
copyright = '2025, Syw.accountonline.com'
author = 'Syw.accountonline.com Help Center'

# Version
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Sphinx extensions (add more later if needed)
extensions = [
    # 'sphinx.ext.autodoc',
    # 'sphinx.ext.napoleon',
    # 'sphinx.ext.todo',
    # 'sphinx.ext.githubpages',
    # 'sphinx.ext.autosectionlabel'
]

# Paths containing templates
templates_path = ['_templates']

# Source file exclusions
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# Theme
html_theme = 'sphinx_rtd_theme'

# Static files (CSS, JS)
html_static_path = ['_static']

# Favicon
html_favicon = 'favicon.ico'

# Hide “View page source”
html_show_sourcelink = False

# Theme options
html_theme_options = {
    'show_powered_by': False,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'style_external_links': True,
    # 'logo_only': True,   # Enable if you add a logo
}

# Optional sidebar customization (uncomment if needed)
# html_sidebars = {
#     '**': [
#         'globaltoc.html',
#         'relations.html',
#         'sourcelink.html',
#         'searchbox.html'
#     ]
# }


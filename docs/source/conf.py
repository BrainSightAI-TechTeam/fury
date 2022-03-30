#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FURY documentation build configuration file, created by
# sphinx-quickstart on Thu Jun 28 12:35:56 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
import sys
from datetime import datetime
# Add current path
sys.path.insert(0, os.path.abspath('.'))
# Add doc in path for finding tutorial and examples
sys.path.insert(0, os.path.abspath('../..'))
# Add custom extensions
sys.path.insert(0, os.path.abspath('./ext'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = '2.1'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    'matplotlib.sphinxext.plot_directive',
    'sphinx_copybutton',
    'sphinx_gallery.gen_gallery',
    'ext.build_modref_templates',
    'ext.github',
    'ext.github_tools',
    'ext.rstjinja',
    'ablog',
]

# Configuration options for plot_directive. See:
# https://github.com/matplotlib/matplotlib/blob/f3ed922d935751e08494e5fb5311d3050a3b637b/lib/matplotlib/sphinxext/plot_directive.py#L81
plot_html_show_source_link = False
plot_html_show_formats = False

# Generate the API documentation when building
autosummary_generate = []
numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
import ablog
templates_path = ['_templates', ablog.get_html_templates_path(), ]


# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'FURY'
copyright = '2018-{0}, FURY'.format(datetime.now().year)
author = 'FURY'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
import fury
# The short X.Y version.
version = fury.__version__
# The full version, including alpha/beta/rc tags.
release = fury.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_material'
# # Material theme options (see theme.conf for more information)
# html_theme_options = {

#     # Set the name of the project to appear in the navigation.
#     'nav_title': 'FURY',

#     # Set you GA account ID to enable tracking
#     'google_analytics_account': 'UA-XXXXX',

#     # Specify a base_url used to generate sitemap.xml. If not
#     # specified, then no sitemap will be built.
#     'base_url': 'https://fury.gl/latest',

#     # Set the color and the accent color
#     'theme_color': '#990000',
#     'color_primary': 'red',
#     'color_accent': 'red',

#     # Set the repo location to get a badge with stats
#     'repo_url': 'https://github.com/fury-gl/fury/',
#     'repo_name': 'fury',

#     # Visible levels of the global TOC; -1 means unlimited
#     'globaltoc_depth': 2,
#     # If False, expand all TOC entries
#     'globaltoc_collapse': True,
#     # If True, show hidden TOC entries
#     'globaltoc_includehidden': True,
#     # 'master_doc': False,
#     "version_dropdown": True,
#     "version_json": "_static/versions.json",
# }
import pydata_sphinx_theme
html_theme = 'pydata_sphinx_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_theme_options = {
  "navigation_depth": 1,
  "logo_link": 'index.html',
  "navbar_start": ["custom-title.html"],
  "navbar_center": '',
  "navbar_end": 'custom-navbar.html',

}

html_additional_pages = {
    'video': 'home-video-page.html',
    'index': 'home.html'
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

# html_baseurl = os.environ.get("SPHINX_HTML_BASE_URL", "http://127.0.0.1:8000/")

html_logo = '_static/images/logo.svg'

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
# html_sidebars = {
#     '**': [
#         'relations.html',  # needs 'show_related': True theme option to display
#         'searchbox.html',
#         'versions.html',
#     ]
# }
html_sidebars = {
    # "**": ["search-field", 'globaltoc.html',"sidebar-nav-bs"]
    "**": ["search-field", 'globaltoc.html']
}
# html_sidebars = {
#     "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"],
# }
# html_sidebars = {
#     "introduction/**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"],
#     "getting_started": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"],
#     "auto_examples/**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"],
#     "auto_tutorials/**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"],
#     "references/**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"],
#     "blog": ["categories.html", "archives.html"],
#     "blog/**": ["categories.html", "archives.html"],
#     "posts/**": ["postcard.html"],
# }

# ghissue config
github_project_url = "https://github.com/fury-gl/fury"

import github_tools as ght
all_versions = ght.get_all_versions(ignore='micro')
html_context = {'all_versions': all_versions,
                'versions_list': ['dev', 'latest'] + all_versions,
                'basic_stats': ght.fetch_basic_stats(),
                'contributors': ght.fetch_contributor_stats(),
                }

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'fury'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'fury.tex', 'FURY Documentation',
     'Contributors', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'fury', 'FURY Documentation',
     [author], 1)
]

# -- Options for sphinx gallery -------------------------------------------
from scrap import ImageFileScraper

sc = ImageFileScraper()

sphinx_gallery_conf = {
     'doc_module': ('fury',),
     # path to your examples scripts
     'examples_dirs': ['../examples', '../tutorials'],
     # path where to save gallery generated examples
     'gallery_dirs': ['auto_examples', 'auto_tutorials'],
     'image_scrapers': (sc),
     'backreferences_dir': 'api',
     'reference_url': {'fury': None, },
     'filename_pattern': re.escape(os.sep)
}

# -- Options for Blog -------------------------------------------

blog_baseurl = "https://fury.gl/"
blog_feed_fulltext = True
blog_feed_length = 10
blog_feed_archives = True
blog_authors = {
    'skoudoro': ('Serge Koudoro', 'https://github.com/skoudoro'),
}

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'fury', 'FURY Documentation',
     author, 'fury', 'Free Unified Rendering in Python',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable', None),
    'matplotlib': ('https://matplotlib.org', None),
    'dipy': ('https://dipy.org/documentation/latest',
             'https://dipy.org/documentation/latest/objects.inv/'),
}

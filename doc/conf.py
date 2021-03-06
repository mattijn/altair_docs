# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Altair"
copyright = "2021, Altair Community"
author = "Altair Community"

# The full version, including alpha/beta/rc tags
release = "0.0.1dev0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "myst_nb",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "numpydoc",
    "jupyter_sphinx",
]

autosummary_generate = True

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_sidebars = {
    "releases/index": [],
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_logo = "_static/altair-logo-light.png"
html_favicon = "_static/favicon.ico"

html_theme_options = {
    "github_url": "https://github.com/altair-viz/altair",
    "use_edit_page_button": True,
    "show_toc_level": 1,
    # "navbar_align": "right",  # For testing that the navbar items align properly
}

html_context = {
    "github_user": "altair-viz",
    "github_repo": "altair",
    "github_version": "master",
    "doc_path": "doc",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Auto-convert markdown pages to demo --------------------------------------
from recommonmark.transform import AutoStructify


def setup(app):
    app.add_transform(AutoStructify)

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

sys.path.insert(0, os.path.abspath("../../src"))


# -- Project information -----------------------------------------------------

project = "shamo"
copyright = "2020-2021, GIGA CRC In-Vivo Imaging"
author = "Martin Grignard <mar.grignard@uliege.be>"

# The full version, including alpha/beta/rc tags
release = "1.1.0"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    "numpydoc",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "nbsphinx",
    "sphinxcontrib.bibtex",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = [".templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["test"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -- Option for intersphinx --------------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "matplotlib": ("https://matplotlib.org", None),
    "chaospy": ("https://chaospy.readthedocs.io/en/master", None),
}

# -- Options for numpydoc ----------------------------------------------------
numpydoc_use_plots = True
numpydoc_show_class_members = False
numpydoc_attributes_as_param_list = False
numpydoc_xref_param_type = True

# -- Options for read the docs theme -----------------------------------------
html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes"]
html_theme_options = {"collapse_navigation": False}

# -- Options for autosummary -------------------------------------------------
autosummary_generate = True
autoclass_content = "both"
autodoc_inherit_docstrings = True

# -- Options for bibtex ------------------------------------------------------
bibtex_bibfiles = ["references.bib"]

# -- Options for nbsphinx ----------------------------------------------------
nbsphinx_allow_errors = True
nbsphinx_execute = "never"

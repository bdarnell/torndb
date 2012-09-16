# Ensure we get the local copy of torndb instead of what's on the standard path
import os
import sys
sys.path.insert(0, os.path.abspath(".."))
import torndb

master_doc = "index"

project = "Torndb"
copyright = "2011, Facebook"

version = release = torndb.version

extensions = ["sphinx.ext.autodoc", "sphinx.ext.coverage", "sphinx.ext.viewcode"]

primary_domain = 'py'
default_role = 'py:obj'

autodoc_member_order = "bysource"
autoclass_content = "both"

coverage_skip_undoc_in_source = True

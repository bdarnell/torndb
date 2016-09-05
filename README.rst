Torndb
======

Unmaintained
------------

This package is not actively maintained, and since it exists primarily
for backwards compatibility with the module provided in Tornado prior
to version 3.0, I do not intend to make major changes or merge pull
requests that do so.  New projects are encouraged to choose a different
database package. Anyone interested in producing an updated version of
`torndb` is welcome to create a fork (under a new name)

Description
-----------

Torndb is a simple wrapper around `MySQLdb` that originally appeared
in Tornado (http://www.tornadoweb.org).  It is being moved into
a separate package for Tornado 3.0.

Limitations
-----------

Torndb does not support Python 3, or any database drivers other than
`MySQLdb` or `pymysql`.

Installation
------------

``pip install torndb``

Documentation
-------------

http://torndb.readthedocs.org

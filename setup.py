#!/usr/bin/env python
#
# Copyright 2012 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import distutils.core

version = "0.2"

distutils.core.setup(
    name="torndb",
    version=version,
    py_modules=["torndb"],
    author="Facebook",
    author_email="python-tornado@googlegroups.com",
    url="https://github.com/bdarnell/torndb",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    description="A lightweight wrapper around MySQLdb.  Originally part of the Tornado framework.",
    )

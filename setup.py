# This file is part of Python-Bijection.
# Copyright 2016 Binary Birch Tree
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import codecs
import os.path
import setuptools

readme_path = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'README.rst'
)

with codecs.open(readme_path, encoding='utf-8') as readme:
    long_description = readme.read()

setuptools.setup(
    name='bijection',
    version='0.1.1',
    description='A library for producing bijective functions in Python.',
    long_description=long_description,
    url='https://github.com/binarybirchtree/python-bijection',
    author='Binary Birch Tree',
    author_email='binarybirchtree@users.noreply.github.com',
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
    ],
    keywords='bijection bijective function',
    py_modules=['bijection'],
    install_requires=['pycryptodome'],
)

"""
* Cython Simple Example by Time to Share
* site: http://mataeoh.egloos.com/7066025
"""

from distutils.core import setup
from Cython.Build import cythonize

FNAME="_hello_cpython.pyx"
setup(ext_modules = cythonize(FNAME))

#EXC: python _hello_cpython_setup.py build_ext --inplace

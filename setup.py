#!/usr/bin/env python
# Use python setup.py build --debug to build
# python setup.py clean --all to clean

from distutils.core import setup, Extension
from os import environ

# LIB_CLANG=$(llvm-config --libdir)
clanglib = "%s" % environ['LIB_CLANG']

# SRC_CLANG=$(llvm-config --src-root)/tools/clang
clanginc = "%s/include" % environ['SRC_CLANG']

libclangmodule = Extension('libclang',
                           sources=['cindex.c'],
                           include_dirs = [clanginc],
                           define_macros = [('_DEBUG', None),
                                            ('__STDC_LIMIT_MACROS', None),
                                            ('__STDC_CONSTANT_MACROS', None)],
                           library_dirs = [clanglib],
                           libraries = ['clang'],
                           runtime_library_dirs = [clanglib],
                           extra_compile_args = ['-O0'])

setup(name='libclang',
      ext_modules=[libclangmodule])

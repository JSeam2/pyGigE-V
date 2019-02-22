import os
import numpy as np

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from setuptools import Extension
except ImportError:
    from distutils.extension import Extension

USE_CYTHON = False

ext = '.pyx' if USE_CYTHON else '.c'

extensions = [Extension("pygigev",
                        ["pygigev" + ext],
                        language="c",
                        include_dirs=[
                            "/usr/dalsa/GigeV/include/", 
                            np.get_include()
                        ],
                        libraries=["GevApi"])]
if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)

setup(ext_modules=extensions,
      name='pygigev',
      version='1.0.1',
      description='Python wrapper for Gige-V cameras',
      url='https://github.com/JSeam2/pyGigE-V',
      py_modules=['pygigev'],
      install_requires=[
          'opencv-python',
          'numpy'
      ],
)

# from distutils.core import setup
# from distutils.extension import Extension

# USE_CYTHON = ...   # command line option, try-import, ...

# ext = '.pyx' if USE_CYTHON else '.c'

# extensions = [Extension("example", ["example"+ext])]

# if USE_CYTHON:
#     from Cython.Build import cythonize
#     extensions = cythonize(extensions)

# setup(
#     ext_modules = extensions
# )

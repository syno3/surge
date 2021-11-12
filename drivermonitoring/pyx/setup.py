from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import os
import numpy

""" mypackage_root_dir = os.path.dirname(__file__)
with open(os.path.join(mypackage_root_dir, 'requirements.txt')) as requirements_file:
    requirements = requirements_file.read().splitlines()
 """
extensions = [Extension(
    name="sleepNN",
    sources=["sleepNN.pyx"],
    include_dirs=[numpy.get_include()],
    )
]

setup(name='cython',
      version=0.1,
      description='...',
      author='festus murimi',
      ext_modules = cythonize(extensions),
)
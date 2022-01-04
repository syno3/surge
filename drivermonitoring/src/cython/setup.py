from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy

## enviroment, func, sleepNN
extensions = [Extension(
    name="sleepNN",
    sources=["sleepNN.pyx"],
    include_dirs=[numpy.get_include()],)
]

setup(name='cython',
    version=0.1,
    description='...',
    author='festus murimi',
    ext_modules = cythonize(extensions),
)
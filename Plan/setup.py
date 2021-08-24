from setuptools import setup
from Cython.Build import cythonize

setup(
    name='dense odometry',
    ext_modules=cythonize("localization.pyx"),
    zip_safe=False,
)
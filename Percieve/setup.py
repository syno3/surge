from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Lane detection computer vision',
    ext_modules=cythonize("laneDetection.pyx"),
    zip_safe=False,
)
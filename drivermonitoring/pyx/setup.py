from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize


""" ext_modules=[
    Extension("enviroment", ["enviroment.pyx"]),
    Extension("face", ["face.pyx"]),
    Extension("test", ["test.pyx"]),
]

setup(
  name = 'cythonize',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
) """

setup(
    ext_modules = cythonize("face.pyx", annotate=True)
)
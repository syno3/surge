from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension('enviroment',
                         sources=['enviroment.pyx'],
                         language='c',
                        )]
setup(
name = 'enviroment',
cmdclass = {'build_ext': build_ext},
ext_modules = ext_modules
)
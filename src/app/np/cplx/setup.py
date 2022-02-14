from distutils.core import Extension, setup

import numpy
from Cython.Build import cythonize
from Cython.Compiler import Options

# Generate an annotated HTML version of the input source files for debugging and optimisation purposes.
# This has the same effect as the annotate argument in cythonize().
Options.annotate = True

setup(
    name="app-grover",
    ext_modules=cythonize(
        [
            Extension(
                name="*",
                sources=["**/*.pyx"],
                language="c++",
                extra_compile_args=["-O3"],
            )
        ],
        # https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html#compiler-options
        compiler_directives={
            # language_level (2/3/3str)
            # Globally set the Python language level to be used for module compilation. Default is compatibility with
            # Python 2. To enable Python 3 source code semantics, set this to 3 (or 3str) at the start of a module or
            # pass the “-3” or “–3str” command line options to the compiler. The 3str option enables Python 3
            # semantics but does not change the str type and unprefixed string literals to unicode when the compiled
            # code runs in Python 2.x. Note that cimported files inherit this setting from the module being compiled,
            # unless they explicitly set their own language level. Included source files always inherit this setting.
            "language_level": 3
        },
    ),
    include_dirs=[numpy.get_include()],
)

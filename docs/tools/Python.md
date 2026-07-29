# Tools for Python programming


## Code formatting

* [Ruff formatter](https://docs.astral.sh/ruff/formatter/): fast formatter
  designed to be largely compatible with Black.  Ruff can provide both
  formatting and linting through one repository configuration.
* [Black](https://black.readthedocs.io/): established, deliberately
  opinionated code formatter.  It remains a good choice when a project already
  uses Black or requires Black's exact formatting behaviour.


## Linting and static analysis

* [Ruff](https://docs.astral.sh/ruff/linter/): fast linter that implements
  rules from Flake8 and many of its plug-ins, as well as rules for import
  sorting, modernization, and common correctness problems.  It is a convenient
  default for new projects.
* [mypy](https://mypy-lang.org/): static type checker for annotated Python
  code.  A linter such as Ruff does not replace a type checker.
* [Pylint](https://pylint.readthedocs.io/): configurable static analyzer with
  broader design, documentation, and code-quality checks.
* [Flake8](https://flake8.pycqa.org/en/latest/): established linter and plug-in
  framework.  It remains useful for projects with an existing Flake8
  configuration, although Ruff can replace it in many new projects.


## Package managers

The appropriate choice depends on whether the environment consists primarily
of Python packages or also includes compiled scientific libraries, compilers,
MPI, accelerator runtimes, and other non-Python dependencies.

* [conda](https://docs.conda.io/): cross-platform package and environment
  manager for Python and compiled packages.  Miniforge and Miniconda are
  installers that provide conda; they are not themselves package managers.
* [mamba and micromamba](https://mamba.readthedocs.io/en/stable/):
  conda-compatible package managers.  Micromamba is a small standalone
  executable that is useful in continuous integration and containers.
* [Pixi](https://pixi.prefix.dev/latest/): project and environment manager that
  can resolve conda and Python packages, record a cross-platform lockfile, and
  define project tasks.  It is a strong starting point for scientific projects
  that need compiled libraries as well as Python packages.
* [uv](https://docs.astral.sh/uv/): fast Python package and project manager
  with Python-version management and a cross-platform lockfile.  It is a good
  choice for projects whose dependencies can be managed through the Python
  package ecosystem.

  `uv` is usually **not the best default for scientific and HPC applications**
  whose reproducible environment must also manage external compiled
  libraries, MPI implementations, accelerator runtimes, compiler variants, or
  packages supplied by an HPC site.  Although Python wheels may contain
  compiled code, `uv` does not manage the complete non-Python toolchain.  For
  those applications, start with Pixi or conda/mamba for a project environment,
  or Spack for a compiler- and architecture-specific HPC software stack; `uv`
  can still be useful for a Python-only layer within such an environment.
* [Poetry](https://python-poetry.org/): project, dependency, build, and
  publishing tool for Python packages.  It is most appropriate when the
  project is centered on the Python packaging ecosystem.


## Configuration files

* [Hydra](https://hydra.cc/): configuration management tool that allows you to
  compose complex configurations from simple pieces.


## Testing

* [pytest](https://docs.pytest.org/): unit testing framework.
* [hypothesis](https://hypothesis.readthedocs.io/): property-based testing for
  Python, it also allows for fuzz testing.


## Profiling

* [cProfile](https://docs.python.org/3/library/profile.html) is a deterministic
  function-level profiler in Python's standard library.
* [snakeviz](https://jiffyclub.github.io/snakeviz/) is a viewer for cProfile
  output.
* [line_profiler](https://github.com/pyutils/line_profiler) is a line-by-line
  profiler.
* [tracemalloc](https://docs.python.org/3/library/tracemalloc.html) is a
  standard-library module for tracing memory allocated by Python.
* [Memray](https://bloomberg.github.io/memray/) is a memory profiler that
  tracks allocations in Python code and compiled extension modules.  It is a
  maintained alternative to the unmaintained `memory_profiler` package.


## Language interoperability

* [Cython](https://cython.org/): a superset of Python that allows you to write
  C extensions for Python.
* [Pybind11](https://pybind11.readthedocs.io/): a header-only library that
    exposes C++ types in Python.
* [SWIG](https://www.swig.org/): a tool that generates wrappers for exposing C
  and C++ libraries to Python and other languages.
* [scikit-build-core](https://scikit-build-core.readthedocs.io/): modern build
  backend for Python extension modules that use CMake.  The original
  scikit-build remains relevant mainly to existing projects.
* [F2PY](https://numpy.org/doc/stable/f2py/): a tool that allows you to wrap
  Fortran code for Python.
* [rpy2](https://rpy2.github.io/): a tool that allows you to run R code
  from Python.

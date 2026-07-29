# Tools for Fortran programming


## Code formatting

* [fprettify](https://fortran-lang.org/packages/fprettify/): auto-formatter for
  modern Fortran source code.


## Linting and static analysis

* [Fortitude](https://fortitude.readthedocs.io/en/stable/): linter for Fortran
  that checks correctness, modernization, portability, and style rules.  It can
  produce output suitable for continuous integration and fix some findings
  automatically.


## Testing

* [pFUnit](https://github.com/Goddard-Fortran-Ecosystem/pFUnit): unit testing
  framework for serial and MPI-parallel Fortran software, with limited OpenMP
  support.


## Profiling

* [GNU gprof](https://sourceware.org/binutils/docs/gprof/) is a basic
  instrumenting profiler distributed with GNU Binutils.  It is useful for
  introductory profiling and existing workflows, but
  [gprofng](https://sourceware.org/binutils/docs/gprofng.html) is the more
  capable profiler in current Binutils releases.
* [Intel VTune Profiler](https://www.intel.com/content/www/us/en/developer/tools/oneapi/vtune-profiler.html)
  analyzes CPU, accelerator, threading, and memory-performance behaviour.  It
  supports applications containing Fortran and can be installed separately or
  as part of the Intel oneAPI toolkits.
* [Linaro Forge](https://docs.linaroforge.com/latest/html/forge/forge/introduction_to_forge/index.html)
  combines the DDT parallel debugger, MAP profiler, and Performance Reports.
  It is designed for MPI, OpenMP, and accelerator-enabled HPC applications.
* [HPCToolkit](https://hpctoolkit.org/) is an open-source measurement and
  analysis suite for CPU and GPU-accelerated applications, including parallel
  programs.
* [Scalasca](https://www.scalasca.org/) is an open-source performance-analysis
  toolset for MPI, OpenMP, and hybrid applications.


## Build tools

* [Fortran Package Manager (fpm)](https://fpm.fortran-lang.org/): build system
  and package manager that creates Fortran project layouts, manages
  dependencies, and builds and runs applications and tests.  CMake remains
  useful for established or mixed-language projects and for integration with
  wider HPC software stacks.

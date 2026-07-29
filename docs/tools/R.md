# Tools for R programmers


## Code formatting

* [styler](https://styler.r-lib.org/): formats R source files, packages, and
  supported literate-programming documents according to a configurable style.


## Linting and static analysis

* [lintr](https://lintr.r-lib.org/): static analysis for style, syntax, and
  selected semantic problems.  It can be run from an editor, the R console, or
  continuous integration.


## Package and environment management

* [renv](https://rstudio.github.io/renv/): creates a project-local R library
  and lockfile so that package versions can be restored on another system.
  It records the R version but does not install R itself or manage compilers
  and system libraries.
* [pak](https://pak.r-lib.org/): fast package installer with dependency
  resolution and support for CRAN, Bioconductor, Git repositories, URLs, and
  local packages.  It complements rather than replaces an `renv` lockfile.


## Testing

* [testthat](https://testthat.r-lib.org/index.html): testing framework for R.


## Package development and documentation

* [usethis](https://usethis.r-lib.org/): automates repetitive project and
  package setup tasks.
* [devtools](https://devtools.r-lib.org/): convenient interface to common R
  package development, checking, testing, and documentation tasks.
* [roxygen2](https://roxygen2.r-lib.org/): generates R package reference
  documentation and namespace information from comments beside the code.


## Profiling

* [profvis](https://profvis.r-lib.org/): interactive visualization of profiling
  data collected by R's sampling profiler.


## Language interoperability

* [Rcpp](https://www.rcpp.org/): allows you to write C++ code that can be called
  from R.

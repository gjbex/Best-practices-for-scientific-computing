# Best practices for scientific computing

[![DOI](https://zenodo.org/badge/745445839.svg)](https://zenodo.org/doi/10.5281/zenodo.10665372)

Material for a training on best practices for scientific computing.

For participant-facing information about the training format, prerequisites,
level, and schedule, see the [training overview](training_overview.md).


## Programming languages

Although this training aims to be programming language-agnostic, the repository
also lists a number of tools that are programming language-specific.
Obviously, this can not be exhaustive, so feel free to suggest additional
tools if you are aware of any.

Programming languages covered:

  * C
  * C++
  * Fortran
  * Rust
  * Julia
  * Python
  * R


## Table of contents

  1. [Syntax versus semantics](syntax_vs_semantics.md)
  1. [Code style and conventions](code_style.md)
  1. [Version control & collaboration](version_control.md)
  1. [Code documentation](documentation.md)
  1. [Testing](testing/index.md)
     * [Testing as experiments](testing/testing_as_experiments.md)
     * [Testing scientific software](testing/scientific_testing.md)
     * [Unit testing](testing/unit_testing.md)
     * [Functional testing](testing/functional_testing.md)
     * [Code coverage](testing/code_coverage.md)
  1. [Optimization](optimization.md)
  1. [Deployment](deployment.md)
  1. [Continuous integration](continuous_integration.md)
  1. [Reproducibility](reproducibility.md)
  1. [References](references.md)
  1. [Tools](tools/index.md)
     * [C](tools/C.md)
     * [C++](tools/C-plus-plus.md)
     * [Fortran](tools/Fortran.md)
     * [Rust](tools/Rust.md)
     * [Julia](tools/Julia.md)
     * [Python](tools/Python.md)
     * [R](tools/R.md)
  1. [Further training](training.md)


## Acknowledgments

I've "borrowed" much of the table of contents from a
[training](https://www.esciencecenter.nl/event/good-practices-in-research-software-development-2/)
given by the Netherlands eScience Center, although no actual contents of that
training was used for the development of this material.

Thanks to the following people for their suggestions and comments:
* Ilaria Misuri: pointed out the `rpy2` package for using R from Python.

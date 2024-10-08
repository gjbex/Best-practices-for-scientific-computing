# Best practices in programming

[![DOI](https://zenodo.org/badge/745445839.svg)](https://zenodo.org/doi/10.5281/zenodo.10665372)

![Render and test
workflow](https://github.com/gjbex/Best-practices-in-programming/actions/workflows/build_and_deploy.yml/badge.svg)

Material for a training on best practices for programming and software
development, specifically for those working in the context of scientific
computing.

The material is available as a
[website](https://gjbex.github.io/Best-practices-in-programming/).


## Table of contents

1. Syntax versus semantics
1. Code style and conventions
1. Version control with git and collaboration
1. Code documentation
1. Testing
   * Testing as experiments
   * Unit testing
   * Functional testing
   * Code coverage
1. Optimization
1. Deployment
1. Continuous integration
1. Reproducibility
1. Tools
1. Training


## Programming languages covered

Although this training aims to be programming language-agnostic, the repository
also list a number of tools that are programming language-specific. Obviously,
this can not be exhaustive, so feel free to suggest additional tools if you are
aware of any.

Programming languages covered:

* C
* C++
* Fortran
* Python
* R

Of course, there are many programming language-agnostic tools as well.


## What is it?

1. `docs`: directory with the markdown source for the site.
1. `mkdocs.yml`: mkdocs configuration file.
1. `environment.yml`: conda environment for building the site.
1. `linkcheck_skip_file.txt`: skip file for
[linkcheck](https://github.com/filiph/linkcheck)
1. `LICENSE`: license for this repository and materials.
1. `CONTRIBUTING.md`: how to contribute to this repository.
1. `CODE_OF_CONDUCT.md`: code of conduct.


## About

This material is [licensed under Creative Commons](LICENSE).

You can [contribute](CONTRIBUTING.md) to this project in various ways.

Both contributing to this material and participating in the training are
subject to the [code of conduct](CODE_OF_CONDUCT.md).


## Acknowledgments

I've "borrowed" much of the table of contents from a
[training](https://www.esciencecenter.nl/event/good-practices-in-research-software-development-2/)
given by the Netherlands eScience Center, although no actual contents of that
training was used for the development of this material.

# Programming language-agnostic tools

This is a list of tools that are not specific to a specific
programming language.


## Version control

* [Git](https://git-scm.com/): version control software.
* [SmartGit](https://www.syntevo.com/smartgit/): Git GUI
  application that is cross-platform (Windows/MacOS/Linux) and can be used
  with multiple hosting services.
* [DVC](https://dvc.org/): Data Version Control, tool to manage versions of
  your data alongside your code.  Using this tool avoids having to commit
  large files into a git repository for which it is not intended.
* [GitHub](https://github.com/): hosting platform.
* [GitLab](https://about.gitlab.com/): hosting platform.


## Build tools

Some build tools can be used for many programming languages.  Build tools let
you specify how to build your applications and libraries, but often also how
to test and package them.

* [CMake](https://cmake.org/): cross-platform build tool that can be used to
  build and install C/C++/Fortran libraries and applications.  A number of
  examples of using CMake in various scenarios can be found in the repository on
  [CMake use cases](https://github.com/gjbex/CMake-usecases).


## Package managers

Some package managers are fairly specific to a particular programming language,
but others can be used for multiple languages, or even workflows.

* [Spack](https://spack.io/): package manager that can be used to install
  software in a controlled environment, ensuring that the software is built
  with the required dependencies, compilers, variants, and compiler options.
  It is particularly useful for HPC software stacks and installations that
  must support several compilers or hardware targets.
* [Pixi](https://pixi.prefix.dev/latest/): project and environment manager
  based on the conda and Python package ecosystems.  It provides lockfiles,
  tasks, and multiple environments, and is useful when a scientific project
  combines Python packages with compiled libraries.  It does not replace
  Spack when an HPC installation must manage detailed compiler, MPI, or
  architecture variants.


## Libraries

Libraries are collections of code that can be used to perform specific tasks.
The libraries listed here are useful in the context of scientific computing.
They are available in multiple programming languages via bindings, or used
under the hood by language-specific libraries.

*  [BLAS](https://www.netlib.org/blas/): Basic Linear Algebra Subprograms,
   a standard interface for basic vector and matrix operations.  Reference,
   vendor, and open-source optimized implementations are available, and the
   implementation chosen can have a large effect on performance.
*  [LAPACK](https://www.netlib.org/lapack/): Linear Algebra PACKage, a library
   that provides routines for solving systems of linear equations, linear
   least squares problems, eigenvalue problems, and singular value
   decomposition.
*  [FFTW](https://www.fftw.org/): Fastest Fourier Transform in the West, a
    library that provides routines for computing the Discrete Fourier
    Transform (DFT) and its inverse.


## Containers

Containers package an application with much of its user-space environment and
dependencies, making it easier to share and run on other systems.  They
contribute to reproducibility, but do not capture the host kernel, hardware,
drivers, or all runtime settings.  Consequently, a container alone does not
guarantee identical numerical results on different machines or at different
times.

* [Docker](https://www.docker.com/): containerization tool that can be used to
  build and run OCI container images containing an application's user-space
  software environment.
* [Podman](https://podman.io/): a daemonless container engine for developing,
  managing, and running OCI containers.
* [Apptainer](https://apptainer.org/): containerization tool that is
  compatible with Singularity images and able to use images from OCI
  registries. It is designed for shared and HPC environments and normally runs
  containers without giving the user elevated privileges.  Whether users can
  build images without privileges depends on how Apptainer is installed and
  configured.


## Workflows

* [Snakemake](https://snakemake.readthedocs.io/en/stable/): a workflow
  management system that aims to reduce the complexity of creating workflows
  by providing a readable and expressive syntax in Python style.
* [Nextflow](https://www.nextflow.io/): a workflow manager that enables the
  development of portable and reproducible workflows. It comes with a
  domain-specific language that simplifies the writing of complex
  computational workflows.


## Documentation

In this session, we will discuss two tools for creating attractive
documentation, Doxygen and MkDocs.  The former is best suited for reference
guides, while the latter is excellent for tutorial-style material.

1. [Doxygen](https://www.doxygen.nl/): some programming languages such as Java
    and Python provide support for documentation as part of their
    specification. The languages we use most frequently in an HPC context, C,
    C++, and Fortran, have no such provisions.  However, Doxygen generates
    reference documentation out of comment blocks for a wide variety of
    programming languages, including those of interest to us. This documentation
    is fully hyperlinked. For instance, clicking the type of a function's
    argument will bring you to the type's documentation.
1. [MkDocs](https://www.mkdocs.org/): this is a very convenient tool for
   generating nice looking documentation that can be viewed standalone as HTML
   pages, or that can be served from the
   Read the Docs service. It automatically
   generates a navigation panel and adds search functionality. You can also
   define a GitHub trigger that will automatically push your project's
   documentation to Read the Docs each time you do a release. Documentation of
   previous software versions remain available. In that scenario, MkDocs will
   provide useful previews before you make a release of your code project.
1. [Sphinx](https://www.sphinx-doc.org/en/master/): this is another tool to
   generate documentation.  It can generate API reference documentation for
   Python, and tutorial style documentation in general.  The resulting
   documentation can be hosted on Read the Docs or GitHub Pages.
1. [Quarto](https://quarto.org/docs/guide/): an open-source scientific and
   technical publishing system for executable reports, manuscripts,
   presentations, websites, and books.  It complements rather than replaces
   API-reference tools such as Doxygen and Sphinx.
1. [Read the Docs](https://readthedocs.org/): a hosting service for
   documentation.  It supports both MkDocs and Sphinx.  Documentation can be
   fetched from a GitHub repository and (re)built.  This can be automated and
   set to be triggered by, e.g., a merge into main.
1. [GitHub Pages](https://pages.github.com/): you can activate Pages for any
   GitHub repository.  This will create a website that you can use to host the
   documentation for your
   project to make it available to your group or even to every user of your
   software.  The documentation can be generated using a GitHub Action
   triggered by, for instance, a merge into the main branch.  The repository
   that [hosts this
   information](https://github.com/gjbex/Best-practices-for-scientific-computing)
   is an
   example of that.


## Testing

Some testing tools are generic and can be used to do functional testing for
applications developed in any programming language.

1. [Bats-core](https://github.com/bats-core/bats-core): a
   community-maintained testing framework for Bash and other command-line
   programs that emits Test Anything Protocol (TAP) output.
1.  [CTest](https://cmake.org/cmake/help/latest/manual/ctest.1.html):
   CTest is part of CMake and lets you do functional testing as part of the
   build process.


## Automating local checks

[pre-commit](https://pre-commit.com/) manages repository-configured checks that
can run before a commit and in continuous integration.  It can invoke
formatters, linters, and simple repository checks written in different
languages.  It automates selected tools; it is not itself a formatter, linter,
or substitute for a test suite.


## Licensing

Selecting an appropriate license is not trivial.

1. [Website](https://choosealicense.com/) that tries to guide you through the
   process.


## Attribution

1. [Zenodo](https://zenodo.org/): general-purpose research repository that can
   archive a software release and assign it a Digital Object Identifier (DOI).
   Its GitHub integration can create a new archive for each enabled GitHub
   release.

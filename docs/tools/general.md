# Programming language-agnostic tools

This is a list of tools that are not specific to a specific
programming language.


## Version control

* [git](https://git-scm.com/): version control software.
* [SmartGit](https://www.syntevo.com/smartgit/): nice git GUI
  application that is cross-platform (Windows/MacOS/Linux) and can be used
  with multiple hosting services.
* [DVC](https://dvc.org/): Data Version Control, tool to manage versions of
  your data alongside your code.  Using this tool avoid having to commit
  large files into a git repository for which it is not intended.
* [GitHub](https://github.com/) hosting platform.
* [GitLab](https://about.gitlab.com/) hosting platform.


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
  with the correct dependencies and compiler options.


## Libraries

Libraries are collections of code that can be used to perform specific tasks.
The libraries listed here are useful in the context of scientific computing.
They are available in multiple programming languages via bindings, or used
under the hood by language-specific libraries.

*  [BLAS](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms):
   Basic Linear Algebra Subprograms, a library that provides standard
   building blocks for performing linear algebra operations.
*  [LAPACK](https://en.wikipedia.org/wiki/LAPACK): Linear Algebra PACKage, a library
    that provides routines for solving systems of linear equations, linear
    least squares problems, eigenvalue problems, and singular value
    decomposition.
*  [FFTW](http://www.fftw.org/): Fastest Fourier Transform in the West, a
    library that provides routines for computing the Discrete Fourier
    Transform (DFT) and its inverse.


## Containers

Containers are a way to package your code and its dependencies in a way that
makes it easy to share with others.  They can be used to ensure that your code
runs in the same environment on different machines.  In addition, they can be
used to ensure that your code runs in the same environment at different times,
contributing to the reproducibility of your results.

* [Docker](https://www.docker.com/): containerization tool that can be used to
  specify the exact environment in which your code is run, including the
  operating system and the versions of all software used.
* [Podman](https://podman.io/): a daemonless container engine for developing,
  managing, and running OCI Containers on your Linux System.
* [Apptainer](https://apptainer.org/): containerization tool that is
  compatible with Singularity and Docker. It is designed to be used in an
  HPC environment and doesn't require root privileges to build images and
  run containers.


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

1. [Doxygen](http://www.doxygen.org/): some programming languages such as Java
    and Python provide support for documentation as part of their
    specification. The languages we use most frequently in an HPC context, C,
    C++, and Fortran, have no such provisions.  However, Doxygen generates
    reference documentation out of comment blocks for a wide variety of
    programming languages, including those of interest to us. This documentation
    is fully hyperlinked. For instance, clicking the type of a function's
    argument will bring you to the type's documentation.
1. [MkDocs](http://www.mkdocs.org/): this is a very convenient tool for
   generating nice looking documentation that can be viewed standalone as HTML
   pages, or that can be served from the
   ReadTheDocs service. It automatically
   generates a navigation panel and adds search functionality. You can also
   define a GitHub trigger that will automatically push your project's
   documentation to Read the Docs each time you do a release. Documentation of
   previous software versions remain available. In that scenario, MkDocs will
   provide useful previews before you make a release of your code project.
1. [Sphinx](https://www.sphinx-doc.org/en/master/): this is another tool to
   generate documentation.  It can generate API reference documentation for
   Python, and tutorial style documentation in general.  The resulting
   documentation can be hosted on ReadTheDocs or GitHub pages.
1. [ReadTheDocs](http://www.readthedocs.org/): a hosting service for
   documentation.  It supports both MkDocs and Sphinx.  Documentation can be
   fetched from a GitHub repository and (re)built.  This can be automized and
   set to be triggered by, e.g., a merge into main.
1. [GitHub pages](): you can activate pages for any GitHub repository.  This
   will create a website that you can use to host the documentation for your
   project to make it available to your group or even to every user of your
   software.  The documentaiton can be genreated using a GitHub Action
   triggered by, for instance, a merge into the main branch.  The repository
   that [hosts this
   information](https://github.com/gjbex/Best-practices-in-programming) is an
   example of that.


## Testing

Some testing tools are generic and can be used to do functional testing for
application developed in any programming language.

1. [shunit2 framework](https://github.com/kward/shunit2): use Bash scripts to
   perform functional testing as unit tests.
1.  [CTest](https://cmake.org/cmake/help/book/mastering-cmake/chapter/Testing%20With%20CMake%20and%20CTest.html#:~:text=CTest%20is%20an%20executable%20that,for%20CTest%20is%20called%20CTestTestfile.):
   CTest is part of CMake and lets you do functional testing as part of the
   build process.


## Licensing

Selecting an appropirate license is not trivial.

1. [Website](https://choosealicense.com/) that tries to guide you through the
   process.


## Attribution

1. [Zenodo](https://github.com/gjbex/Best-practices-in-programming): website to
   request a Digital Object Identifier (DOI) for your version control
   repositories.

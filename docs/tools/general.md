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

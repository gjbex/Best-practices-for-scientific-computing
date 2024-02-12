# Deployment

Making sure you software can be build and installed easily is a very important
part of the software's life cycle.  It will be a hard requirement if you intend
your software to be adopted and used by others.


## Building software

### C, C++ and Fortran

For C, C++ and Fortran the build system of choice would be
[CMake](https://cmake.org/).  You describe what you want to build, e.g., a
library or an executable and add the dependencies, i.e., the directories
where to find header files or libraries, as well as the libraries that
are required.  You can specify compiler flags for the entire project, or
specifically for an individual target.

CMake has a lot of support to find installed libraries on your system, so
this will ensure that builds are much more likely to succeed on other
systems as well, as long as the dependencies have been installed.

Many IDEs have built-in support for CMake.

A number of examples of using CMake in various scenarios can be found in the
repository on [CMake use cases]().


### Python

Poetry is an interesting tool to help you manage all stages of a Python
software projects.

It helps you to set up an environment with all required dependencies and run
your code in it.  It also has direct support for testing your implementation
using `pytest`.

You start by initializing a project and adapting the configuration file to
your needs.  It will also allow you to conveniently run several tools such
as `mypy` to type check your code, `black` to format your code.

Finally, you can easily package your project in a wheel or source distribution
and upload it to PyPi.

If the Poetry configuration file is under version control, this approach also
helps you to share your development environment among team members.

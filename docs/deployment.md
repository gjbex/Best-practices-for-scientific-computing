# Deployment

## Build tools

Making sure you software can be built and installed easily is a very important
part of the software's life cycle.  It will be a hard requirement if you intend
your software to be adopted and used by others.

For compiled langauges such as C, C++ and Fortran you will need to set up how to
compile and link your code.  Several build environment are available such as
autotools and CMake.

Although scripting languages such as Python and R don't require compilation you
would still rely on these environments if you build extensions for these
languages.

Although it takes time to properly configure the build process, and there is a
learning curve, it will save you a lot of time in the long run.

Most build environments also allow you to run tests, and that includes those for
scripting languages.  Integrating test execution as part of your build process
is most certainly a best practice.


## Deployment

Most build environments let you easily create distributions of your software
projects, for instance under the form of source archives that include the build
configuration files.

Some environments go even a step further by supporting uploads to software
distribution repositories.

The build systems can also be configured to do the installation of software,
something that can be tuned further by the person who installs the software on
her own system.


## Package managers

Many software project rely on packages that need bo be installed to succesfully
link or run the application or library.  Managing these dependencies can be
pretty tedious.

Some build tools will help you to easily integrate such libraries by configuring
the build configuration with the information on where they are installed on a
system.

Most build systems also support a form a depedency management or package
management that allows you to easily download and install packages.  Typically
these installs will be local to the project, so it is not necessary to install
them centrally and "pollute" your system.

This dependency isolation makes it easier to test the software build system and
makes it more portable to other computers and operating systems.


## License

A very important aspect of software deployment is licensing.  Releasing software
without a license or with one that is not appropriate can have dire
consequences.

It is also very important to verify that the licenses of software component or
tools are compatible with the one you select for yourself.

There is a nice website that helps you [select an appropriate
license](https://choosealicense.com/).  However, when in doubt, get in touch
with your Technology Transfer Office, they will be able to advice.


## Examples

Examples of using various tools can be found in other repositories.

  * [CMake use cases](https://github.com/gjbex/CMake-usecases)
  * [Poetry](https://github.com/gjbex/CI-example)
  * [C/C++ package
    managers](https://github.com/gjbex/C-plus-plus-software-engineering)

# Code coverage


# Introduction

Unit tests are very useful to formulate fine-grained test to check the
functionality of functions and methods. Unit tests check for edge and corner
cases, but also for handling of error conditions such as exceptions being
thrown.

This is of course very useful in itself, but using a run of the complete unit
test suite can also provide a good test to see whether all functions and methods
are called, and all codes paths in the code get executed.

Code coverage tools will instrument your code, run it, and provide feedback on
regions of code that are not executed doing that run.

Since we claim that code that is not tested is not correct, coverage provided by
running all the unit tests should in fact be (close to) 100 %.  If code coverage
is insufficient, more unit tests should be added to the test suite.


# Best practices

Maintaining code over long periods of time is quite expensive. The larger the
code base, the more effort has to be spent on keeping code up to date. If some
parts of the code are never used, that adds to this burden without return on
investment. Updates are an issue as well, since some unused parts of the code
may get out of sync with respect to the parts that are executed regularly. If
someone starts using the abandoned part of the code, interesting bugs may creep
into her code.

Hence code that is not used is best removed from the code base. If you use a
version control system and informative commit messages, it is quite easy to
recover that code later when it is unexpectedly required.

An important concern when writing tests for your software project is whether or
not all branches in function, and indeed all functions are tested. Figuring out
by hand whether that is the case is pretty hard for sizable projects.

Fortunately, software tools are available for checking which parts of the code
base are executed and which are not.  For many programming languages, one has to
resort to third party tools, but the compilers for C, C++ and Fortran support
this out of the box.

The first step in the workflow is to instrument the code with instructions to do
the bookkeeping for reporting which lines of code have been executed. Compilers
have options to do that automatically, so this can easily be incorporated into
the build process by adding a make target specific for a code coverage build.

The second step is to execute the software, so that a report is generated. In
case you wonder how to run your code to get the most useful report, this depends
on your goal. If you want to detect code that is likely not executed in
applications, running a number of typical use cases are the best way to go. On
the other hand, if you want to verify that you have a comprehensive set of unit
tests, execute those.

The third step is to inspect that report. Typically, you will get summary
information, e.g., the percentage of the code covered in each file. In addition,
each individual file can be inspected on a line by line basis. Lines that have
not been executed are clearly marked, so that they are easy to spot.

Finally, you decide to either weed out the lines if they are dead code, i.e.,
code that will never be executed in the context of your project, or to create
additional unit tests if that code will be executed but is not tested yet.

Since code coverage tests produce artifacts, it is best to add rules to remove
these artifacts to your make file.  This ensures you start with a clean slate
when rebuilding. 

Code coverage assessment is an important tool for delivering good quality code,
and goes hand in hand with unit testing and functional testing.

# Reproducibility

A very important aspect of scientific research is the ability to reproduce the
results of an experiment. There are a number of factors that can affect the
reproducibility of an experiment, including

 * the versions of the software used, including your own code and any
   third-party libraries;
 * the data ingestion process, including the data sources and the data cleaning
   process;
 * the seed used for random number generation;
 * the (hyper)parameters used for the experiment;
 * the computational environment, including the operating system and the
   hardware used.

Not only should you be able to reproduce your own results, but others should be
able to do so as well, e.g., the reviewers of a paper that you submit for
publication.  This is important for the credibility of your work.

This is also crucial to allow other researchers to build on your work.  If they
cannot reproduce your results, it is hard to assess the potential improvements
of their own work.


## Software versions

To ensure that you can reproduce results generated using your own code, it is
important to use a version control system.  Using tags appropriately can help
you to keep track of the versions used to generate results for, e.g., the
submission of a paper.  For more information on version control, see the
[Version Control](version_control.md) page.

In addition to version control for your own code, it is also important to keep
track of the versions of third-party libraries that you use.  This can
typically be done by using a package manager, such as miniconda or Poetry for
Python.  Package managers typically allow to specify requirements in a text
file that can be versioned along with your project.  For C++ or Fortran, the
build system, e.g., CMake, can be used to specify the versions of libraries
used.

One step futher is to use a containerization tool, such as Docker, Singularity,
or Apptainer. These tools allow you to specify the exact environment in which
your code is run, including the operating system and the versions of all
software used.  The container definition is a simple text file that can be
version controlled along with your code.  This makes it easy to share your code
and the environment in which it was run with others, ensuring that they can
reproduce your results.

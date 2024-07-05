# Reproducibility

A very important aspect of scientific research is the ability to reproduce the
results of an experiment. There are a number of factors that can affect the
reproducibility of an experiment, including

 * the data used;
 * the versions of the software used, including your own code and any
   third-party libraries;
 * the workflow used to run the experiment, including the order in which
   scripts are run;
 * the (hyper)parameters used for the experiment.

Not only should you be able to reproduce your own results, but others should be
able to do so as well, e.g., the reviewers of a paper that you submit for
publication.  This is important for the credibility of your work.

This is also crucial to allow other researchers to build on your work.  If they
cannot reproduce your results, it is hard to assess the potential improvements
of their own work.


## Data

The first step in ensuring that your results are reproducible is to keep track
of the data used in your experiments.  Ideally, your data resides in a data
repository that gives long-term access to the data.

Some of these repositories are domain-specific, but there are also general
repositories that can be used to store data from any domain.  Some of these
repositories are built to support the FAIR principles, which state that data
should be

  * Findable;
  * Accessible;
  * Interoperable;
  * Reusable.

Findable means that the data should be easy to find for both humans and
computers, e.g., by using a unique identifier such as a digital object
identifier (DOI), but also by adding metadata to the data.

Accessible means that the data should be easy to access, e.g., by providing a
download link, but also by providing the data in a format that is easy to use.

Interoperable means that the data should be easy to combine with other data,
e.g., by using a standard format, but also by providing metadata that describes
the data.

Reusable means that the data should be easy to reuse, e.g., by providing
metadata that describes the data, but also by providing documentation that
explains how the data was generated.

Of course you might not want to share all or any of your data while a research
project is ongoing, so many repositories allow you to keep your data private
until you are ready to share it.  However, it is a good idea to start thinking
about where you will store your data once the project is finished, as this will
make it easier to share your results with others.  Many funding agencies now
require that data be made available after a project is finished, and even
require a data management plan as part of a project proposal.

Typically, storing data sets directly in your version control system is not
possible due to restrictions on the size of files that can be stored.  However,
you can use a tool such as [DVC](https://dvc.org/) to manage versions of your
data.  DVC stores the data in a separate location, and keeps track of the
versions of the data in a text file that can be version controlled along with
the other artifacts of your experiments.


## Software versions

To ensure that you can reproduce results generated using your own code, it is
important to use a version control system.  Using tags appropriately can help
you to keep track of the versions used to generate results for, e.g., the
submission of a paper.  For more information on version control, see the
section on [version control](version_control.md).

In addition to version control for your own code, it is also important to keep
track of the versions of third-party libraries that you use.  This can
typically be done by using a package manager, such as
[miniconda](https://docs.anaconda.com/miniconda/) or
[Poetry](https://python-poetry.org/) for Python.  Package managers typically
allow to specify requirements in a text file that can be versioned along with
your project.  For C, C++ or Fortran, the build system, e.g.,
[CMake](https://cmake.org/) , can be used to specify the versions of libraries
used.

At the level of entire software packages, but also for libraries, the
[Spack](https://spack.io/) package manager can be used to specify the exact
versions of software used. Spack can be used to install software in a
controlled environment, ensuring that the software is built with the correct
dependencies and compiler options.

Going one step further you can use a containerization tool, such as
[Docker](https://www.docker.com/), [Podman](https://podman.io/) , or
[Apptainer](https://apptainer.org/). These tools allow you to specify the exact
environment in which your code is run, including the operating system and the
versions of all software used.  The container definition is a simple text file
that can be version controlled along with your code.  This makes it easy to
share your code and the environment in which it was run with others, ensuring
that they can reproduce your results.

Clearly, the environment specification or the container definition should
mention explicit version numbers for all software used, including the operating
system.  This ensures that the environment in which your code is run is exactly
the same which ensures that your results are reproducible.

Obviously, the environment specification or the container definition should be
version controlled along with your code.  This ensures that you can reproduce
the results of your experiments at any time in the future.

**Important note on performance:** using package managers or containerization
tools such as Docker can have an impact on the performance of your code.  This
is because the software is built with specific compiler options and
dependencies that may not be optimal for your specific use case. For this
reason, it is important to test the performance of your code in the environment
in which it will be run, and to optimize the build options if necessary.

For containers, it is best practice to build those on a similar environment as
the one on which they will be run.  This is especially important if you are
running your code on a high-performance computing (HPC) system, where the
hardware and software environment can be quite different from your own
workstation.  However, if you use Linux package managers for
performance-critical applications while building your container, the results
are likely to be suboptimal.


## Workflows

An experiment or series of experiments typically involves a number of steps:

  * data ingestion;
  * data preprocessing;
  * running one or more applications;
  * postprocessing the results.

The bare minimum you should do is to have an accurate, complete description of
the steps to be taken.  Better still, write a script that automates the entire
process.  This can be done in various ways, ranging from quite straightforward
shell scripts to more complex workflows using tools such as
[Nextflow](https://www.nextflow.io/), or
[Snakemake](https://snakemake.readthedocs.io/en/stable/).

An additional advantage of using a workflow management system is that it can
help you to redo only the parts of the workflow that are affected by changes in
the input data or the code.  This can save a lot of time when you are
developing your code, as you do not have to rerun the entire workflow every
time you make a change.

Of course, the development overhead of creating a full fledged workflow will be
only worth the effort if the workflow is involved enough.  For simple
experiments, a shell script may be sufficient.

Note that the workflow can now be version controlled along with your code, and
the environment specification or the container definition.  This ensures that
you can reproduce the results of your experiments at any time in the future.


## Parameters

The final aspect of reproducibility is the parameters used for the experiment.
These can be the parameters of data preprocessing, the parameters of the
application, or the parameters of the postprocessing.  It is important to keep
track of these parameters, as they can have a significant impact on the results
of the experiment.

It is therefore good practice to store the parameters used for an experiment in
one or more separate files, and to version control these files.

If you develop your own software, it is good practice to ensure that the
application can be run with parameters stored in a configuration file.
Libraries exist for many programming languages that can be used to read
configuration files, e.g., [Hydra](https://hydra.cc/) for Python, or for
Python, or [libconfig](https://hyperrealm.github.io/libconfig/) for C/C++.

Note that some preprocessing steps and applications may use a random number
generator.  In this case, it is important to store the seed of the random
number generator along with the parameters used for the experiment.  This
ensures that the results of the experiment can be reproduced exactly.

# Further training

This four-hour training provides an overview of good practices and explains why
they matter for scientific work.  The courses below provide more extensive
hands-on treatment of particular topics.  They are grouped by the need they
address rather than by the organization that offers them.

The [training sessions catalogue](https://gjbex.github.io/Training-sessions/)
contains the complete collection, including learning paths for HPC application
development and data science.  A course website normally provides the training
material even when no live session is currently scheduled.


## Version control and collaboration

The [version-control section](version_control.md) in this training concentrates
on motivation, traceability, recovery, collaboration, and scientific
provenance.

* [Version control with
  Git](https://gjbex.github.io/Version-control-with-git/) provides the detailed
  hands-on follow-up.  It covers individual and collaborative workflows,
  repository hosting, history, branches, graphical clients, and command-line
  use.


## Code quality, testing, documentation, and debugging

These courses extend the [code-style](code_style.md),
[documentation](documentation.md), and [testing](testing/index.md) sections
with language-specific tools and exercises.

* [Defensive programming and
  debugging](https://gjbex.github.io/Defensive_programming_and_debugging/)
  covers coding practices, compiler and static checks, unit and functional
  testing, documentation, and debugging tools.  It is the most
  language-agnostic follow-up in this group, although many examples use
  compiled languages.
* [C++ software
  engineering](https://gjbex.github.io/C-plus-plus-software-engineering/)
  applies the practices to C++ projects, including CMake, static analysis,
  Catch2, CTest, package management, and design.
* [Python software
  engineering](https://gjbex.github.io/Python-software-engineering/) applies
  them to Python, including coding practices, type annotations, error handling,
  documentation, unit testing, and software design.

These courses concentrate mainly on software behavior.  The
[scientific-testing section](testing/scientific_testing.md) in this repository
adds numerical tolerances, invariants, convergence, stochastic behavior, and
parallel consistency.


## Performance optimization and scalability

Optimization should start only after the behavior of the program is protected
by suitable tests.  The [optimization section](optimization.md) provides the
motivation and basic workflow; the following courses go further.

* [Code optimization](https://gjbex.github.io/Code-optimization/) covers
  computer architecture, scaling, memory behavior, vectorization, profiling,
  and performance pitfalls.
* [POP online
  training](https://pop-coe.eu/further-information/online-training) introduces
  a methodology and tools for analysing the performance of parallel
  applications.
* The [parallel-computing training
  overview](https://gjbex.github.io/Training-sessions/parallel_computing/)
  links to courses on MPI, OpenMP, parallel C++, and accelerator programming.
* [Python for HPC](https://gjbex.github.io/Python-for-HPC/) is useful when a
  Python application needs profiling, compiled numerical libraries, or
  language-specific approaches to improved performance.


## Deployment, environments, and reproducible workflows

The [deployment](deployment.md), [continuous-integration](continuous_integration.md),
and [reproducibility](reproducibility.md) sections introduce the relevant
principles.  The following courses cover particular execution and workflow
environments.

* [Containers for HPC](https://gjbex.github.io/Containers-for-HPC/) covers
  building and running portable container images in an HPC environment.
  Containers can capture much of a runtime environment, but they do not by
  themselves guarantee reproducible scientific results.
* [Workflows for HPC](https://gjbex.github.io/Workflows-for-HPC/) covers tools
  and practices for organizing and executing multi-step computational
  workflows.
* [MLOps on HPC](https://gjbex.github.io/MLOps-on-HPC/) addresses reproducible
  and maintainable computational experiments.  Despite its name, much of the
  workflow guidance is also relevant outside machine learning.
* [Jupyter notebooks](https://gjbex.github.io/Jupyter-notebooks/) covers
  effective notebook use for exploratory programming and data analysis.
  Notebook files still need appropriate environment, data, testing, and
  version-control practices.

The catalogue currently has no dedicated general continuous-integration
course.  The C++ and Python software-engineering courses above cover many of
the build, analysis, test, and documentation commands that a CI workflow would
automate.


## Scientific data and I/O

The [scientific I/O and data-formats section](scientific_io.md) introduces
format selection, metadata, validation, checkpointing, and the relationship
between access patterns and performance.

* [Best practices for data science on
  HPC](https://gjbex.github.io/Best-practices-for-data-science-on-HPC/)
  provides the detailed follow-up.  It includes experiments with tabular,
  textual, and image data, structured formats, and the many-small-files problem
  on HPC filesystems.


## Programming-language foundations

This training assumes fluency in at least one programming language.  If a
participant needs to learn or refresh a language first, the catalogue contains
the following relevant courses.

* [Scientific C](https://gjbex.github.io/Scientific-C/)
* [Scientific C++](https://gjbex.github.io/Scientific-C-plus-plus/)
* [Fortran for programmers](https://gjbex.github.io/Fortran-for-programmers/)
* [Python for
  programmers](https://gjbex.github.io/Python-for-programmers/) and
  [Scientific Python](https://gjbex.github.io/Scientific-Python/)
* [Julia: the good, the bad and the
  ugly](https://gjbex.github.io/Julia_good_bad_ugly/)
* [Rust: the good, the bad and the
  ugly](https://gjbex.github.io/Rust-good-bad-ugly/)

The [programming overview](https://gjbex.github.io/Training-sessions/programming/)
shows how these language courses connect to software engineering, parallel
computing, and GPU computing.  There is currently no R-specific course in this
catalogue; the [R tools page](tools/R.md) provides project-tool guidance for
participants using R.


## Linux and HPC foundations

Command-line and HPC-system skills are prerequisites rather than topics of this
training.  Participants who need that background can start with

* [Linux
  introduction](https://gjbex.github.io/Training-sessions/linux_intro/), for
  shell, file, process, and remote-access basics; and
* [HPC
  introduction](https://gjbex.github.io/Training-sessions/hpc_intro/), for
  cluster architecture, software environments, storage, schedulers, and
  resource use.


## Finding scheduled sessions

The course websites above provide material and course descriptions; they do not
necessarily show the next scheduled delivery.  Current offerings and
registration can be found through

* the [Vlaams Supercomputer Centrum
  training calendar](https://www.vscentrum.be/vsctraining);
* [EuroCC ACCESS training](https://www.eurocc-access.eu/services/training/);
  and
* the [CÉCI HPC training programme](https://www.ceci-hpc.be/training/).

Schedules, prerequisites, delivery formats, and access conditions change, so
check the provider's current course page before registering.

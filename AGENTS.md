# Repository guidance

## Purpose and scope

This repository contains training material on good software-development
practices for scientific computing.  It is intended for researchers, PhD
students, research software engineers, and technical staff who already have
programming experience.

The training is primarily programming-language agnostic.  Language-specific
examples and tool recommendations may support sessions tailored to C, C++,
Fortran, Rust, Julia, Python, or R, but the main concepts should remain
transferable between languages and scientific domains.

The standard training session lasts four hours.  Keep additions proportionate
to the stated learning outcomes and schedule, and prioritize scientific
relevance, practical motivation, and concepts that participants can apply to
their own work.  Avoid turning introductory sections into exhaustive technical
tutorials.

Where a topic has a dedicated training repository, avoid duplicating detailed
material that would then have to be maintained in two places.  For example,
this repository should motivate version control and demonstrate its value,
while detailed Git mechanics and hands-on instruction belong in
`Version-control-with-git`.

When the training content changes, check the learning outcomes, schedule,
training overview, navigation, exercises, and `TODO.md` for corresponding
updates.  Keep participant-facing statements about the scope and supported
language tracks consistent across the repository.


## Maintaining tool recommendations

When adding or revising material under `docs/tools/`, check the current
upstream documentation and maintenance status of the tools concerned.  Do not
assume that a working link means that a tool remains maintained or is still a
good default.

During occasional maintenance reviews, check for deprecated, archived, or
superseded tools and for important changes in scope or platform support.
Prefer official project documentation and current primary sources when making
these assessments.

Evaluate recommendations in the context of scientific computing as well as
general software development.  In particular, consider compiled libraries,
compilers, MPI, accelerators, HPC-site restrictions, reproducibility, and
continuous-integration support where relevant.  Update related comparison
text, navigation, and language-specific pages together when a recommendation
changes.

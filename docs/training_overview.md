# Training overview

As a scientist, your core business is science, not software engineering.
Nevertheless, having a good understanding of how best practices in software
engineering can help you work more efficiently, make your work easier to reuse,
and give your work more exposure is useful.

This training is flexible. It can be tailored to C, C++, Fortran, Rust, Julia,
Python, R, or a language-agnostic mix, and the depth can be adapted to the
audience.


## Learning outcomes

When you complete this training you will be able to

* explain why software engineering practices matter for scientific computing;
* explain how version control supports traceability, recovery, collaboration,
  and scientific provenance;
* recognize the role of code style, documentation, testing, and reproducibility
  in scientific software;
* identify scientifically meaningful properties and numerical comparisons for
  testing scientific software;
* distinguish between unit tests, functional tests, and code coverage;
* recognize how deployment and continuous-integration practices support
  reliable scientific software;
* choose relevant tools for the programming language and project context you
  work in.


## Schedule

Total duration: 4 hours.

Because the training is flexible, the exact schedule can be adapted to the
programming language and level of detail requested.

  | Subject                                        | Duration |
  |------------------------------------------------|----------|
  | introduction and motivation                    | 10 min.  |
  | code style and conventions                     | 30 min.  |
  | motivation for version control and collaboration | 20 min. |
  | testing, including scientific correctness      | 70 min.  |
  | documentation                                  | 30 min.  |
  | deployment and continuous integration          | 40 min.  |
  | reproducibility and wrap up                    | 40 min.  |


## Training materials

The training material is available as this website:

<https://gjbex.github.io/Best-practices-for-scientific-computing/>

The source repository is available on GitHub:

<https://github.com/gjbex/Best-practices-for-scientific-computing>


## Target audience

This training is for researchers, PhD students, research software engineers, and
technical staff who write or maintain software in a scientific-computing
context.

It is especially useful if your scripts, notebooks, or applications are becoming
important enough that they need to be shared, reviewed, tested, reproduced, or
maintained over time.


## Prerequisites

You should be fluent in at least one programming language. The training is not
an introduction to programming.

If you plan to apply the material in a Linux or HPC environment, you should be
familiar with those environments as well.


### Quick self-assessment

If you can do most of the tasks below in a programming language you use for
scientific work, you are likely ready for this training.

* read and modify an existing script, notebook, or small program;
* split repeated code into a function or helper module;
* use the command line to run code or inspect files;
* explain what input data, output files, and parameters a small analysis uses;
* recognize when code would be difficult for a colleague to understand or reuse;
* make a small change and check whether the result still looks correct;
* use or be willing to learn version control for collaborative work.

If several of these items still feel difficult, the training will probably move
too fast. In that case, it is better to first refresh the basics of your main
programming language and command-line workflow.


### Software and access requirements

To follow hands-on, you need a computer with the tools used for the selected
language track. At minimum, you should have access to:

* a shell environment;
* Git;
* a text editor or IDE;
* the compiler, interpreter, or notebook environment for the programming
  language used in the session.

For sessions on an HPC system, make sure you can log in, edit files, submit
jobs if needed, and load the relevant software environment.


## Level of the Material

For participants who already have programming experience, the material in this
training is approximately

* Introductory: 30 %
* Intermediate: 50 %
* Advanced: 20 %

These percentages describe the level of the software-engineering and
scientific-computing topics covered in the training, not the participants'
general programming background.


## Trainer(s)

  * Geert Jan Bex ([geertjan.bex@uhasselt.be](mailto:geertjan.bex@uhasselt.be))

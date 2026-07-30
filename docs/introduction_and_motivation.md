# Introduction and motivation

Scientific software is often written to answer a question rather than to
become a software product.  A script may begin as a quick experiment and then
grow into an analysis used for a paper, a simulation shared by a research
group, or an application on which later work depends.

At that point, the important question is no longer only whether the program
runs.  We also need to know what it computed, why its result should be trusted,
which inputs and assumptions it used, and whether another researcher can
understand or repeat the work.


## Scientific software is part of the method

Source code expresses choices that can affect scientific conclusions:
equations, constants, units, numerical methods, tolerances, quality criteria,
and data transformations.  A small software change can therefore change a
result without producing an obvious error message.

Good software-development practices are not administrative work added after
the science.  They help make the computational part of the scientific method
inspectable:

* readable code communicates the procedure;
* version control records how that procedure changed;
* static analysis identifies some implementation defects early;
* tests provide evidence about software behaviour and scientific correctness;
* documentation preserves interfaces, assumptions, and limitations;
* meaningful data formats preserve the interpretation of inputs and outputs;
* automation applies agreed checks consistently; and
* reproducibility connects a result to its code, data, configuration, and
  environment.

None of these practices proves that a scientific claim is true.  Together,
they make mistakes easier to detect, decisions easier to review, and results
easier to understand and reproduce.


## The central question

This training is organized around one question:

> How do we turn scientific code into a trustworthy, understandable, and
> reproducible computational experiment?

The core route follows a single narrative:

**Readable code → traceable changes → meaningful tests → documented interfaces
→ interpretable data → automated checks → reproducible results**

The [running temperature-analysis example](running_example.md) revisits this
route throughout the training.  Each topic contributes a different kind of
evidence; no individual tool or practice establishes trust on its own.


## Do these practices still matter with agentic AI?

Agentic tools can inspect repositories, generate and modify code, run commands,
and perform development tasks much faster than a person working alone.
However, generating code is not the same as establishing that the code is
understandable, correct, scientifically valid, or reproducible.

These practices may become more important as more work is delegated:

* readable code makes generated changes reviewable;
* version control makes large changes inspectable and reversible;
* static analysis and tests can expose some plausible but incorrect changes;
* documentation makes units, assumptions, and limitations explicit;
* automation ensures that generated code is subjected to normal project
  checks; and
* reproducibility connects the resulting computation to an identifiable
  scientific workflow.

An agent may help perform any of these activities, but it does not remove the
need for them.  It may produce an incorrect equation, unit conversion,
tolerance, interface, or interpretation that still looks convincing.  The
researcher and project remain responsible for the evidence used to accept a
change and for the scientific conclusions drawn from it.

> **Agentic AI increases the rate at which software can change; best practices
> provide the evidence needed to trust those changes.**

The principles above are independent of any particular AI product.  Current
tools can be considered later using the same [tool-selection
criteria](tools/choosing_tools.md) as other development tools.  The
[agentic AI chapter](agentic_ai.md) develops the scientific, operational, and
reproducibility implications without depending on one product.


## Opening discussion

Choose a computational result from your own work and consider:

1. What would another researcher need before they could trust the result?
2. Which part of the computation would be hardest to explain or reproduce?
3. If a person or an AI agent changed the code today, what evidence would tell
   you that the result was still valid?

Keep that example in mind during the training.  The aim is not to adopt every
practice at once, but to identify which missing evidence creates the greatest
risk for work that matters to you.


## Scope of this training

The training concentrates on transferable concepts and scientific motivation.
Examples and tool recommendations support several programming languages, but
the session is not an exhaustive tutorial for Git, testing frameworks,
continuous-integration platforms, or AI coding tools.

Detailed mechanics belong in the relevant [further
training](training.md).  Here, the purpose is to recognize the practices,
understand the evidence they provide, and decide how they apply to your own
scientific software.

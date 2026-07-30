# Choosing development tools

There is no universally best collection of tools for scientific software.
Appropriate choices depend on the problem being solved, the programming
language, the people maintaining the project, and the systems on which the
software must run.

Start with a need rather than with a tool.  A new tool is useful only if it
solves a real problem without adding more maintenance effort than it saves.


## Selection criteria

When evaluating a tool, consider the following questions.

### What problem should it solve?

Be specific about the desired outcome.  "Improve quality" is vague; "format
every file consistently before review" or "detect changes to a numerical
result" is easier to evaluate.

Also check whether an existing tool already provides the required capability.
Several overlapping tools can produce contradictory reports and make the
development workflow harder to understand.


### Does it fit the project?

The tool must support the project's

* programming language and language version;
* operating systems and hardware platforms;
* build and package-management approach;
* editor, command-line, and continuous-integration workflows; and
* deployment environment, including any restrictions imposed by an HPC system.

A tool that works well on a laptop but cannot run in the project's continuous
integration or HPC environment may not be a good project-wide choice.


### Can the team use and maintain it?

Consider the learning curve, quality of the documentation, release activity,
and size of the user community.  Existing experience in the team or
organization is valuable because it reduces setup and support costs.

Prefer tools whose configuration can be stored in the repository.  A
repository-local configuration makes expectations visible to contributors and
allows local and continuous-integration checks to use the same settings.


### Can it be automated and reproduced?

A development tool should ideally

* have a non-interactive command-line interface;
* return a meaningful exit status;
* produce output that is useful to both people and continuous integration;
* allow its version and configuration to be recorded; and
* behave consistently enough that contributors obtain comparable results.

For performance tools, reproducibility also requires recording the workload,
machine, compiler or interpreter, libraries, and relevant runtime settings.


### What is its total cost?

The purchase price is only one possible cost.  Also consider installation,
configuration, training, maintenance, execution time, license restrictions,
and the work required to update continuous-integration or deployment
environments.

For a small project, a simple tool with fewer features may be a better choice
than a more capable tool that requires substantial maintenance.


## Decision table

The table below starts from common project needs.  It points to questions that
help narrow the choice and to the pages containing candidate tools.

| Need | Questions to ask | Candidate lists |
|------|------------------|-----------------|
| consistent source formatting | Is there a standard formatter for the language? Is its output deterministic? Can editors and CI run it? | language-specific pages |
| early defect detection | Does the tool check likely correctness problems, style, types, or all three? Does it complement rather than duplicate the formatter? | [static analysis](../static_analysis.md) and language-specific pages |
| automated behavior checks | Does the framework support the required scientific assertions, fixtures, parameterized cases, and test granularity? | [testing](../testing/index.md) and language-specific pages |
| agent-assisted repository work | Which files, commands, data, networks, and services may the tool access? Where is project context processed? How are changes reviewed and reversed? | [agentic AI concepts](../agentic_ai.md) and [current tools](agentic_ai.md) |
| automated pull-request feedback | Does the service review every relevant change? Can findings be explained, dismissed, and rechecked after updates? Which checks remain the responsibility of CI and human reviewers? | [agentic AI concepts](../agentic_ai.md), [current tools](agentic_ai.md), and [continuous integration](../continuous_integration.md) |
| repeatable builds | Which languages must be compiled? Are multiple compilers, platforms, build types, or optional dependencies required? | [general tools](general.md) and compiled-language pages |
| dependency and environment management | Are dependencies language-specific or system-level? Are compiled scientific libraries involved? Is a lockfile or HPC integration required? | [general tools](general.md) and language-specific pages |
| useful documentation | Is the need a tutorial, API reference, project website, or all three? Can examples and links be checked automatically? | [documentation](../documentation.md) and [general tools](general.md) |
| performance diagnosis | Is the suspected issue CPU time, memory, I/O, communication, synchronization, or accelerator use? Must parallel execution be supported? | [optimization](../optimization.md) and language-specific pages |
| reproducible multi-step work | Is a script sufficient, or does the workflow need dependency tracking, retries, parallel execution, and portability between systems? | [reproducibility](../reproducibility.md) and [general tools](general.md) |
| a portable runtime environment | Is the target a workstation, continuous integration, cloud system, or HPC cluster? Are root privileges or accelerators involved? | [general tools](general.md) |
| publication and attribution | What must be licensed, archived, cited, and assigned a persistent identifier? | [deployment](../deployment.md) and [general tools](general.md) |

The categories are not mutually exclusive.  For example, a formatter changes
layout while a static analyzer searches for suspicious code; they may be
complementary.  A build system describes how compiled code is built, while a
package manager obtains dependencies.  Continuous integration does not replace
tests: it provides an environment in which the tests and other checks are run
automatically.


## A lightweight selection process

Use the following process rather than trying to compare every available tool.

1. Define the problem and the minimum capability required.
2. Write down hard constraints such as language, platform, HPC environment,
   license, and continuous-integration support.
3. Select two or three plausible candidates from the relevant tool pages.
4. Try them on a representative part of the project.
5. Compare usefulness, false reports, configuration effort, runtime, and team
   experience.
6. Record the decision and configuration in the repository.
7. Automate the tool only after the team agrees on how it should be used.

It is reasonable to decide that no additional tool is needed.  Every tool added
to a project becomes another dependency that must be understood and maintained.


## Short activity

Consider the following project.

> Three researchers maintain a Python analysis that uses compiled numerical
> libraries.  It runs on laptops and an HPC cluster.  Changes are reviewed in a
> shared repository, and the team wants to detect incorrect results before
> changes are merged.

In small groups, take five to ten minutes to answer these questions.

1. Which tool *categories* does the project need immediately?
2. Which categories could wait until the project becomes larger or develops a
   demonstrated performance problem?
3. Select one or two candidates for each immediate need from the
   [Python](Python.md) and [general](general.md) tool pages.
4. Justify each candidate using at least two selection criteria.
5. Identify one constraint that should be checked on the HPC system before
   adopting the tool.

There is no single correct toolchain.  A good answer distinguishes immediate
needs from optional tooling and explains the trade-offs rather than merely
listing popular tools.


## Candidate lists

Candidate tools are organized into

* [programming language-agnostic tools](general.md);
* [agentic software-development tools](agentic_ai.md);
* tools for [C](C.md);
* tools for [C++](C-plus-plus.md);
* tools for [Fortran](Fortran.md);
* tools for [Rust](Rust.md);
* tools for [Julia](Julia.md);
* tools for [Python](Python.md); and
* tools for [R](R.md).

These lists are starting points, not endorsements.  Tool capabilities and
maintenance status can change, so verify the current documentation before
adopting one for a project.

# Version control

Version control is a very important aspect of software development.  In short,
it allows to answer the following questions.

  * What was changed?
  * When was it changed?
  * Who made the change?
  * Why was the change made?

Using a version control system you can compare versions of your code, and if
necessary, revert to a previous version.

In scientific computing, source code is part of the experimental method: even a
small change can affect the results and potentially the conclusions.  Version
control lets you experiment safely, compare implementations, restore a
known-working version, and identify the exact code version used to produce a
result.  Recording that version with the results provides an important link in
the chain of scientific provenance.

Version control alone does not make a computation reproducible: the input data,
parameters, software environment, and workflow must also be recorded.  However,
it makes the evolution of the source code traceable.

A short [version-control demonstration](version_control_demo.md) illustrates
these benefits by introducing a bug into a small scientific program, inspecting
the change, and recovering the known-working version.

It is good practice to host your repositories on a service such as
[GitHub](https://github.com/), [GitLab](https://gitlab.com) or a hosting service
provided by your organization.  These environments all facilitate collaboration
on software projects and make it easy to work in teams.

Participants who want hands-on practice with Git commands and hosting services
can continue with the dedicated [Version control with
Git](https://gjbex.github.io/Version-control-with-git/) training.

<!--
Keep Git command instruction in Version-control-with-git.  This page should
remain focused on motivation and scientific relevance.
-->

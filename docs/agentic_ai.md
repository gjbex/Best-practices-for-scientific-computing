# Agentic AI and scientific software

Agentic AI tools combine a generative model with access to context and tools.
Depending on the system and the permissions it is given, an agent may inspect a
repository, search documentation, edit files, run commands, execute tests, and
iterate on the results.

This is a substantial change from asking a chatbot for a code fragment.  The
agent can act on a development environment and pursue a multi-step goal.
Greater capability can save time, but it also increases the amount and impact
of work that must be reviewed.

This chapter concerns the durable principles for using such tools in scientific
software.  Current products and interfaces are kept on the separate, explicitly
dated [agentic tools page](tools/agentic_ai.md).


## A spectrum of assistance

The boundary between an assistant and an agent is not exact.  It is more useful
to ask what a tool can observe and do.

| Form of assistance | Typical interaction | Main responsibility for action |
|--------------------|---------------------|--------------------------------|
| code completion | suggests the next lines while a person edits | the person accepts and integrates each suggestion |
| conversational assistance | explains code or proposes a fragment in response to a question | the person transfers and adapts the answer |
| agentic assistance | inspects context, changes files, runs tools, and responds to their output | the person defines scope, permissions, and acceptance evidence |

Tools may support several of these modes.  An interactive planning mode can be
less autonomous than a non-interactive agent with permission to edit files,
execute commands, access a network, and interact with external services.
Evaluate the actual operating mode rather than relying on the product label.


## What agents can contribute

Agentic tools can help with work such as

* explaining an unfamiliar repository or execution path;
* drafting documentation and examples;
* generating initial tests from an explicit requirement;
* applying repetitive, well-scoped changes;
* running formatters, static analysers, builds, and tests;
* investigating an error using logs and source code;
* comparing an implementation with documented expectations; and
* preparing a change for human review.

The strongest tasks have a clear scope and a cheap way to check the result.
For example, "rename this configuration key and make the existing tests pass"
has a more objective completion criterion than "improve the scientific
quality of this simulation."


## Why the existing practices still matter

Agentic AI does not replace the evidence developed in this training.  It makes
that evidence more important because software can change more quickly and
across more files.

**Readable code → traceable changes → meaningful tests → documented interfaces
→ interpretable data → automated checks → reproducible results**

Each stage constrains or verifies agentic work:

* **Readable code** lets a researcher understand the accepted implementation
  rather than trusting an explanation generated alongside it.
* **Traceable changes** show exactly what the agent changed and make those
  changes reviewable and reversible.
* **Meaningful tests** challenge generated code with known results, invariants,
  bounds, and relations grounded in the scientific problem.
* **Documented interfaces** give both people and agents explicit information
  about units, parameters, data schemas, assumptions, and failure conditions.
* **Interpretable data** reduces the risk that values or files are used without
  their scientific meaning.
* **Automated checks** apply agreed safeguards consistently, regardless of who
  or what produced a change.
* **Reproducible results** connect the accepted computation to its inputs,
  configuration, code state, command, and environment.

An agent can help create or run these checks, but it cannot use its own output
as independent evidence that the output is correct.


## Scientific risks

Generated scientific code may be syntactically valid, readable, and plausible
while still containing an incorrect

* equation, constant, sign, unit conversion, or index convention;
* numerical method, convergence criterion, tolerance, or initial condition;
* interpretation of a data column, quality flag, or missing value;
* statistical test, uncertainty calculation, or random-sampling procedure;
* parallel decomposition, reduction, synchronization, or boundary exchange; or
* scientific explanation of what a computed result establishes.

The model may also invent an API, option, reference, package, or capability.
Checking that code runs is necessary but insufficient: a program can execute
successfully and produce a convincing wrong answer.

Scientific review therefore requires domain knowledge and evidence external to
the generated implementation, such as an analytical result, a trusted small
case, a conservation law, a convergence study, or independently validated
reference data.


## Operational and governance risks

An agent that can execute tools acts with some subset of the user's authority.
It may be able to modify files, delete results, install dependencies, access
credentials, submit jobs, contact network services, or change external systems.

Before using an agent, establish

* which files and directories it may read or modify;
* which commands and external tools it may run;
* whether proposed actions require approval;
* whether source code, prompts, logs, or data leave the local system;
* which provider and organizational data-use policies apply;
* whether the repository contains confidential, personal, export-controlled,
  licensed, or unpublished material; and
* how accidental or inappropriate changes can be recovered.

Use the least privilege sufficient for the task.  Planning or review may need
only read access.  Editing usually needs access to one working tree, not a home
directory, credential store, production system, or unrelated project.


## Scientific and HPC environments

An agent used with an HPC project may see module configurations, scheduler
commands, storage locations, allocation identifiers, and credentials that are
not present in an ordinary workstation project.

Check institutional policy before exposing source code, job output, or
research data to an external service.  Also consider that

* login nodes may prohibit expensive builds, tests, or analyses;
* compute nodes may have restricted or no network access;
* an agent should not submit or cancel jobs without an explicitly defined
  scope;
* generated commands may request inappropriate resources or consume a shared
  allocation;
* local test environments may not reproduce MPI, accelerator, filesystem, or
  scheduler behaviour; and
* credentials and private keys should not be included in prompts, logs,
  repository instructions, or test fixtures.

Repository guidance can describe the approved build, test, and submission
workflow, but technical controls and site policy remain necessary.  An
instruction file is guidance, not a security boundary.


## A defensible working pattern

Treat agentic work as a change proposed by a capable but fallible collaborator.

1. **Start from a controlled state.** Use version control and separate unrelated
   changes so that the agent's work can be identified and reversed.
2. **Define the task and boundaries.** State the intended behaviour, files in
   scope, constraints, and actions that require confirmation.
3. **Define acceptance evidence.** Identify the tests, reference results,
   invariants, documentation, and review needed before accepting the change.
4. **Grant limited access.** Prefer read-only or workspace-scoped operation and
   approve broader actions deliberately.
5. **Inspect the changes.** Review the actual difference, including dependency,
   configuration, test, data, and documentation changes.
6. **Run independent checks.** Use the project's normal formatter, static
   analysis, build, software tests, scientific tests, and documentation checks.
7. **Review the science.** Check equations, units, assumptions, tolerances,
   data meaning, and conclusions rather than only software structure.
8. **Record the accepted result.** Commit the reviewed change and preserve the
   inputs, configuration, environment, and provenance required by the
   computation.

Repository-local guidance can help an agent find the correct commands and
conventions.  Keep such guidance concise, version controlled, and aligned with
the checks that the project actually runs.


## Reproducibility and provenance

Agentic work is not necessarily reproducible by replaying the same prompt.
Models, tools, context, services, and generated choices can change, and the
interaction may include intermediate decisions that were never written down.

The durable record should therefore be the reviewed scientific artifact and
its evidence:

* the accepted source-code difference and commit;
* tests and their scientifically justified expectations;
* input data, parameters, configuration, and environment information;
* relevant tool or model identity when it materially affects interpretation;
* commands or workflows used to produce the result; and
* human decisions that explain why the change was accepted.

A conversation transcript can provide useful supplementary provenance, subject
to privacy and retention policy, but it should not be the only record of the
scientific method.


## Choosing an agentic tool

Do not start from a product name.  Start from the task, the evidence needed to
accept its result, and the access that the tool would require.

In addition to the general [tool-selection
criteria](tools/choosing_tools.md), consider

* local versus remote execution and data processing;
* filesystem, command, network, and external-service permissions;
* approval, sandboxing, audit, and recovery mechanisms;
* support for repository-local instructions and existing development tools;
* interactive versus unattended operation;
* organizational policy, licensing, cost, and account requirements; and
* whether the tool works in the project's workstation, CI, and HPC
  environments.

The dated [agentic tools page](tools/agentic_ai.md) lists current candidates
for comparison.  It is a starting point, not a substitute for checking current
upstream documentation and institutional policy.

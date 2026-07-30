# Conclusions

The training began with one central question:

> How do we turn scientific code into a trustworthy, understandable, and
> reproducible computational experiment?

There is no single tool or practice that provides the answer.  Trust is built
from complementary evidence gathered throughout the development and execution
of the software.


## Return to the narrative

**Readable code → traceable changes → meaningful tests → documented interfaces
→ interpretable data → automated checks → reproducible results**

The stages support one another:

* readable code makes scientific intent and implementation choices easier to
  inspect;
* traceable changes show how and why the computation evolved;
* meaningful tests challenge both software behaviour and scientific
  expectations;
* documented interfaces state what the program, configuration, and data mean;
* interpretable data retains units, metadata, provenance, and structure;
* automated checks apply selected safeguards consistently; and
* reproducible results connect an output to the inputs, decisions, code, and
  environment that produced it.

The absence of one link can weaken the others.  A test is hard to interpret if
the units are undocumented; a recorded code version is insufficient if the
input and configuration are unknown; and an automated check is only useful if
it tests a meaningful expectation.


## Agentic AI changes the workflow, not the evidence

Agentic tools can accelerate reading, writing, reviewing, testing, and
documenting software.  They can also produce more changes, more quickly, than
a researcher could inspect informally.

Generated code should therefore enter the same workflow as any other change:
inspect the difference, run relevant static checks and tests, review the
scientific assumptions, and record the accepted result.  Neither a confident
explanation nor a clean-looking implementation is a substitute for evidence.

The enduring question is not who or what typed the code.  It is whether the
computational result is supported by an inspectable and defensible process.
The [agentic AI chapter](agentic_ai.md) provides a fuller working pattern for
applying this principle.


## Start with the next defensible step

Improving an existing project need not begin with a complete toolchain.  Choose
one result or workflow that matters and strengthen its weakest link:

1. make units, constants, and scientific decisions visible in the code;
2. place the code under version control and record why consequential changes
   are made;
3. add one known result, invariant, bound, or relation that could reveal an
   incorrect computation;
4. document the inputs, configuration, outputs, assumptions, and limitations;
5. preserve data meaning through explicit formats, metadata, and validation;
6. automate a small set of fast, agreed checks; and
7. record enough of the code, data, parameters, command, and environment to
   connect a result to its computational experiment.

Prefer a small practice that the project will maintain over an elaborate
setup that contributors do not understand or use.


## Closing discussion

Return to the computational result considered at the start of the training:

1. Which part of its evidence chain is already strong?
2. Which missing link presents the greatest scientific or maintenance risk?
3. What is one change you can realistically make in the next week?
4. How would you verify that this change improved the trustworthiness of the
   result?

The [optional running-example
exercise](running_example/exercise/README.md) provides a self-paced way to
practise the complete narrative.  The [tool-selection
guidance](tools/choosing_tools.md) can help choose an appropriate implementation
for a particular language and environment, while [further
training](training.md) develops individual topics in more depth.

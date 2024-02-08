# Documentation best practices

When you consider using a new software library, you probably like to start by
looking at some example code. You'll do a few experiments of your own, based
on those examples.  Once you start using the new library for non-trivial
applications, you will most likely have to refer to the reference guide.  All
this documentation is a great help if its quality is good.

If you want to deliver high quality software, the documentation is a very
important aspect of the development process.  You can distinguish between two
types of documentation: tutorial style and reference documentation.

## Types of documentation

Broadly speaking, we distinguish two types of documentation, tutorials and
reference guides. They serve different purposes, and hence are complementary.

*Tutorials* will typically illustrate a number of use cases, presented as a
narrative. It is more of a high-level overview of the software project.  Such
documentation is typically written separately from the source code, and a
convenient format is markdown. We will discuss MkDocs, a tools to generate nice
looking documentation based on this format.

A *reference guide* serves a different purpose. It is intended to get
low-level information on the contents of the library. It should be easy to
navigate, so that one can view the definition of a datatype by clicking it when
it occurs in the signature of a function. Hence this type of documentation
integrates closely with the source code itself. If the latter changes, so
should the former.


## Pitfalls

When working on a software project, one of the main pitfalls is neglecting
documentation. Many developers don't particularly enjoy writing documentation,
and hence postpone it. The more classes and functions to be documented, the
worse the tasks seems to be, and the larger the probability that it will never
happen.

Getting into the habit of immediately writing the reference documentation for
each module, data type or function as you code is certainly a "best practice".
Although it may seem to slow you down while coding, that is not necessarily a
bad thing.

However, even when documentation is diligently written while coding, it has to
be kept up to date when code changes.  It is all too easy to forget to update
the documentation when the signature of a function is modified. Inaccurate
documentation is almost worse than no documentation since it is likely to cause
serious software defects.


## What to document?

The first question to answer is, what do you need to document since a software
project has many artifacts.

### Documenting functions

Consider the documentation of a function or a subroutine for instance. You
would write a description of what the it does, which argument it takes, and what
the return type is. However, you would also add the assumptions the procedure
makes about the values its arguments can have.

Such assumptions are called preconditions. By way of example, consider a
function that takes a temperature as an argument. An important aspect is the
units it expects the temperature to be specified in. Will that be degrees
Celsius, or Fahrenheit, or Kelvin?  In case it is degrees Celsius, it doesn't
make sense to pass a value to the function that is less than -273.15 degrees
Celsius. On the other hand, if it is Kelvin, the value should be positive.
Needless to say that if you pass a temperature expressed in Kelvin to a function
that expects degrees Celsius as a unit, the results will be wrong.

This example illustrates an important point: the function documentation should
clearly specify its expectation about the arguments that you pass to it. In our
example, that would be the units of the temperature, but also the valid range of
values. These restrictions are often called preconditions, and they constitute a
contract between the user of the procedure and its author.

The contract, i.e., the precondition, says that if the user of the function
supplies arguments that fulfill all the preconditions, then the author
guarantees that the function will return proper results.

When considering values returned by a function, you have to consider similar
restrictions. What are the units of the return value and what is the range of
values that would make sense? This amounts to postconditions, again a contract
between the function's author and its user.

The contract, i.e., the postcondition, specifies that the user of the function
can rely on it to return a value that fulfills all the conditions if she calls
it correctly.

When a procedure has side effects, i.e., it modifies one of its arguments, this
should be stated as well.  The "principle of least astonishment" is very useful
in software development.

Conversely, when passing an argument to a function that is not changed at all,
that constitutes an invariant. Although it may be useful to state this in the
documentation, it is far better practice to make that explicit by declaring it
constant.

The concepts of preconditions, postconditions, and invariants were introduced
in the ["design by contract"](https://en.wikipedia.org/wiki/Design_by_contract)
paradigm, pioneered by Bertrand Meyer in 1986.

If you make it part of your coding process to immediately provide the
documentation when writing a procedure, it will actually help you since you have
to make your assumptions explicit, and hence may discover potential flaws.

Documenting failure is very important as well. Can the function generate an
error?  What is the semantics of these errors?  Again, this is an application of
the "principle of least astonishment". The user of your functions will be aware
of potential failure, and can code to deal with it appropriately.


### Documenting data types

For data types, the semantics of the type should be documented. What does a
variable of the type represent? Of course, the type name should be chosen so
that this is clear, but it doesn't hurt to explain this more formally in the
documentation as well.

For each field, you should document its type, semantics, and, if applicable,
the units that are expected.

When doing object oriented programming, the documentation of methods is similar
to that of functions.


### Documenting modules

Code is typically aggregated according to functionality in modules for separate
compilation or importing.  Hence this aggregation has a purpose, and you should
document that as well. What is the overall purpose of the module?  Another
question that you can answer in module documentation is the interaction between
various components. How can the output of one function be used as the input for
another, are the various functions independent, or should they be called in a
certain order?

As an example, if you have a function that initializes a data structure, a few
that manipulate such data structures, and a finalization function that releases
the resources in that data structure, then the module documentation should
probably mention that you should

  1. call the initialization function to get a valid data structure;
  1. call functions that use the data structure; and
  1. call the finalization function to avoid memory leaks.

At this level, you may want to add some example code of using the software
components in that module. How do you call the procedures, how can you use the
return values, what are the use cases? This type of documentation could also be
maintained at the project level, though.


### Documenting projects

This is typically high-level documentation in the form of a tutorial with use
cases and code samples. It should of course contain a link to the reference
documentation.

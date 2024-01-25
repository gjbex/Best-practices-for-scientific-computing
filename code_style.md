# Coding best practices: reading material

A number of very simple things go a long way towards improving your code
substantially. For good programmers, they are second nature, and you should
strive to make them a habit.

This text tries to be programming language-agnostic, and code fragments
will be presented in several programming languages such as C, C++, Fortran
and Python.  However, even if you don't master these languages, the code
fragments should be easy enough to understand.

Although each programming languages has some specific best practices, many
are applicable to any programming language.  This is what this text focusses
on.  We also provide a list of references to best practices specific to
various programming languages, and we encourage you strongly to read those as
well.

In this section, we will use the term function in a very broad sense, simply
to keep the text easy to read. In the context of Fortran, a function refers
to a program unit, any procedure, either a function or a subroutine. It also
refers to a method defined in a class. In the context of Python and C++, we
will use the term function for methods as well.

Similarly, we use the term variable for constants, and also for attributes of
objects and classes, whenever that doesn't lead to confusion.


## Format your code nicely

To quote Robert C. Martin, *"Code formatting is about communication, and
communication is the professional developer’s first order of business".*

All programming languages have one or possibly multiple conventions about
how to format source code. For example, consistent indentation of code helps
considerably to assess the structure of a function at a glance. For
multi-level indentation, always use the same width, e.g., multiples of four
spaces.

The convention you have to use is often determined by the community you are
working with, such as your co-workers.  It is best to stick to that convention,
since coding is communicating. If no convention is established, consider
introducing one.  The one which is prevalent in the programming language
community is most likely to be your best choice.

For several programming languages there are tools to automatically format
your code so that it adheres to a convention.  It is considered good practive
to use such tools if they are available, and even to make them part of your
development pipeline, either as git pre-commit hooks, or as part of a more
substantial CI/CD setup on GitHub or GitLab.

Another issue is code formatting is the maximum number of characters on a
line.  Some guidelines for programmers have very strong opinions on that,
while other are more tolerant.

Since many editors will automatically display a view on your code with
lines wrapped to the length that can be displayed on the screen, that might
not seem an issue, but it can be argued that this makes the code harder to
read.  If you switch that off, you will have a view on your code were some
lines are truncated, again a very unpleasant and potentially confusing
situation.

Personally I like the maximum line length to be 80 characters, since that
will guarantee it can be displayed without the need to wrap it, even when
displaying multiple editor windows side-by-side.  Again, code formatters
can enforce this and properly wrap the code for you automatically.

Whichever convention you follow, be consistent!


## Use language idioms

Linguists use the term "idiom" for an expression that is very specific to a
certain language and that cannot be translated literally to another. For
instance, the English idiom "it is raining cats and dogs" would translate to
"il pleut des cordes" in French.  The corresponding idiom in French is
completely unrelated to its counterpart in English. Mastering idioms is one of
the requirements for C1 certification, i.e., to be considered to have a
proficiency close to that of native speakers.

We observe a similar phenomenon for programming languages. Some syntactic
constructs are typical for a specific programming language but, when
translated one-to-one into another language, lead to code constructs that are
unfamiliar to programmers who are proficient in that language.  The code
fragments below illustrate this for Fortran and C.

Although you could write line 4 of the C function below in this way, you most
likely wouldn't since it is not idiomatic C.

~~~~c
int factorial(int n) {
    fac = 1;
    for (int i = 2; i <= n; i++)
        fac = fac*i;
    return fac;
}
~~~~

The idiomatic formulation of line 4 would be `fac *= i`.

In Fortran for example, you would write

~~~~fortran
REAL, DIMENSION(10) :: a
...
a = value
~~~~

rather than

~~~~fortran
integer :: i
real, dimension(10) :: a
...
do i = 1, 10
    a(i) = value
end do
~~~~

Using idioms, i.e., expressions that are particular to a (programming)
language, will make your code much easier to interpret correctly by
programmers that are fluent in that language.

In the spirit of Robert C. Martin's quote: it is all about communication.

However, there are sometimes different reasons as well.  If we consider the
following Python code that uses the numpy library, we can observe a marked
performance difference when comparing the two code fragments below.

```python
   a = np.emptylike(b)
   for i in range(b.shape[0]):
       for j in range(b.shape[1]):
           a[i, j] = np.sqrt(b[i, j])
```
versus
```python
    a = np.sqrt(b)
```

The second form is more idiomatc, but it will also substantially outperform
the first fragment.  MATLAB users will be aware of this difference as well.


## Choose descriptive names

In a way, programming is storytelling. The data are the protagonists in the
story, and the functions are the actions they take, or what happens to them.
Hence variable names should be nouns and functions names should be verbs. If a
function returns a property, it should be phrased as a question.

Any editor worth its salt provides completion, so you can't argue in favour of
short but less descriptive names to save typing. A long but descriptive name is
just hitting the tab key away.

Choosing descriptive names for variables and functions is another aspect that
can make reading your code much easier. Consider the following pseudo-code
fragment, and although I'll grant that it is something of a caricature, I've
seen some in the wild that are not significantly better.

~~~~python
f = open(fn, 'r')
for i in f:
    x = get(i)
    if condition(x):
        a = compute(x)
        if a < 3.14:
            do_something(a)
f.close()
~~~~

A key principle of good software design is that of the *least surprise*.
Choosing appropriate names for our variables and functions helps a lot in this
respect.

When it comes to programming languages, there is a very clear bias: all those
I'm aware of have keywords defined in English.  Hence I would argue that code
that also uses English variable and function names is easier to read.  This saves
you from continuously, although unconsciously, to switch from one natural
language to another.

It may seem convenient, or even more natural to choose variable names in your
native language, but that leads to more "surprises" when reading the code since
you would also expect keywords in your native language to form actual sentences.

Moreover, communicating about your code with others that don't speak your
language will be just that bit harder.

Just to put things in context: sometimes short variable names are perfectly
adequate.  For instance, trivial variable using in an iteration to index an
array are conventianally called `i`, `j` and so on.  This is perfectly fine,
and unless you have a good reason to choose different names, the "default"
names will even help others to understand your code.

Also domain specific variables can have short names, using, e.g., `T` to
denote the temperature, or `t` for time.  This particular example would of
course break for programming languages that are case-insensitive, e.g.,
Fortran.

Note that these last remarks in no way contradicts the message of this
section: `T` and `t` are very desciptive for developers in the domains
where this notation is used.


## Keep it *simple*

Ideally, code is simple.  A function should have two levels of indentation at
most.  This is advice you'll find in the literature on general purpose
programming. Although this is good advice, there are some caveats in the
context of scientific computing.

However, the gist is clear: code is as simple as possible, but not simpler.

Even for scientific code, a function has no more lines of code than fit
comfortably on your screen. It is all too easy to lose track of the semantics
if you can't get an overview of the code. Remember, not everyone has the
budget for a 5K monitor.

If you find yourself writing a very long code fragment, ask yourself whether
that is atomic, or whether the task it represents can be broken up into
sub-tasks. If so, and that is very likely, introduce new functions for those
sub-tasks with descriptive names. This will make the narrative all the easier
to understand.

A function should have a single purpose, i.e., you should design it to do one
thing, and one thing only.

For function signatures, simplicity matters as well.  Functions that take many
arguments may lead to confusion.  In C and C++, you have to remember the order
of the function arguments.  Accidentally swapping argument values with the same
type in a function call can lead to interesting debugging sessions.

The same advice applies to Fortran procedures or Python functions, keep the
number of arguments limited.  However, both Fortran and Python support using
keyword arguments, a nice feature that makes your code more robust.  Consider
the following procedure signature:

~~~fortran
real function random_gaussian(mu, sigma)
    implicit none
    real, intent(in) :: mu, sigma
    ...
end function random_gaussian
~~~

You would have to check the documentation to know the order of the function
arguments.  Consider the following four function calls:

  1. `random_gaussian(0.0, 1.0)`: okay;
  1. `random_gaussian(1.0, 0.0)`: not okay;
  1. `random_gaussian(mu=0.0, sigma=1.0)`: okay;
  1. `random_gaussian(sigma=1.0, mu=0.0)`: okay.

The two last versions of this call are easier to understand, since the meaning
of the numbers is clear.  Moreover, since you can use any order, it eliminates
a source of bugs.

Unfortunately, neither C nor C++ support this feature.


## Limit scope

Many programmers will declare all variables at the start of a block, or even at
the start of a function's implementation. This is a syntax requirement in C89
and Fortran.  However, C99, C++, R and Python allow you to declare variables
anywhere before their first use. Since the scope of a variable starts from its
declaration, and extends throughout the block, that means it is in fact too
wide.

Limiting the scope of declarations to a minimum reduces the probability of
inadvertently using the variable, but it also improves code quality: the
declaration of the variable is at the same location where the variable is
first used, so the narrative is easier to follow.

In C++ this may even have performance benefits since a declaration may trigger
a call to a potentially expensive constructor.

Fortran requires that variables are declared at the start of a compilation
unit, i.e., `program`, `function`, `subroutine`, `module`, but Fortran 2008
introduced the `block` statement in which local variables can be declared.
Their scope doesn't extend beyond the `block`. Modern compilers support this
Fortran 2008 feature.

Note that Fortran still allows variables to be implicitly typed, i.e., if you
don't declare a variable explicitly, its type will be `integer` if its starts
with the characters `i` to `n`, otherwise its type will be `REAL`.

Consider the code fragment below. Since the variables were not declared
explicitly, `i` is interpreted as `INTEGER` and `total` as `real`. However, the
misspelled `totl` is also implicitly typed as `REAL`, initialised to `0.0`,
and hence the value of `total` will be `10.0` when the iterations ends, rather
than `100.0` as was intended.

~~~~fortran
integer :: i
real :: total
do i = 1, 10
    total = totl + 10.0
end do
~~~~

To avoid these problems caused by simple typos, use the `implicit none`
statement before variable declarations in `program`, `module`, `function`,
`subroutine`, and `block`, e.g,

~~~~fortran
implicit none
integer :: i
real :: total
do i = 1, 10
    total = totl + 10.0
end do
~~~~

The compiler would give an error for the code fragment above since all
variables have to be declared explicitly, and `totl` was not.

Limiting scope of of declarations extends to headers files that are included
in C/C++.  It is recommended not to include files that are not required.  Not
only will it pollute the namespace with clutter, but it will also increase
build times.

This advice is even more important for Python `import` statements.  While the
performance impact for C and C++ is limited to compile time, that of
unnecessary imports of Python modules will increase the run time of your
application.


### Multithreading

When developing multi-threaded C/C++ programs using OpenMP, limiting the scope
of variables to parallel regions makes those variables thread-private, hence
reducing the risk of data races. We will discuss this in more detail in a later
section.  Unfortunately, the semantics for the Fortran `block` statement in an
OpenMP do loop is not defined, at least up to the OpenMP 4.5 specification.
Although `gfortran` accepts such code constructs, and seems to generate code
with the expected behavior, it should be avoided since Intel Fortran compiler
will report an error for such code.

This recommendation is [mentioned](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Res-scope) in the C++ core guidelines.


### Namespaces and imports

In C++, you can importing everything defined in a namespace, e.g.,

~~~~c++
using namespace std;
~~~~

Although it saves on typing, it is better to either use the namespace prefix
explicitly, or use only what is required, e.g.,

~~~~c++
using std::cout;
using std::endl;
~~~~

In Fortran it is also possible to restrict what to use from modules, e.g.,

~~~~fortran
use, intrinsic :: iso_fortran_env, only : REAL64, INT32
~~~~

The `only` keyword ensures that only the parameters `REAL64` and `INT32` are
imported from the `iso_fortran_env` module.

Note that the `intrinsic` keyword is used to ensure that the compiler supplied
module is used, and not a module with the same name defined by you.

Similar advice applies to Python, `from math import *` is considered bad
practice since it polutes the namespace.


## Be explicit about constants

If a variable's value is not supposed to change during the run time of a
program, declare it as a constant, so that the compiler will warn you if you
inadvertently modify its value. In C/C++, use the `const` qualifier, in
Fortran, use `parameter`.

If arguments passed to function should be read-only, use `const` in C/C++ code,
and `intent(in)` in Fortran. Although Fortran doesn't require that you state
the intent of arguments passed to procedures, it is nevertheless wise to do so.
The compiler will catch at least some programming mistakes if you do.

However, this is not quite watertight, in fact, one can still change the value
of a variable that is declared as a constant in C.  Compile and run the
following program, and see what happens.

~~~~c
#include <stdio.h>

void do_mischief(int *n) {
    *n = 42;
}

int main(void) {
    const int n = 5;
    printf("originally, n = %d\n", n);
    do_mischief((int *) &n);
    printf("mischief accomplished, n = %d\n", n);
    return 0;
}
~~~~

In fact, this is [explicitly mentioned](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#Res-casts-const)
in the C++ core guidelines.


## Control access

When defining classes in C++ and Fortran, some attention should be paid to
accessibility of object attributes. An object's state is determined by its
attributes' values, so allowing unrestricted access to these attributes may
leave the object in an inconsistent state.

In C++, object attributes and methods are private by default, while structure
fields and methods are public.  For Fortran, fields in user defined types and
procedures defined in modules are public by default. Regardless of the defaults,
it is useful to specify the access restrictions explicitly. It is good practice
to specify private access as the default, and public as the exception to that
rule.

Interestingly, both Fortran and C++ have the keyword `protected`, albeit with
very different semantics.  In Fortran, `protected` means that a variable defined
in a module can be read by the compilation unit that uses it, but not modified.
In the module where it is defined, it can be modified though.  In C++, an
attribute or a method that is declared `protected` can be accessed from derived
classes as well as the class that defines it.  However, like attributes and
methods declared `private`, it can not be accessed elsewhere.

This is another example where getting confused about the semantics can lead to
interesting bugs.

In summary:

| access modifier | C++                                           | Fortran |
|-----------------|-----------------------------------------------|---------|
| private         | access restricted to class/struct             | access restricted to module |
| protected       | access restricted to class/struct and derived | variables: modify access restricted to module, read everywhere |
| public          | attributes and methods can be accessed from everywhere | variables, types and procedures can be accessed from everywhere |
| none            | class: private, struct: public                | public |

Python has no notion of private attributes or methods, they are alwas public.
However, attributes and methods that are supposed to be private to the class
are by convention prefixed with a `_`.  Note that this is a convention for
programmers, the Python runtime will not enforce this.

In both C++ and Python you can "simulate" Fortran notion of `protected`, i.e.,
read-only attributes by implementing a getter, but no setter.


## Variable initialisation

The specifications for Fortran, C and C++ do not define the value an
uninitialized variable will have. So you should always initialise variables
explicitly, otherwise your code will have undefined, and potentially
non-deterministic behavior. When you forget to initialise a variable, the
compilers will typically let you get away with it. However, most compilers have
optional flags that catch expressions involving uninitialised variables. We
will discuss these and other compiler flags in a later section.

When initialising or, more generally, assigning a value to a variable that
involves constants, your code will be easier to understand when those values
indicate the intended type. For example, using `1.0` rather than `1` for
floating point is more explicit. This may also avoid needless conversions. This
also prevents arithmetic bugs since `1/2` will evaluate to `0` in C, C++ as well
as Fortran.  Perhaps even more subtly, `1.25 + 1/2` will also evaluate to
`1.25`, since the division will be computed using integer values, evaluating to
`0`, which is subsequently converted to the floating point value `0.0`, and
added to `1.25`.

Specifically for C++, I'd strongly encourage you to use universal
initialisation, since narrowing conversion would lead to warnings.  In the code
fragment below, the first local variable `n1` will be initialised to `7` without
any warnings, while the compiler will generate a warning for the initialisation
of `n2`.

~~~~c++
int conversion(double x) {
    int n1 = x;
    int n2 {x};
    return n1 + n2;
}
~~~~

Precision is also an important factor.  If you intend to work purely in single
precision for floating point arithmetic operations, it is important to avoid
accidental type promotion.  For instance, in the code below, the single
precision argument is multiplied by `2.1` in ... double precision since
that is what the compiler assumes you want to do.  When that computation is
done, the result is converted back to a single precision value.

~~~~c
float times2(float x) {
    return 2.1*x;
}
~~~~

In C and C++, a single precision floating value is denoted by `2.1f` to
indicate its type.

~~~~c
float times2(float x) {
    return 2.1f*x;
}
~~~~

In Fortran, you can similarly make the distinction between kinds of literal
numerical values.

~~~~fortran
function times2(x) result(y)
    implicit none
    use, intrinsic :: iso_fortran_env, only : sp => REAL32
    real(kind=sp), intent(in) :: x
    real(kind=sp) :: y
    y = 2.1_sp*x
    return y
end function
```

Similar concerns are important when using `numpy` in Python.


## To comment or not to comment?

Comments should never be a substitute for code that is easy to understand. In
almost all circumstances, if your code requires a comment without which it can
not be understood, it can be rewritten to be more clear.

Obviously, there are exceptions to this rule. Sometimes we have no alternative
but to sacrifice a clean coding style for performance, or we have to add an
obscure line of code to prevent a problem caused by over-eager compilers.

If you need to add a comment, remember that it should be kept up-to-date with
the code. All too often, we come across comments that are no longer accurate
because the code has evolved, but the corresponding comment didn't. In such
situations, the comment is harmful, since it can confuse us about the intentions
of the developer, and at the least, it will cost us time to disambiguate.

The best strategy is to make sure that the code tells its own story, and
requires no comments.

A common abuse of comments is to disable code fragments that are no longer
required, but that you still want to preserve. This is bad practice. Such
comments make reading the code more difficult, and take up valuable screen real
estate.

Moreover, when you use a version control system such as git or subversion in
your development process, you can delete with impunity, in the sure knowledge
that you can easily retrieve previous versions of your files. If you don't use a
version control system routinely, you really should. See the additional material
section for some pointers to information and  tutorials.

You should also bear in mind the distinction between comments and documentation.
Documentation describes how to use your data types and functions to those who
may want to use them.  Comments are intended for the consumption of the
developers only.


## Stick to the standard

The official syntax and semantics of languages like C, C++ andFortran is
defined in official specifications. All compilers that claim compliance with
these standards have to implement these specifications.

However, over the years, compiler developers have added extensions to the
specifications. The Intel Fortran compiler for instance has a very long history
that can trace its ancestry back to the DEC compiler, and implements quite a
number of Fortran extensions. Similarly, the GCC C++ compiler supports some
non-standard features.

It goes without saying that your code should not rely on such compiler specific
extensions, even if that compiler is mainstream and widely available. There is
no guarantee that future releases of that same compiler will still support the
extension, and the only official information about that extension would be
available in the compiler documentation, not always the most convenient source.

Moreover, that implies that even if your code compiles with a specific
compiler, that doesn't mean it complies with the official language
specification. An other compiler would simply generate error message for the
same code, and would fail to compile it.

Using language extensions makes code harder to read. As a proficient programmer,
you're still not necessarily familiar with language extensions, so you may
interpret those constructs incorrectly.

Hence I'd encourage you strongly to strictly adhere to a specific language
specification.  For C there are four specifications that are still relevant,
C89, C99, C11 and C23.  For C++ that would be C++11, C++14, C++17, C++20 and
C++23.  The relevant specification for Fortran are those of 2003, 2008, and 2018.
References to those specifications can be found in the section on additional
material.

For C, you may be interested to read the MISRA C software development guidelines,
a collections of directives and rules specified by the Motor Industry Software
Reliability Association (MISRA) aimed at ensuring safer and more reliable
software systems in the automotive industry.  A reference to this specification
is mentioned in the additional material section.


## Copy/paste is evil

If you find yourself copying and pasting a fragment of code from one file
location to another, or from one file to another, you should consider turning
it into a function.  Apart from making your code easier to understand, it makes
it also easier to maintain.

Suppose there is a bug in the fragment.  If you copy/pasted it, you would have
to remember to fix the bug in each instance of that code fragment.  If it was
encapsulated in a function, you would have to fix the problem in a single spot
only.

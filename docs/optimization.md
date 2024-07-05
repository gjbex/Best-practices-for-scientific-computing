# Optimization

In scientific computing, we potentially care a lot about the performance
of our workflows or applications.  We want to study larger systems, more
complex models, or consider more variations of our problem.  This often
means we need to optimize our code to run faster, use less memory, or
scale to more processors.

In this section, a few general strategies for optimization are discussed.
It is not really possible to go into the details since optimization is
often very problem specific.


## Software stack

If you are using third party software, make sure you are using the
version that is optimized for your system.  This means that the software
is compiled with the right compiler, with the right flags, and with the
right libraries.

Some software environments such as R will always build additional R packages
from source.  If you use a version of R built specifically for your system,
the packages will also be built for your system.  This can make a big
difference in performance.

For Python, you can use the Intel distribution of Python which is optimized
for Intel processors.  Intel also provides optimized versions of numpy,
scipy, and many machine learning-related packages.

For Fortran, C and C++, make sure you are using the right compiler and the
right flags.  For example, the Intel compiler can often generate faster code
than the GNU compiler.  Make sure to compile with optimization flags such as
`-O3` and `-xHost` (Intel) or `-march=native` (GNU).

When using CMake, make sure to set the build type to `Release` to enable
optimizations, i.e., `cmake -DCMAKE_BUILD_TYPE=Release ..`.  CMake will then
pass the appropriate flags to the compiler(s).

If you work on an HPC system, it is very likely that the software stack provided
by the module system is already optimized for the system.  Make sure to use
the modules if you can.


## Your code

If the bulk of the time your workflow takes is spent in your own code, you
you should consider optimizing your code.  This can be done in many ways, use

 * unit for functional tests to ensure that your code works as expected;
 * a profiler to identify bottlenecks in your code;
 * a faster algorithm;
 * a more efficient data structure;
 * parallelism to speed up your code;
 * vectorization to speed up your code;
 * a faster compiler;
 * compiler flags to optimize your code;
 * a faster library;
 * a faster language.

Having tests in place is vital before starting to optimize your code.  You will
want to make sure that your code still works after you have optimized it. You
will find more information on this topic in the section on
[testing](testing.md).


### Profiling

Your first priority is to identify the bottlenecks in your code.  This can be
done with a profiler.  A profiler will tell you where your code spends most of
its time.  You can then focus on optimizing these parts of your code.

You may think that you know where the bottlenecks are, but you may be surprised
by the results of a profiler.  It is always a good idea to profile your code
before you start optimizing it.

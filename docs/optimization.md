# Optimization

In scientific computing, we potentially care a lot about the performance
of our workflows or applications.  We want to study larger systems, more
complex models, or consider more variations of our problem.  This often
means we need to optimize our code to run faster, use less memory, or
scale to more processors.

In this section, a few general strategies for optimization are discussed.
It is not really possible to go into the details since optimization is
often very problem specific.


## Benchmarking

Before you start optimizing your workflow or application, you should
establish a baseline.  This means you should measure the performance
of the current version of your workflow or application.  This will
give you a reference point to compare against.

The benchmark should be chosen so that it is representative of the
workload you are interested in.  For example, it will likely not be
useful to measure the performance of a workflow on a small dataset if
you intend to run it on a large dataset.  The memory usage and the
runtime of the workflow will likely be very different, and hence the
benchmark will not be representative.

You should also make sure that you can run the benchmark easily and
consistently.  This means that you should automate the benchmarking
process as much as possible.  This will allow you to run the benchmark
often and to compare the results.

You should also make sure that you can reproduce the benchmark.  This
means that you should document the benchmark and the environment in
which it was run.  This will allow you to compare the results of the
benchmark over time and to compare the results of the benchmark on
different systems.  You will find more information on this topic in
the section on [reproducibility](reproducibility.md).


## Testing

Having tests in place is vital before starting to optimize your workflow or
application.  You will want to make sure that everything still works after you
make changes. You will find more information on this topic in the section
on [testing](testing.md).


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

When installing software from source, make sure to use the right compiler and
the right flags.  This can make a big difference in performance.  See the section
on [compilers and their flags](#compilers-and-their-flags) for more information.

If you work on an HPC system, it is very likely that the software stack provided
by the module system is already optimized for the system.  Make sure to use
the modules if you can.

Even if several libraries offer the same functionality, they may not be
equally efficient.  For example, the Intel Math Kernel Library (MKL) is
sometimes faster than OpenBLAS/LAPACK.

Another example is the use of the Intel MPI library instead of Open MPI.  The
Intel MPI library is often faster than OpenMPI, especially on Intel processors.
However, you should experiment, since for some codes, Open MPI may be faster.


## Your own code

If the bulk of the time your workflow takes is spent in your own code, you
you should consider optimizing your code.  This can be done in many ways, use

 * a faster compiler and compiler flags to optimize your code;
 * a profiler to identify bottlenecks in your code;
 * a faster algorithm and/or a more efficient data structure;
 * a faster language;
 * vectorization to speed up your code;
 * parallelism to speed up your code.


### Compilers and their flags

For Fortran, C and C++, make sure you are using the right compiler and the
right flags.  For example, the Intel compiler can often generate faster code
than the GNU compiler.  However, you should experiment, since for some codes,
the GNU compiler may generate faster code.

Make sure to compile with optimization flags such as `-O3` and `-xHost` (Intel)
or `-march=native` (GNU).  Many other compiler flag influence performance, but
that is outside the scope of this section.

When using CMake, make sure to set the build type to `Release` to enable
optimizations, i.e., `cmake -DCMAKE_BUILD_TYPE=Release ..`. CMake will then
pass the appropriate flags to the compiler(s).


### Profiling

Your first priority is to identify the bottlenecks in your code.  This can be
done with a profiler.  A profiler will tell you where your code spends most of
its time.  You can then focus on optimizing these parts of your code.

You may think that you know where the bottlenecks are, but you may be surprised
by the results of a profiler.  It is always a good idea to profile your code
before you start optimizing it.

To make this concrete, suppose that your intuitiion tells you that you should
improve the performance of a function, and you spend two days working on it, and
are rewarded by a very impressive improvement by a factor of 10.  This was
excellent work.  However, if your application spends only 5 % of its time in
this function, what will be the runtime of the new version of your application
if that is the only thing you change?

If the total runtime of the orignal application is $t$, it means that its runtime
after your optimization will be $0.95t + 0.5t/10 = 0.955t$, i.e., you improved
the overall runtime by less than 5 %.  In some circumstances this may be worth the
effort you spent, but if you would have profiled your application, you might have
chosen to spend your time differently.

Remenber that you should profile in representative circumstances, see the section
on [benchmarking](#benchmarking) for a more thorough discussion.

There are many tools to profile your application, some open source, but commercial.
TODO: add references to profilers


### Algorithms and data structures

The choice of the algorithm you use to solve a particular problem, or the data
structures you use to represent your data can have a profound impact on the
pformance of your application.

To illustrate this, consider a very simple example, sorting a list of numbers.
There are many algorithms to do this, and all result in the same sorted list.
However, the choice of the algorithm will depend on the length of the list.  A
very simple algorithm is bubble sort which on average implies $O(N^2)$
comparison operations where $N$ is the length of the list.  However, the
quicksort algorithm that is a bit more sophisticated will on average only have
to perform $O(N \log N)$ comparisons.  For long lists, this makes a huge
difference.  For example, if the list has a 1,000 elements ($N = 1000$), then
bubble sort will take a million comparisons, while quicksort will only require
3,000, and hence is a factor of 300 faster.

The choice of data structures you make can also have a profound impact on
perforance.  If the goal of the data structure is to hold, e.g., numbers to
allow to check whether or not a number occured previously, you can use a list
or a set.  Checking membership in a list will take $O(N)$ comparisons on
average, while checking membership of a set only takes $O(1)$ (ideally).  Just
like the choice of algorhtm in the previous example, this may have an important
impact on performance.

This section only draws your attention to the problem, it would be impossible to
go into more detail, but it is a very good investment of your time to familiarize
yourself with the subject.  Many excellent books have been published on the subject,
covering the most common algorithms, and a lot of articles have been published that
address very specific algorithms and specialized data structures.
TODO: add references to books

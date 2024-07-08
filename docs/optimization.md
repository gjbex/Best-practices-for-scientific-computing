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
useful to measure the performance of a workflow on a small data set if
you intend to run it on a large data set.  The memory usage and the
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
on [testing](testing/index.md).


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
Intel MPI library is often faster than Open MPI, especially on Intel processors.
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

To make this concrete, suppose that your intuition tells you that you should
improve the performance of a function, and you spend two days working on it, and
are rewarded by a very impressive improvement by a factor of 10.  This was
excellent work.  However, if your application spends only 5 % of its time in
this function, what will be the runtime of the new version of your application
if that is the only thing you change?

If the total runtime of the original application is $t$, it means that its runtime
after your optimization will be $0.95t + 0.5t/10 = 0.955t$, i.e., you improved
the overall runtime by less than 5 %.  In some circumstances this may be worth the
effort you spent, but if you would have profiled your application, you might have
chosen to spend your time differently.

Remember that you should profile in representative circumstances, see the section
on [benchmarking](#benchmarking) for a more thorough discussion.

There are many tools to profile your application, some open source, but
commercial as well.  Some tools can profile parallel applications.  See the
[tools section](tools/index.md) for more information.


### Algorithms and data structures

The choice of the algorithm you use to solve a particular problem, or the data
structures you use to represent your data can have a profound impact on the
performance of your application.

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
performance.  If the goal of the data structure is to hold, e.g., numbers to
allow to check whether or not a number occurred previously, you can use a list
or a set.  Checking membership in a list will take $O(N)$ comparisons on
average, while checking membership of a set only takes $O(1)$ (ideally).  Just
like the choice of algorithm in the previous example, this may have an important
impact on performance.

This section only draws your attention to the problem, it would be impossible to
go into more detail, but it is a very good investment of your time to familiarize
yourself with the subject.  Many excellent books have been published on the subject,
covering the most common algorithms, and a lot of articles have been published that
address very specific algorithms and specialized data structures.
TODO: add references to books


### Programming languages

Holy wars are waged on the subject of programming languages.  Many of the
discussions royally miss the point completely.

In general compiled languages such as Fortran, C and C++ will produce faster
applications. However, it is typically also more difficult to write
applications in such a language then it is in R or Python.  This implies that
if your application is not performance critical, it would be a waste of time to
write it in Fortran, C, or C++.  Your time as a researcher is also quite
valuable, so a short time to solution will be appreciated by the taxpayer.

A good compromise is to implement the performance-critical parts of the
application in a language such as Fortran, C, or C++, and wrap the resulting
shared libraries so that they can be used from Python or R.  This gives you the
best of both worlds. TODO: add wrapper tools for Python and R.

Often, the work is already done for you.  Consider the somewhat extreme example
of machine learning.  Frameworks such as TensorFlow or PyTorch allow you to
write your code in Python at a high lever, while relying on libraries that were
developed by HPC specialists under the hood.  The execution time spent in pure
Python code is completely negligible when compared to that spent on
computations done by these core libraries.

Again, [profiling](#profiling) is crucial to determine what parts of your
application make good candidates for reimplementation in a more performant
programming language.

Julia takes a somewhat different approach.  The code you write will under the
hood be translated to machine code before it is actually executed.  Hence you
get quite good performance out of the box when using Julia (well).


### Vectorization

In scientific computing, core computations often consists of loops over arrays.
If these loops implement matrix-vector or matrix-matrix operations, it is likely
not a good idea to write such code.  Consider using a library to represent these
data structures that uses a BLAS (TODO) or LAPACK (TODO) library under the hood.

These libraries have been developed with vectorization in mind, i.e., multiple
iterations of the loops required for matrix-vector or matrix-matrix multiplication
are done in parallel using wide registers.  Depending on the numerical precision
(single or double), the compiler flags used, as well as the hardware you compiled
your code for that may range from 2 to 16.  Since such operations are often at the
core of your computations, ensuring that you benefit from vectorization may give
you a significant performance benefit.

In your own code, the compiler can often automatically apply vectorization on
your own loops, given that it can prove that the iterations are independent of one
another.  To ensure that the compiler will attempt this, you would have to use the
appropriate compiler flags.
TODO: add compiler flags for vectorization

Sometimes the compiler can not prove that vectorization is possible, i.e., that
the iterations are independent.  If you as a programmer knows for sure that although
loop iterations are dependent, that dependence is on iterations that are not within
the vector length, you can help the compiler by providing the appropriate OpenMP
SIMD (TODO) directives.  Again, this exceeds the scope of this section and you are
referred to trainings on this specific topic. (TODO: refer to trainings)


### Parallelization

Parallelization comes in many forms at various levels and complexity.


#### Embarrassingly parallel

The most obvious and common situation is that you have to run your workflow or
application on many different data sets, or with a variety of (hyper)parameter
values.  This form of parallelism is called "embarrassingly parallel" because it
is very simple to implement.  It is as simple as running your workflow or
application on as many compute resources as you can get.

The CPU (Central Processing Unit) of a modern laptop has multiple cores, each core
capable of executing an application independent and in parallel with applications
running on other cores.  A simple shell script using [parallel](TODO) can help you
to run such workloads easily on your own system.

On HPC clusters, more specialized tools exist that serve the same purpose, using
the scheduler to run your workload in parallel.  Some examples of such tools are
[atools][TODO] and [worker-ng](TODO).

If your use case doesn't match this approach, or individual runs of your workflow
or application require too much time then other options are available at the price
of (often) much higher complexity and effort on your part.


#### Shared memory programming

As mentioned before, modern CPUs have multiple cores, today ranging for
typically 4 in your laptop to 128 in HPC compute nodes.  Shared memory
programming allows your application to utilize (potentially) all of these cores
to perform computations in parallel, hence speeding up your application.

Again, using the right libraries may give you a free lunch, similar to
vectorization. Intel MKL and OpenBLAS/LAPACK will execute operations on
multiple course if you link to the correct implementation.  This is also the
case for other libraries that use these under the hood. (TODO: add examples).
The same applies to Python and R packages, e.g., numpy can use a BLAS library
under the hood to perform matrix operations, hence using multiple cores for the
computations.

For Fortran, C, and C++, [OpenMP](TODO) is a good option to parallelize your
code in a shared memory context. Typically, you annotate your source code with
directives on, e.g., loop constructs to indicate to the compiler that these
loops should be parallelized. The compiler will generate the appropriate
instructions for you.  This sounds suspiciously easy, and indeed, it is not so
simple in practice to obtain good efficiency. 

Specifically for C++ a few more options are available.  Many algorithms in the
STL (Standard Template Library) can be executed in parallel with minimal
changes to your source code.  Of course, this is restrictions to those
algorithms that support it.

An alternative to OpenMP for C++ is TBB (Threading Building Blocks).  This
library is purely task oriented, with an excellent task scheduler under the
hood.

For Python, packages such as [Cython](TODO) and [Numba](TODO) will allow you to
leverage multiple cores explicitly or implicitly, respectively.

Again, you are referred to specific trainings on this subject.


#### GPGPUs

If your compute system is equiped with a graphics card that has compute
capabilities (certain NVIDIA or AMD GPUs) then this is another level of
parallelism that can be exploited.

Again, certain libraries will do this for you under the hood, e.g., machine
learning frameworks such as [TensorFlow](TODO) and [PyTorch](TODO). More
general frameworks  such as [cupy](TODO) and [Numba](TODO) allow you to offload
more general computations to the GPU.

For Fortran, C, and C++ OpenACC or OpenMP may be an excellent solutions since
compilers that implement these standards will generate appropriate code to
transfer data to and from the GPU device, and run kernels.

For C and C++ vendors of GPUs offer specific programming language extensions
that work only on the specific hardware.  This is [CUDA](TODO) for NVIDIA GPUs,
and [HIP](TODO) for AMD hardware.  This is a trade-off between (potentially)
better performance and vendor lock-in.

Specifically for C++ there are even more options: [Data Parallel C++](TODO)
(based on SYCL, developed by Intel) and the [Kokkos](TODO) library.

Getting good performance on GPUs is not a trivial task due to data transport
between host and device memory.  Also, not all types of algorithms map well on
the hardware architecture of such devices. (TODO: refer to training)


#### Using multiple computers

Up to this point, parallelization was limited to the possibilities a single
system offered, multiple cores and perhaps one or more GPUs.  To further scale
and use multiple compute nodes more work is required.

Relatively simple option for some tasks exist for Python.  Frameworks like [Dask](TODO)
or [Ray](TODO) allow you to distributes computations over multiple compute nodes.
Note that these are not general solutions, but will support certain use cases only.
If your problem fits one of those use cases, substantial gains can be made without
too much effort.

For Python, Fortran, C, and C++ Message Passing Interface (MPI) may be an option.
This is a standard implemented in various libraries such as Intel MPI, Open MPI,
MVAPICH and others.  Using such a library requires a substantial rewrite of your
code.  The standard offers great flexibility and the potential for excellent
parallel performance and scaling to a large number of nodes.

To similarly parallelize code on multiple NVIDIA GPUs on multiple compute nodes,
[NCCL](TODO) can be used.  Conceptually, it is quite similar to MPI, but messages
are exchanged between processes running on GPUs, rather than processes on the CPUs.

Finally, [Data Parallel C++](TODO) and [Kokkos](TODO) can also be used from C++ to
parallelize your code over multiple  nodes. (TODO: check this).

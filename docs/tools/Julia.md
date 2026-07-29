# Tools for Julia programming

Julia includes package management, testing, and profiling facilities in its
standard distribution.  A practical baseline combines those facilities with
Juliaup, JuliaFormatter, Documenter, and editor support; package-quality and
deeper analysis tools can be added when the project needs them.


## Recommended baseline

* [Juliaup](https://github.com/JuliaLang/juliaup) installs Julia and manages
  multiple release channels.  It is useful when a project must be checked
  against more than one Julia version.
* [Pkg](https://pkgdocs.julialang.org/) is Julia's standard package and
  environment manager.  Use a project-specific environment and commit its
  `Project.toml`.  For an application or reproducible scientific workflow,
  also commit `Manifest.toml` so that collaborators can instantiate the same
  package versions.
* The [Julia extension for Visual Studio
  Code](https://www.julia-vscode.org/docs/stable/) provides language-server
  support, debugging, profiling, test integration, and formatting.

A project environment can be instantiated and tested non-interactively with

```bash
julia --project=. -e 'using Pkg; Pkg.instantiate(); Pkg.test()'
```

This is a useful starting point for both a local check and continuous
integration.


## Code formatting and interactive development

* [JuliaFormatter](https://domluna.github.io/JuliaFormatter.jl/stable/) formats
  Julia source and can use a repository-local `.JuliaFormatter.toml`
  configuration.  The Julia extension for Visual Studio Code uses
  JuliaFormatter for document formatting.
* [Revise](https://timholy.github.io/Revise.jl/stable/) updates loaded code
  when source files change.  It reduces the need to restart a long-running
  interactive Julia session, although a clean session should still be used for
  final validation and reproducibility checks.


## Testing and package-quality checks

* Julia's standard [`Test`
  library](https://docs.julialang.org/en/v1/stdlib/Test/) supports test sets,
  approximate comparisons, exception tests, and other assertions.
  `Pkg.test()` runs a package's test suite in a dedicated environment.
  Numerical tests should state appropriate absolute or relative tolerances and
  check scientifically meaningful properties.
* [Aqua](https://juliatesting.github.io/Aqua.jl/stable/) checks package hygiene,
  including method ambiguities, undefined exports, stale dependencies,
  compatibility bounds, type piracy, and persistent tasks.  It is especially
  useful for reusable packages, but it is not a substitute for behavioral
  tests.
* [JET](https://aviatesk.github.io/JET.jl/stable/) uses compiler inference to
  report possible type and dispatch errors.  Treat it as an optional advanced
  analysis tool rather than as a direct equivalent of a conventional linter:
  its compatibility and results can depend on the Julia compiler version, and
  a clean report does not establish that all program behavior is correct.


## Documentation

* [Documenter](https://documenter.juliadocs.org/stable/) builds documentation
  from Markdown files and Julia docstrings.  It supports cross-references,
  executable examples, and doctests, which can help keep documentation aligned
  with the code.


## Benchmarking and profiling

* [BenchmarkTools](https://juliaci.github.io/BenchmarkTools.jl/stable/)
  provides warm-up, repeated sampling, and controls that reduce common
  measurement errors.  Use interpolation correctly so that a benchmark
  measures the intended operation rather than global-variable access or setup
  work.
* Julia's standard [`Profile`
  library](https://docs.julialang.org/en/v1/stdlib/Profile/) is a sampling
  profiler for CPU execution.  Results can be inspected with
  [ProfileView](https://github.com/timholy/ProfileView.jl) or the
  [Visual Studio Code profile
  viewer](https://www.julia-vscode.org/docs/stable/userguide/profiler/).

BenchmarkTools is appropriate for focused operations, while profiling a
representative application is better for finding the part of a scientific
workflow that is actually worth optimizing.  Record Julia and package
versions, hardware, input data, warm-up procedure, and relevant thread or
process settings when reporting performance.


## Scientific and HPC environments

Pkg records Julia packages and binary artifacts, but it does not necessarily
describe the complete environment of an HPC application.  External MPI
installations, system compilers and libraries, accelerator drivers, scheduler
settings, and site-provided modules may remain outside the Julia environment.

Use a suitable environment or system-level package manager, such as Spack or
Pixi, when these dependencies must be managed together.  If a site-provided
MPI or accelerator stack is required, document its modules and versions and
test the Julia bindings against the configuration used for production runs.

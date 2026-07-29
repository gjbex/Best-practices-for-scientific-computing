# Tools for Rust programming

Rust provides an unusually integrated development toolchain.  For most
projects, start with rustup, Cargo, rustfmt, Clippy, rustdoc, and rust-analyzer
before adding more specialized tools.


## Recommended baseline

* [rustup](https://rust-lang.github.io/rustup/) installs Rust toolchains and
  optional components.  A project can use a `rust-toolchain.toml` file to state
  the required toolchain and components.
* [Cargo](https://doc.rust-lang.org/cargo/) manages Rust packages and
  dependencies and provides the standard commands for building, running,
  testing, benchmarking, and generating documentation.
* [rust-analyzer](https://rust-analyzer.github.io/) provides editor and
  language-server support, including completion, navigation, and diagnostics.

A useful local or continuous-integration baseline is

```bash
cargo fmt --check
cargo clippy --all-targets --all-features -- -D warnings
cargo test
cargo doc --no-deps
```

Projects do not need to use `--all-features` if some features are mutually
exclusive or require unavailable system dependencies.  The commands used in
continuous integration should match configurations that the project actually
supports.


## Code formatting and static analysis

* [rustfmt](https://github.com/rust-lang/rustfmt) is Rust's standard formatter
  and is normally run as `cargo fmt`.  Its configuration can be stored in
  `rustfmt.toml`.
* [Clippy](https://doc.rust-lang.org/clippy/) is the standard collection of
  lints for common mistakes, suspicious code, and non-idiomatic constructs.
  It complements rather than replaces compiler diagnostics and tests.


## Testing, coverage, and documentation

* [`cargo test`](https://doc.rust-lang.org/cargo/commands/cargo-test.html)
  builds and runs unit tests, integration tests, and documentation tests.
  Numerical tests should use tolerances and scientifically meaningful
  invariants rather than exact equality where rounding error is expected.
* [cargo-llvm-cov](https://github.com/taiki-e/cargo-llvm-cov) provides
  source-based test-coverage reports using LLVM's instrumentation.  Coverage
  shows which code was executed, not whether the scientific assertions were
  adequate.
* [rustdoc](https://doc.rust-lang.org/rustdoc/) generates API documentation
  from Rust source and documentation comments.  `cargo doc` is its normal
  Cargo interface, and examples in documentation can be checked as tests.


## Benchmarking and profiling

* [Criterion.rs](https://bheisler.github.io/criterion.rs/book/) provides
  statistically analysed microbenchmarks with warm-up and repeated sampling.
  It is useful for focused functions or kernels, but a microbenchmark does not
  replace measurement of the complete scientific workload.
* [cargo-flamegraph](https://github.com/flamegraph-rs/flamegraph) records a
  program and produces a flame graph that helps identify where CPU time is
  spent.  On Linux it normally uses `perf`.
* General HPC profilers such as HPCToolkit, Linaro Forge, Scalasca, and Intel
  VTune may be more appropriate for applications that use MPI, accelerators,
  multiple languages, or vendor numerical libraries.  See the
  [general tools](general.md) and [optimization](../optimization.md) pages.

Use representative inputs and record the compiler toolchain, optimization
settings, hardware, thread or rank placement, and relevant library versions
when reporting performance.


## Dependency auditing

* [cargo-audit](https://github.com/rustsec/rustsec/tree/main/cargo-audit)
  checks dependencies recorded in `Cargo.lock` against the RustSec Advisory
  Database.  It is a useful automated check, but findings still require
  assessment in the context of how a dependency is used.


## Scientific and HPC environments

Cargo is the appropriate default for Rust crates, but it does not manage a
complete HPC software stack.  A Rust application may also depend on a system
MPI implementation, C or Fortran libraries, vendor mathematics libraries,
compiler modules, accelerator runtimes, or scheduler configuration.

Use a suitable environment or system-level package manager, such as Spack or
Pixi, when those dependencies must be resolved together.  Record site-provided
modules and compiler or MPI versions when the environment cannot be captured
in the repository.  Cargo remains responsible for the Rust portion of such a
mixed environment.

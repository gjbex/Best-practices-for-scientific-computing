# Scientific I/O and data formats

Scientific software does not end when a calculation produces numbers.  Data
files are interfaces between stages of a workflow, software tools,
collaborators, and future versions of a project.  A result is difficult to
reproduce or reuse if its values cannot be read reliably, or if their meaning
is no longer known.

Input and output (I/O) choices also affect performance, especially for large
data or shared HPC filesystems.  Performance is not the main concern here,
however.  The first priority is data that remains interpretable, accessible,
and reliable throughout its intended lifetime.


## Start with the purpose of the data

Before choosing a format, determine why the data is being stored and who or
what will read it.  Common purposes include

* configuration and parameters;
* intermediate data passed between workflow stages;
* results intended for analysis or visualization;
* checkpoints used to restart a calculation;
* data exchanged with collaborators or other software; and
* data prepared for publication or long-term preservation.

One format does not have to serve every purpose.  A checkpoint optimized for a
fast restart may be a poor publication format, while a rich analysis file may
contain information that is unnecessary during a restart.

When a scientific community has an established data standard, prefer it unless
there is a concrete reason not to.  Domain standards improve interoperability
and often define metadata conventions that a generic format does not provide.


## Choosing a format

The format should fit the structure, size, access pattern, portability
requirements, and expected lifetime of the data.

| Need | Useful starting point | Important limitation |
|------|-----------------------|----------------------|
| configuration or structured metadata | JSON, YAML, or TOML | a schema, units, and value constraints still need to be documented |
| small, human-inspectable tables | CSV or TSV | types, units, missing values, and schema are not preserved automatically |
| large analytical tables | Parquet or an Arrow-based format | consider tool support and whether access is row-oriented or column-oriented |
| multidimensional arrays, grids, or time series | HDF5, NetCDF, or a domain standard | layout, chunking, compression, and metadata conventions require deliberate choices |
| checkpoints | a supported binary or structured container | it must contain the complete restart state and identify incompatible files |
| small diagnostic output | plain text or structured logs | usually unsuitable for large numerical datasets |

Text is valuable when people need to inspect or edit small files.  It is
usually a poor default for large numerical arrays because it consumes more
space, loses type information, and requires conversion between text and binary
values.

A custom binary format may be justified for a specialized application, but it
creates a long-term obligation.  Its schema must specify types, precision,
shapes, ordering, endianness, metadata, and versioning, and a maintained reader
must remain available.


## Store meaning as well as values

Numbers without context are not reusable scientific data.  Depending on the
data, record or document

* descriptive variable and field names;
* units and numerical precision;
* dimensions, shapes, and axis order;
* coordinate systems, reference frames, and indexing conventions;
* missing-value and invalid-value representations;
* category or enumeration definitions;
* the schema or file-layout version; and
* the provenance needed to understand how the data was produced.

Provenance may include identifiers or checksums for input data, the software
version, configuration, random seed, and processing step that produced the
file.  Keep metadata close to the values it describes when practical.  An
unversioned note in a separate location is easily lost or allowed to become
inconsistent with the data.

The [reproducibility section](reproducibility.md) discusses how data,
software, workflows, and parameters together form the record of a computational
experiment.


## Treat readers and writers as interfaces

Reading and writing data are part of the software interface and should be
designed and tested accordingly.

* Validate required fields, types, shapes, ranges, and metadata when reading.
* Fail clearly on malformed, truncated, or unsupported files.
* Test important formats with a write-read round trip.
* Check scientifically meaningful values after the round trip, not only
  whether a file exists.
* Use checksums to detect accidental modification or transfer errors.
* Write a new file completely before replacing an existing result, using an
  atomic replacement where the filesystem provides the required guarantees.
* Avoid silently overwriting raw input data or previous results.
* Version schemas and provide a migration path when old files must remain
  readable.

A checksum can show that a sequence of bytes has not changed.  It does not show
that the file is scientifically correct, complete for its intended purpose, or
associated with the right experiment.


## Checkpoint and restart

A checkpoint is useful only if the application can restart from it correctly.
It must contain the full state required to continue, which may include

* simulation time and progress counters;
* fields, particles, or model state;
* solver and algorithm state;
* parameters and numerical precision;
* pseudo-random-number-generator state; and
* global shape or decomposition information for a parallel calculation.

Include enough version information to reject an incompatible checkpoint with a
clear error.  Document whether checkpoints are portable between program
versions, machines, process counts, or numerical precisions.

Checkpoint writes should tolerate interruption.  Useful strategies include
writing to a new file before marking it complete, retaining more than one
recent checkpoint, and validating a checkpoint before removing the previous
one.  Test the restart path: successfully writing a checkpoint is not evidence
that it contains everything required to resume.


## Access patterns and performance

I/O is part of the end-to-end runtime of a scientific workflow.  Several
general observations are useful even when performance is not the primary
topic.

* Reading or writing many small files can cause many metadata operations and
  perform poorly on a shared filesystem.
* Batching several values or records into one operation can reduce overhead.
* Compression reduces storage and transfer volume but requires processor time.
* Array layout and chunking should match the way data will normally be
  accessed.
* Writing unnecessary precision or outputting too frequently wastes both time
  and storage.
* Per-process files may be easy to implement but difficult to manage or
  reconstruct at larger process counts.
* Node-local temporary storage may help some workloads, but durable results
  still need to be transferred and recorded safely.

Measure I/O using representative data and access patterns before redesigning a
format.  A format that performs well for sequential access may perform poorly
for small random reads, and results obtained on a laptop may not transfer to an
HPC filesystem.

The [Best practices for data science on
HPC](https://gjbex.github.io/Best-practices-for-data-science-on-HPC/)
training provides detailed examples and experiments on data formats, filesystem
behavior, and the many-small-files problem.


## Short activity

Consider a simulation that produces

* a human-edited configuration;
* a multidimensional state field;
* periodic restart checkpoints;
* a summary table used for plotting; and
* a subset of results that will accompany a publication.

For each output, discuss

1. who or what will read it;
2. a suitable format and why;
3. the metadata required to interpret it;
4. one validation or round-trip check;
5. whether partial writes or incompatible versions must be detected; and
6. the expected access pattern.

There is not necessarily one correct set of formats.  A good answer makes the
requirements and trade-offs explicit rather than selecting a format solely
because it is familiar.


## Checklist

Before adopting an I/O design, ask:

1. What purpose does each file serve?
2. Can the intended users and tools read it?
3. Will its values still be interpretable without undocumented knowledge?
4. Can the reader detect malformed, incomplete, or incompatible data?
5. Has the write-read path been tested?
6. Does the layout fit the expected data size and access pattern?
7. Is the relationship between the file and the computational experiment
   recorded?

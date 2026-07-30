# Version-control demonstration

This instructor-led demonstration is the **traceable changes** stage of the
[running temperature-analysis example](running_example.md).  It shows why
version control is useful without turning the session into a tutorial on Git
commands.  It takes about 10 minutes and uses a disposable repository
containing a small scientific analysis.


## Learning objective

After observing the demonstration, participants should be able to explain how
version control helps them

* identify a change that affects a scientific result;
* recover a known-working version of the code;
* experiment without being afraid of losing working code; and
* associate a result with a specific version of its source code.

Participants are not expected to memorize the commands shown.


## Requirements

The demonstration requires

* Git;
* Python 3; and
* a text editor.

It has no third-party Python dependencies and requires no network access.


## Prepare the demonstration

From the root of this training repository, create a new disposable repository:

```bash
demo_dir=$(bash docs/version_control_demo/prepare_demo.sh)
cd "$demo_dir"
```

The preparation script copies the example files to a temporary directory,
initializes a Git repository, and creates one known-working commit.  It prints
the path of the new repository, which is stored in `demo_dir` above.

Run these commands before the session to verify the starting state:

```bash
python3 temperature_analysis.py measurements.csv
python3 check_result.py
git status --short
git log --oneline
```

The analysis and check should report

```text
Mean temperature: 293.15 K
PASS: mean temperature is 293.15 K
```

`git status --short` should produce no output, indicating that the working tree
is unchanged.


## Demonstration script

### 1. Establish the working result

Run the analysis and its known-result check:

```bash
python3 temperature_analysis.py measurements.csv
python3 check_result.py
```

Explain that the five accepted measurements have a mean of 20 degrees Celsius,
or 293.15 kelvin.  One additional observation remains visible in the input but
is excluded by its quality flag.  The check gives the group a quick way to
notice if the accepted scientific result changes.


### 2. Introduce a plausible bug

Open `temperature_analysis.py` and change

```python
KELVIN_OFFSET = 273.15
```

to

```python
KELVIN_OFFSET = 272.15
```

Rerun the analysis and check:

```bash
python3 temperature_analysis.py measurements.csv
python3 check_result.py
```

The output should now be

```text
Mean temperature: 292.15 K
FAIL: expected 293.15 K, observed 292.15 K
```

The failed command is intentional.  Ask participants what they would normally
do when a previously working result changes.


### 3. Inspect what changed

Show that Git knows the file was modified:

```bash
git status --short
git diff
```

The diff identifies the exact change from `273.15` to `272.15`.  Emphasize the
capability rather than the syntax: version control can show what changed since
the known-working version.


### 4. Recover the working version

Restore the version recorded in the last commit:

```bash
git restore temperature_analysis.py
python3 check_result.py
git status --short
```

The check should pass again, and `git status --short` should produce no output.
The important point is not the `git restore` command itself, but that the
known-working version was available and could be recovered immediately.


### 5. Connect the result to its source

Display the identifier of the current commit:

```bash
git rev-parse --short HEAD
```

Explain that recording such an identifier with computational results connects
those results to a precise version of the code.  Data, parameters, the software
environment, and the workflow must still be recorded separately.


## Timing and delivery notes

| Part | Time |
|------|------|
| establish the working result | 1 min. |
| introduce the bug | 2 min. |
| inspect the difference | 3 min. |
| restore and verify | 2 min. |
| provenance takeaway | 2 min. |

Keep the terminal font large and narrate what Git makes possible rather than
explaining every option.  If participants ask how the commands work, refer them
to the [Version control with Git](https://gjbex.github.io/Version-control-with-git/)
training for hands-on instruction.

To rehearse or repeat the demonstration, run the preparation script again.  It
creates a fresh temporary repository each time.

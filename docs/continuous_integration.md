# Continuous integration

Continuous Integration (CI) is provided by both GitHub and GitLab.  It can be
used to make sure that code that is committed is automatically tested and that
it can be build, potentially on a matrix of architectures and operating systems.

You can find an example of using CI for development in the repository
[CI-example](https://github.com/gjbex/CI-example).  A workflow is defined that
will run on a push or a pull request to both `main` and `development`. If that
workflow fails, the pull request can not be merged.  The workflow will run
`pytest` and `mypy` to perform unit tests and static type analysis respectively.
This can be a safeguard against accidentally merging commits that break your
code.  This also relies on the configuration of the `main` branch that requires
the build to succeed in order to allow a merge.

The same repository also illustrates how poetry can be used to manage Python
development projects.

You can also use CI to build your documentation using doxygen, mkdocs or other
tools such as, e.g., Sphinx.  The documentation can be automatically deployed
using GitHub Pages thanks to predefined actions.  In fact, these web pages are
rendered an published using mkdocs and a GitHub workflow.  This workflow will
checkout the `main` branch, render the site using mkdocs in the `gh-pages`
branch so that it is published.  Each time a push is done to the `main` branch
the workflow is run, and the latest version is guaranteed to be available via
GitHub pages.  You can find the workflow definition in the `.github/workflows`
directory in the [repository]().

Since this is in fact a deployment of documentation, it is referred to as
Continuous Deployment (CD).  It would of course also be possible to typeset a
LaTeX document in a workflow, and make a PDF version available for download.

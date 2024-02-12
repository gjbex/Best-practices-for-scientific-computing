# Continuous integration

Continuous Integration (CI) is provided by both GitHub and GitLab.  It can be
used to make sure that code that is committed is automatically tested and that
it can be build, potentially on a matrix of architectures and operating systems.

You can also use CI to build your documentation using doxygen, mkdocs or other
tools such as, e.g., Sphinx.  The documentation can be automatically deployed
using GitHub Pages thanks to predefined actions.  In fact, these webpages are
rendered an published using mkdocs and a GitHub workflow.  This workflow will
checkout the `main` branch, render the site using mkdocs in the `gh-pages`
branch so that it is published.  Each time a push is done to the `main` branch
the workflow is run, and the latest version is guaranteed to be available via
GitHub pages.  You can find the workflow definition in the `.github/workflows`
directory in the [repository]().

Since this is in fact a deployment of documentation, it is referred to as
Continuous Deployment (CD).  It would of course also be possible to typeset
a LaTeX document in a workflow, and make a PDF version available for download.

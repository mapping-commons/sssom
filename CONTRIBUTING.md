# Contributing to SSSOM

:+1: First of all: Thank you for taking the time to contribute!

The following is a set of guidelines for contributing to SSSOM. They are derived from the excellent contribution guidelines for the [ATOM Editor](https://github.com/atom/atom/blob/master/CONTRIBUTING.md) and are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

#### Table Of Contents

[Code of Conduct](#code-of-conduct)

[I don't want to read this whole thing, I just have a question!!!](#i-dont-want-to-read-this-whole-thing-i-just-have-a-question)

[What should I know before I get started?](#what-should-i-know-before-i-get-started)

[How Can I Contribute?](#how-can-i-contribute)
  * [Reporting Bugs](#reporting-bugs)
  * [Suggesting Enhancements](#suggesting-enhancements)
  * [Your First Code Contribution](#your-first-code-contribution)
  * [Pull Requests](#pull-requests)
  * [Local Testing](#local-testing)

[Styleguides](#styleguides)
  * [Git Commit Messages](#git-commit-messages)
  * [Documentation Styleguide](#documentation-styleguide)

[Additional Notes](#additional-notes)
  * [Issue and Pull Request Labels](#issue-and-pull-request-labels)

## Code of Conduct

This project and everyone participating in it is governed by the [SSSOM Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [a member of the SSSOM core team](https://mapping-commons.github.io/sssom/contact/).

## I don't want to read this whole thing I just have a question!!!


We have an official message board with a detailed FAQ and where the community chimes in with helpful advice if you have questions.

* [Github Discussions](https://github.com/mapping-commons/sssom/discussions)
* [SSSOM FAQ](https://mapping-commons.github.io/sssom/faq/)

## What should I know before I get started?

- Read the [overview](https://mapping-commons.github.io/sssom/spec/)
- Do the [SSSOM tutorial](https://mapping-commons.github.io/sssom/tutorial/)
- Read about the [SSSOM toolkit](https://mapping-commons.github.io/sssom-py), which is managed [in a different repo](https://github.com/mapping-commons/sssom-py)

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report for SSSOM. Following these guidelines helps maintainers and the community understand your report :pencil:, reproduce the behavior :computer: :computer:, and find related reports :mag_right:.

Before creating bug reports, please check [this list](#before-submitting-a-bug-report) as you might find out that you don't need to create one. When you are creating a bug report, please [include as many details as possible](#how-do-i-submit-a-good-bug-report). Wherever available, use [existing issue tracker templates](https://github.com/mapping-commons/sssom/issues/new/choose), the information it asks for helps us resolve issues faster.

> **Note:** If you find a **Closed** issue that seems like it is the same thing that you're experiencing, open a new issue and include a link to the original issue in the body of your new one.

#### Before Submitting A Bug Report

* **Check the [discussions](https://github.com/mapping-commons/sssom/discussions)** for a list of common questions and problems.
* **Decide whether the issue should be reported in the tracker for the [SSSOM data model](https://github.com/mapping-commons/sssom/issues) or the tracker for the [SSSOM toolkit](https://github.com/mapping-commons/sssom-py/issues)**.
* **Perform a [cursory search](https://github.com/mapping-commons/sssom/issues)** to see if the problem has already been reported. If it has **and the issue is still open**, add a comment to the existing issue instead of opening a new one.

#### How Do I Submit A (Good) Bug Report or Feature request?

Bugs and feature requests are tracked as [GitHub issues](https://guides.github.com/features/issues/). After you've determined which repository your bug or feature is related to, create an issue on that repository providing the information required by [the appropriate template](https://github.com/mapping-commons/sssom/issues/new/choose).

Explain the problem and include additional details to help maintainers reproduce the problem:

* **Use a clear and descriptive title** for the issue to identify the problem/requests.
* **Describe the exact steps which reproduce the problem** in as many details as possible. For example, start by explaining how you started SSSOM, e.g. which command exactly you used in the terminal, or how you started SSSOM otherwise. When listing steps, **don't just say what you did, but explain how you did it**. For example, if you moved the cursor to the end of a line, explain if you used the mouse, or a keyboard shortcut or an SSSOM command, and if so which one?
* **Provide specific examples to demonstrate the steps**. Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples. If you're providing snippets in the issue, use [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**

Include details about your configuration and environment:

* **Which version of SSSOM toolkit/model are you using?** You can get the exact version by running `sssom --version` in your terminal
* **What's the name and version of the OS you're using**?

### Your First Code Contribution

Unsure where to begin contributing to SSSOM? You can start by looking through these `beginner` and `help-wanted` issues:

* [Beginner issues][beginner] - issues which should only require a few lines of code, and a test or two.
* [Help wanted issues][help-wanted] - issues which should be a bit more involved than `beginner` issues.

### Pull Requests

The process described here has several goals:

- Maintain SSSOM's quality
- Fix problems that are important to users
- Engage the community in working toward the best possible data model and toolkit
- Enable a sustainable system for SSSOM's maintainers to review contributions

Please follow these steps to have your contribution considered by the maintainers:

1. Follow all instructions in the pull request template (you will see them when you open a pull request).
2. Follow the [styleguides](#styleguides)
3. After you submit your pull request, verify that all [status checks](https://help.github.com/articles/about-status-checks/) are passing <details><summary>What if the status checks are failing?</summary>If a status check is failing, and you believe that the failure is unrelated to your change, please leave a comment on the pull request explaining why you believe the failure is unrelated. A maintainer will re-run the status check for you. If we conclude that the failure was a false positive, then we will open an issue to track that problem with our status check suite.</details>

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.

### Local testing

Contributors are strongly advised to run the test suite locally even before submitting a pull request. This requires a working Python environment that includes a working version of Poetry.

Prepare the testing environment by running:

```sh
$ make install
```

This only needs to be run once after cloning the repository. After that, the test suite can be run anytime with

```sh
$ make test
```

Furthermore, any change to the LinkML model should also be tested against SSSOM-Py. To do so:

1. In the current `sssom` repository, build the Python files derived from the LinkML:

```sh
$ make all
```

2. Clone the SSSOM-Py repository somewhere (outside of your current checkout of `sssom`):

```sh
$ git clone https://github.com/mapping-commons/sssom-py.git
```

3. Initialise the Poetry environment inside the newly cloned SSSOM-Py repository:

```sh
$ poetry install
```

(Beware that SSSOM-Py does not support Python 3.12, so if that is your default Python version, you may need to explicitly require that Python < 3.12 be used instead, e.g. with `poetry env use 3.11`.)

4. Forcefully install your _local_ version of `sssom-schema` in the newly initialised environment:

```sh
$ poetry run python -m pip install /path/to/your/sssom/repository
```

You may get a warning about “incompatible sssom-schema versions”; this is due to the fact that your local copy of `sssom` has a version number set to `0.0.0` (the “real” version number is set at release time, when the package is published to PyPI) and can be safely ignored.

5. Run SSSOM-Py’s test suite:

```sh
$ poetry run tox -e py
```


## Styleguides

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* Consider starting the commit message with an applicable emoji:
    * :art: `:art:` when improving the format/structure of the code
    * :racehorse: `:racehorse:` when improving performance
    * :non-potable_water: `:non-potable_water:` when plugging memory leaks
    * :memo: `:memo:` when writing docs
    * :penguin: `:penguin:` when fixing something on Linux
    * :apple: `:apple:` when fixing something on macOS
    * :checkered_flag: `:checkered_flag:` when fixing something on Windows
    * :bug: `:bug:` when fixing a bug
    * :fire: `:fire:` when removing code or files
    * :green_heart: `:green_heart:` when fixing the CI build
    * :white_check_mark: `:white_check_mark:` when adding tests
    * :lock: `:lock:` when dealing with security
    * :arrow_up: `:arrow_up:` when upgrading dependencies
    * :arrow_down: `:arrow_down:` when downgrading dependencies
    * :shirt: `:shirt:` when removing linter warnings

### Documentation Styleguide

* Use [Markdown](https://daringfireball.net/projects/markdown).

## Additional Notes

### Issue and Pull Request Labels

This section lists the labels we use to help us track and manage issues and pull requests. Most labels are used across all mapping commons repositories.

#### Type of Issue and Issue State

| Label name | `mapping-commons/sssom` :mag_right: | `sssom`‑org :mag_right: | Description |
| --- | --- | --- | --- |
| `enhancement` | [search][search-sssom-repo-label-enhancement] | [search][search-mapping-commons-org-label-enhancement] | Feature requests. |
| `bug` | [search][search-sssom-repo-label-bug] | [search][search-mapping-commons-org-label-bug] | Confirmed bugs or reports that are very likely to be bugs. |
| `question` | [search][search-sssom-repo-label-question] | [search][search-mapping-commons-org-label-question] | Questions more than bug reports or feature requests (e.g. how do I do X). |
| `feedback` | [search][search-sssom-repo-label-feedback] | [search][search-mapping-commons-org-label-feedback] | General feedback more than bug reports or feature requests. |
| `help-wanted` | [search][search-sssom-repo-label-help-wanted] | [search][search-mapping-commons-org-label-help-wanted] | The SSSOM core team would appreciate help from the community in resolving these issues. |
| `beginner` | [search][search-sssom-repo-label-beginner] | [search][search-mapping-commons-org-label-beginner] | Less complex issues which would be good first issues to work on for users who want to contribute to SSSOM. |
| `more-information-needed` | [search][search-sssom-repo-label-more-information-needed] | [search][search-mapping-commons-org-label-more-information-needed] | More information needs to be collected about these problems or feature requests (e.g. steps to reproduce). |
| `needs-reproduction` | [search][search-sssom-repo-label-needs-reproduction] | [search][search-mapping-commons-org-label-needs-reproduction] | Likely bugs, but haven't been reliably reproduced. |
| `blocked` | [search][search-sssom-repo-label-blocked] | [search][search-mapping-commons-org-label-blocked] | Issues blocked on other issues. |
| `duplicate` | [search][search-sssom-repo-label-duplicate] | [search][search-mapping-commons-org-label-duplicate] | Issues which are duplicates of other issues, i.e. they have been reported before. |
| `wontfix` | [search][search-sssom-repo-label-wontfix] | [search][search-mapping-commons-org-label-wontfix] | The SSSOM core team has decided not to fix these issues for now, either because they're working as intended or for some other reason. |

[search-sssom-repo-label-enhancement]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Aenhancement
[search-mapping-commons-org-label-enhancement]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Aenhancement
[search-sssom-repo-label-bug]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Abug
[search-mapping-commons-org-label-bug]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Abug
[search-sssom-repo-label-question]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Aquestion
[search-mapping-commons-org-label-question]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Aquestion
[search-sssom-repo-label-feedback]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Afeedback
[search-mapping-commons-org-label-feedback]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Afeedback
[search-sssom-repo-label-help-wanted]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Ahelp-wanted
[search-mapping-commons-org-label-help-wanted]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Ahelp-wanted
[search-sssom-repo-label-beginner]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Abeginner
[search-mapping-commons-org-label-beginner]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Abeginner
[search-sssom-repo-label-more-information-needed]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Amore-information-needed
[search-mapping-commons-org-label-more-information-needed]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Amore-information-needed
[search-sssom-repo-label-needs-reproduction]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Aneeds-reproduction
[search-mapping-commons-org-label-needs-reproduction]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Aneeds-reproduction
[search-sssom-repo-label-triage-help-needed]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Atriage-help-needed
[search-mapping-commons-org-label-triage-help-needed]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Atriage-help-needed
[search-sssom-repo-label-windows]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Awindows
[search-mapping-commons-org-label-windows]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Awindows
[search-sssom-repo-label-linux]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Alinux
[search-mapping-commons-org-label-linux]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Alinux
[search-sssom-repo-label-mac]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Amac
[search-mapping-commons-org-label-mac]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Amac
[search-sssom-repo-label-documentation]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Adocumentation
[search-mapping-commons-org-label-documentation]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Adocumentation
[search-sssom-repo-label-performance]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Aperformance
[search-mapping-commons-org-label-performance]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Aperformance
[search-sssom-repo-label-security]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Asecurity
[search-mapping-commons-org-label-security]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Asecurity
[search-sssom-repo-label-ui]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Aui
[search-mapping-commons-org-label-ui]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Aui
[search-sssom-repo-label-api]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Aapi
[search-mapping-commons-org-label-api]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Aapi
[search-sssom-repo-label-crash]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Acrash
[search-mapping-commons-org-label-crash]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Acrash
[search-sssom-repo-label-auto-indent]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Aauto-indent
[search-mapping-commons-org-label-auto-indent]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Aauto-indent
[search-sssom-repo-label-encoding]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Aencoding
[search-mapping-commons-org-label-encoding]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Aencoding
[search-sssom-repo-label-network]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Anetwork
[search-mapping-commons-org-label-network]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Anetwork
[search-sssom-repo-label-uncaught-exception]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Auncaught-exception
[search-mapping-commons-org-label-uncaught-exception]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Auncaught-exception
[search-sssom-repo-label-git]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Agit
[search-mapping-commons-org-label-git]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Agit
[search-sssom-repo-label-blocked]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Ablocked
[search-mapping-commons-org-label-blocked]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Ablocked
[search-sssom-repo-label-duplicate]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Aduplicate
[search-mapping-commons-org-label-duplicate]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Aduplicate
[search-sssom-repo-label-wontfix]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Awontfix
[search-mapping-commons-org-label-wontfix]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Awontfix
[search-sssom-repo-label-invalid]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Ainvalid
[search-mapping-commons-org-label-invalid]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Ainvalid
[search-sssom-repo-label-package-idea]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Apackage-idea
[search-mapping-commons-org-label-package-idea]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Apackage-idea
[search-sssom-repo-label-wrong-repo]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Awrong-repo
[search-mapping-commons-org-label-wrong-repo]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Awrong-repo
[search-sssom-repo-label-editor-rendering]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Aeditor-rendering
[search-mapping-commons-org-label-editor-rendering]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Aeditor-rendering
[search-sssom-repo-label-build-error]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Abuild-error
[search-mapping-commons-org-label-build-error]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Abuild-error
[search-sssom-repo-label-error-from-pathwatcher]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Aerror-from-pathwatcher
[search-mapping-commons-org-label-error-from-pathwatcher]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Aerror-from-pathwatcher
[search-sssom-repo-label-error-from-save]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Aerror-from-save
[search-mapping-commons-org-label-error-from-save]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Aerror-from-save
[search-sssom-repo-label-error-from-open]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Aerror-from-open
[search-mapping-commons-org-label-error-from-open]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Aerror-from-open
[search-sssom-repo-label-installer]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Ainstaller
[search-mapping-commons-org-label-installer]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Ainstaller
[search-sssom-repo-label-auto-updater]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Aauto-updater
[search-mapping-commons-org-label-auto-updater]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Aauto-updater
[search-sssom-repo-label-deprecation-help]: https://github.com/search?q=is%3Aopen+is%3Aissue+repo%3Amapping-commons%2Fsssom+label%3Adeprecation-help
[search-mapping-commons-org-label-deprecation-help]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Adeprecation-help
[search-sssom-repo-label-electron]: https://github.com/search?q=is%3Aissue+repo%3Amapping-commons%2Fsssom+is%3Aopen+label%3Aelectron
[search-mapping-commons-org-label-electron]: https://github.com/search?q=is%3Aopen+is%3Aissue+user%3Amapping-commons+label%3Aelectron
[search-sssom-repo-label-work-in-progress]: https://github.com/search?q=is%3Aopen+is%3Apr+repo%3Amapping-commons%2Fsssom+label%3Awork-in-progress
[search-mapping-commons-org-label-work-in-progress]: https://github.com/search?q=is%3Aopen+is%3Apr+user%3Amapping-commons+label%3Awork-in-progress
[search-sssom-repo-label-needs-review]: https://github.com/search?q=is%3Aopen+is%3Apr+repo%3Amapping-commons%2Fsssom+label%3Aneeds-review
[search-mapping-commons-org-label-needs-review]: https://github.com/search?q=is%3Aopen+is%3Apr+user%3Amapping-commons+label%3Aneeds-review
[search-sssom-repo-label-under-review]: https://github.com/search?q=is%3Aopen+is%3Apr+repo%3Amapping-commons%2Fsssom+label%3Aunder-review
[search-mapping-commons-org-label-under-review]: https://github.com/search?q=is%3Aopen+is%3Apr+user%3Amapping-commons+label%3Aunder-review
[search-sssom-repo-label-requires-changes]: https://github.com/search?q=is%3Aopen+is%3Apr+repo%3Amapping-commons%2Fsssom+label%3Arequires-changes
[search-mapping-commons-org-label-requires-changes]: https://github.com/search?q=is%3Aopen+is%3Apr+user%3Amapping-commons+label%3Arequires-changes
[search-sssom-repo-label-needs-testing]: https://github.com/search?q=is%3Aopen+is%3Apr+repo%3Amapping-commons%2Fsssom+label%3Aneeds-testing
[search-mapping-commons-org-label-needs-testing]: https://github.com/search?q=is%3Aopen+is%3Apr+user%3Amapping-commons+label%3Aneeds-testing

[beginner]:https://github.com/search?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3Abeginner+label%3Ahelp-wanted+user%3Amapping-commons+sort%3Acomments-desc
[help-wanted]:https://github.com/search?q=is%3Aopen+is%3Aissue+label%3Ahelp-wanted+user%3Amapping-commons+sort%3Acomments-desc+-label%3Abeginner
[contributing-to-official-sssom-packages]:https://flight-manual.sssom.io/hacking-sssom/sections/contributing-to-official-sssom-packages/
[hacking-on-sssom-core]: https://flight-manual.sssom.io/hacking-sssom/sections/hacking-on-sssom-core/

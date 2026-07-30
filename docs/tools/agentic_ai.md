# Agentic software-development tools

> **Volatile information — last reviewed 30 July 2026.**
>
> Product capabilities, interfaces, access conditions, pricing, policies, and
> maintenance status can change quickly.  Check the linked official
> documentation before using this page in a session or adopting a tool.

This page lists representative tools that can inspect a project, propose or
make changes, and use development tools on a user's behalf.  It deliberately
avoids installation commands, model names, context limits, and detailed feature
comparisons because those details have a particularly short useful life.

For the durable concepts, scientific risks, and review workflow, see
[agentic AI and scientific software](../agentic_ai.md).  Apply the general
[tool-selection criteria](choosing_tools.md) before choosing a product.


## Representative current tools

This is a starting set, not an exhaustive ranking.

| Tool | Current positioning | Points to verify for a project |
|------|---------------------|--------------------------------|
| [Codex CLI](https://learn.chatgpt.com/docs/developer-commands) | OpenAI's terminal client for interactive and non-interactive agentic software-development work.  Current documentation describes workspace-oriented operation, [repository guidance](https://learn.chatgpt.com/docs/customization/overview#agents-guidance), and sandbox and approval controls. | Check the current [security and approval model](https://learn.chatgpt.com/docs/agent-approvals-security), authentication, data policy, supported platform, and whether local or hosted operation fits the project. |
| [Claude Code](https://code.claude.com/docs/en/overview) | Anthropic's coding agent for terminal, editor, desktop, and web workflows.  It can inspect code, edit files, run commands, and integrate with development tools. | Check execution location, permission mode, account or provider requirements, organizational policy, and which project instructions and integrations will be enabled. |
| [Gemini CLI](https://geminicli.com/docs/) | Google's terminal agent for understanding code, automating tasks, and building workflows with project context.  Its documentation includes scripting, project instructions, tools, policies, and sandboxing. | Check authentication, network requirements, data terms, release channel, sandbox configuration, and compatibility with restricted or offline systems. |
| [GitHub Copilot CLI](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli) | GitHub's terminal agent for interactive or programmatic work on code and GitHub-hosted workflows. | Check the required Copilot plan and organization policy, repository and GitHub permissions, approval settings, sandbox availability, and whether the project is hosted on or integrated with GitHub. |
| [GitHub Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review) | AI-assisted review of pull-request changes.  A review can be requested manually or [configured to run automatically](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-automatic-review) when pull requests are opened, and optionally for drafts or new pushes. | Check plan and organization policy, usage costs, data handling, ruleset configuration, review instructions, and excluded files.  Its comments do not count as required approvals or block a merge, so retain human review and appropriate CI checks. |
| [Aider](https://aider.chat/docs/) | A terminal-oriented, Git-integrated AI pair-programming tool that can use several model providers.  It sits toward the interactive-assistant end of the agentic spectrum but can edit files and run project checks. | Check provider choice and data path, API-key handling, automatic commit behaviour, test and lint integration, model compatibility, and whether the desired workflow needs more or less autonomy. |

The products overlap, but their trust boundaries differ.  A terminal interface
does not imply that model inference or data processing happens locally.
Similarly, an open-source client does not by itself determine where prompts,
source code, or tool output are sent.

Pull-request code review is also a different operating mode from a coding
agent that edits a working tree.  The version-controlled change provides a
bounded difference to inspect, and the pull-request event can trigger both
review and continuous integration.  The review interprets the change and
suggests issues; continuous integration runs the project's declared checks.
They provide complementary evidence.


## Compare operating modes, not feature counts

For a representative project task, determine

* which files the tool reads and which context it sends elsewhere;
* whether commands run on the workstation, in a container, or in a hosted
  environment;
* which actions require confirmation and how permissions are scoped;
* whether network access and external integrations can be restricted;
* whether changes are easy to inspect, attribute, and reverse;
* whether repository instructions, tests, and static checks are used
  consistently;
* whether interactive and unattended modes have different safeguards; and
* which logs, transcripts, or audit records are retained and by whom.

Do not select a tool primarily because it advertises the largest number of
features or the most capable model.  A more constrained tool may be preferable
when the task is narrow, the data is sensitive, or the execution environment is
shared.


## Scientific-computing considerations

Evaluate each candidate with a realistic scientific repository rather than a
small generic coding exercise.

### Scientific correctness

Check whether the workflow makes it easy to provide and run

* known-answer and regression tests;
* numerical tolerances and invariants;
* data-validation and schema checks;
* small reference cases;
* documentation builds; and
* compiler warnings, linters, and static analysis.

These integrations make review more efficient, but no product-specific
"verification" feature should be interpreted as proof of scientific
correctness.


### Data and confidentiality

Establish which source files, prompts, test data, command output, and repository
metadata may be processed by the provider.  Check institutional policy,
contracts, data classifications, intellectual-property constraints, and
retention settings.

Do not assume that excluding files from version control also excludes them from
an agent's context.  Check the tool's own ignore, permission, and context rules.


### HPC suitability

For work involving a cluster, determine whether the tool

* can operate without direct internet access on compute nodes;
* requires installation or authentication that the site does not permit;
* understands that expensive work must go through the scheduler;
* can be prevented from reading SSH keys, tokens, unrelated storage, and other
  users' data;
* separates local edits from remote job submission and cancellation; and
* records enough compiler, library, module, accelerator, scheduler, and
  placement context to interpret results.

It may be preferable to use an agent on a workstation or controlled development
node, then submit reviewed code through the site's normal workflow.  Convenience
does not override site policy or allocation responsibility.


## A small evaluation task

This is an optional follow-up activity rather than part of the standard
four-hour session.

Evaluate candidates on a disposable branch or copy of a real project.  Give
each tool the same bounded task, such as

> Explain one calculation, add a scientifically meaningful test for an
> existing invariant, run the documented checks, and summarize the changes and
> remaining limitations.

Compare

* the correctness and relevance of the explanation;
* whether the test could actually expose a defect;
* the size and focus of the change;
* respect for repository instructions and scope;
* commands and permissions requested;
* quality of the reported limitations;
* ease of reviewing and reversing the result; and
* setup, policy, usage, and maintenance costs.

Do not use confidential data or grant broad permissions merely for an
evaluation.


## Maintenance checklist for this page

Before a training session or periodic tool review:

1. open every official documentation link;
2. confirm that the product and named surface are still maintained;
3. check whether the description of local, hosted, interactive, and
   non-interactive operation remains accurate;
4. review current permission, sandbox, data, account, and platform
   documentation;
5. remove deprecated terminology, commands, model names, and access claims;
6. add or remove candidates only when that improves the range of relevant
   choices; and
7. update the review date and summarize material changes in version control.

Stable selection principles belong in [choosing development
tools](choosing_tools.md) or the conceptual [agentic AI
chapter](../agentic_ai.md), not on this volatile page.

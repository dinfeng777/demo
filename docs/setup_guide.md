# Meta-Agent Setup Guide

This guide will detail the steps required to set up the development environment for the Meta-Agent project. (Details to be added as the project evolves, particularly after language and dependency choices are finalized in Step 2).

## Python Environment Setup

This project uses Python. We recommend using Python 3.10 or newer.

### 1. Create a Virtual Environment

A virtual environment helps manage project-specific dependencies. Create one in the project root:

```bash
python -m venv .venv
```
Replace `python` with `python3` if necessary, depending on your system's Python installation.

### 2. Activate the Virtual Environment

Before installing dependencies or running the project, activate the virtual environment:

-   **Linux/macOS:**
    ```bash
    source .venv/bin/activate
    ```
-   **Windows (Command Prompt/PowerShell):**
    ```bash
    .venv\Scripts\activate
    ```

You should see the virtual environment's name (e.g., `(.venv)`) prefixed to your shell prompt.

### 3. Install Dependencies

Project dependencies are listed in `requirements.txt`. Install them using pip:

```bash
pip install -r requirements.txt
```
Ensure your virtual environment is activated before running this command. This will install all necessary packages, including `pytest` for running our test suite.

### 4. Running Tests

Once dependencies are installed, you can run the project's test suite using `pytest`. Navigate to the project root directory in your terminal and execute:

```bash
python -m pytest
```
Or simply:
```bash
pytest
```
This command will automatically discover and run all tests located in the `tests` directory. Ensure your virtual environment is activated.

## Copilot Coding Agent Onboarding Manual

This section is based on the "Copilot Coding Agent 上岗手册" from the `MetaAgent_Full_Plan.md`. It describes how to integrate GitHub Copilot as an AI coding agent for specific tasks.

### 0. Prerequisites

-   GitHub Enterprise/Team account with Copilot licenses enabled.
-   A repository (even a simple "hello-world" one) ready for the agent.
-   Sufficient GitHub Actions minutes (estimate ≥ 50 min for initial setup and tests).

### 1. Enable the Coding Agent Feature

-   Navigate to your GitHub `Settings`.
-   Go to `Copilot` -> `Features`.
-   Check the box for "Copilot Coding Agent (Preview)".

### 2. Labeling Conventions for Issues

To effectively manage tasks for the Copilot Agent, use the following labels:

-   `assign-to-copilot`: Assigns the issue directly to the Copilot Agent.
-   `backlog/tech-debt`: Marks issues related to technical debt or backlog items that the agent might address.
-   `needs-human-review`: Indicates that an agent's pull request or work requires human oversight and approval.

### 3. Issue Template for Agent Tasks

Create an issue template in your repository at `.github/ISSUE_TEMPLATE/agent_task.yml` with the following content:

```yaml
name: 🤖 Agent 任务
labels: ["assign-to-copilot"]
body:
  - type: textarea
    id: task
    attributes:
      label: 📋 任务描述
      placeholder: 例如：升级到 Next.js 15 并修复 TypeScript 报错…
    validations: { required: true }
  - type: input
    id: success
    attributes:
      label: ✅ 完成判据
      placeholder: 测试全绿 + 覆盖率 ≥85%
    validations: { required: true }
```

### 4. CI Workflow

Our project includes a Continuous Integration (CI) workflow defined in `.github/workflows/ci.yml`. This workflow is automatically triggered on pushes and pull requests to the `main` branch.

**Purpose of the CI Workflow:**
-   **Automated Testing**: Ensures that all tests pass before code is merged.
-   **Code Quality**: Can be extended to include linters and other quality checks.
-   **Consistency**: Provides a consistent environment for testing.

**Key Steps in the CI Workflow (`.github/workflows/ci.yml`):**
1.  **Checkout Code**: Fetches the latest code from the repository.
2.  **Set up Python**: Configures the specified Python version (e.g., 3.10).
3.  **Install Dependencies**: Installs all dependencies listed in `requirements.txt` using `pip`.
4.  **Run Tests**: Executes the test suite using `python -m pytest`.

This CI setup helps maintain code quality and ensures that changes integrate smoothly. The "Copilot Coding Agent" may also leverage this or a similar CI when it makes contributions, ensuring its generated code also meets project standards.

### 5. Initial Issues to Test Copilot Agent Setup

As suggested in the full plan, you can create these initial issues to verify the agent's integration:

| # | Title                         | Label                |
|---|-------------------------------|----------------------|
| 1 | feat/langgraph-dag-skeleton   | assign-to-copilot    |
| 2 | ci/spacelift-template         | assign-to-copilot    |
| 3 | backlog/upgrade-deps          | backlog/tech-debt    |

## Further Setup Details

(More details on setting up LangGraph, Flowise, AI Foundry connections, Weaviate, Spacelift, etc., will be added here as the project progresses and these components are actively integrated.)

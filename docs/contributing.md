# Contributing to the Meta-Agent Project

We welcome contributions to the Meta-Agent project! This document outlines our development practices, including coding standards, the Test-Driven Development (TDD) process, and how to submit changes.

## Test-Driven Development (TDD)

This project follows a Test-Driven Development approach to ensure code quality and maintainability.

### TDD Workflow

The basic TDD workflow is as follows:

1.  **Write a Failing Test**: Before writing any implementation code, write a test case that describes a small piece of desired functionality or reproduces a bug. This test should fail initially because the code it's testing doesn't exist or is incorrect.
2.  **Write Minimal Code to Pass**: Write only the code necessary to make the failing test pass. Avoid adding extra functionality at this stage. The goal is to get a green bar from your test runner quickly.
3.  **Refactor**: Once the test is passing, look for opportunities to improve the code's structure, readability, or performance without changing its external behavior. Ensure all tests still pass after refactoring.

Repeat this cycle for each new piece of functionality.

### Testing Framework: `pytest`

-   We use `pytest` as our primary testing framework.
-   All test files should be placed in the `/tests` directory at the project root.
-   Test files should typically be named `test_*.py` or `*_test.py`.
-   Test functions within these files should be named `test_*`.

### Running Tests

To run the test suite, navigate to the project root directory in your terminal (ensure your virtual environment is activated and dependencies are installed) and execute:

```bash
python -m pytest
```

Or simply:

```bash
pytest
```

This command will automatically discover and run all tests in the `tests` directory.

## Coding Standards

Follow PEP 8 guidelines for Python code. Aim for clear, readable, and maintainable code. (More specific standards, including preferred linting and formatting tools like Black or Flake8, may be added as the project evolves).

## Branching Strategy

Propose changes via feature branches. Name branches descriptively (e.g., `feature/name-of-feature`, `fix/issue-number`). Create pull requests to the `main` branch for review. (Further details, such as specific naming conventions or integration branches, may be added later).

## Pull Request (PR) Process

Ensure all tests pass locally before submitting a PR. Provide a clear description of changes in the PR. Link to relevant issues if any. (Additional requirements, such as reviewer assignments or PR templates, may be specified later).

## Reporting Bugs

Use the GitHub Issues tracker to report bugs. Provide detailed steps to reproduce, expected behavior, and actual behavior. Include information about your environment (e.g., Python version, OS) if relevant.

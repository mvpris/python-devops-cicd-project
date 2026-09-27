# Python for DevOps: CI/CD for Python Projects

This repo contains the code for the CI/CD section of my Python for DevOps course.

The developed package `simple-http-checker-d-superteach` is a simple CLI tool to check the status of URLs. A CI/CD pipeline is showcased by building, testing and deploying the package by using an automated GitHub Actions workflow.

## What I implement in this project

- [x] Implement the project (code files)
- [x] Add a simple `GitHub Actions` workflow and make sure it runs until completion
- [x] Add lint (`ruff`) and format (`black`) checks
- [x] Add type (`mypy`) and security (`bandit`) checks
- [x] Add test automation (`pytest`)
- [x] Build the project (`build`, `python-semantic-release`)
- [x] Publish the project to both `TestPyPI` and `PyPI` when a new tag is pushed

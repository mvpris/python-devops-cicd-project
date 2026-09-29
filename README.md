# simple-http-checker

[![CI](https://github.com/mvpris/python-devops-cicd-project/actions/workflows/python-ci.yaml/badge.svg?branch=main)](https://github.com/mvpris/python-devops-cicd-project/actions/workflows/python-ci.yaml)
[![Publish](https://github.com/mvpris/python-devops-cicd-project/actions/workflows/publish.yaml/badge.svg)](https://github.com/mvpris/python-devops-cicd-project/actions/workflows/publish.yaml)
[![PyPI](https://img.shields.io/pypi/v/simple-http-checker-d-superteach)](https://pypi.org/project/simple-http-checker-d-superteach/)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)](https://github.com/mvpris/python-devops-cicd-project/blob/main/pyproject.toml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](https://github.com/mvpris/python-devops-cicd-project/blob/main/LICENSE)

A small command-line tool that checks the HTTP status of one or more URLs, and a fully automated pipeline that lints, type-checks, security-scans, tests, versions and publishes it to PyPI on every push to `main`.

The tool is deliberately small: the point of the project is the pipeline around it. Built as the CI/CD project of Lauro Fialho Müller's *Python for DevOps: Mastering Real-World Automation* course.

## Installation

```bash
pip install simple-http-checker-d-superteach
```

For a command-line tool, an isolated install keeps its dependencies out of your other environments:

```bash
uv tool install simple-http-checker-d-superteach
# or
pipx install simple-http-checker-d-superteach
```

Either way you get one command, `check-urls`. Requires Python 3.10 or newer.

## Usage

```console
$ check-urls --help
Usage: check-urls [OPTIONS] [URLS]...

Options:
  -t, --timeout INTEGER  Timeout in seconds for each request.
  -v, --verbose          Enable debug logging.
  --help                 Show this message and exit.
```

Check several URLs in one run:

```console
$ check-urls https://github.com https://pypi.org https://github.com/mvpris/no-such-repo https://no-such-host.invalid
[2026-09-29 15:15:03] INFO     simple_http_checker.cli: Starting check for 4 URLs.
[2026-09-29 15:15:03] INFO     simple_http_checker.checker: Starting check for 4 URLs with a timeout of 5 s.
[2026-09-29 15:15:03] WARNING  simple_http_checker.checker: Connection error for https://no-such-host.invalid
[2026-09-29 15:15:03] INFO     simple_http_checker.checker: URL check finished.

--- RESULTS ---
https://github.com                       -> 200 OK
https://pypi.org                         -> 200 OK
https://github.com/mvpris/no-such-repo   -> 404 Not Found
https://no-such-host.invalid             -> CONNECTION_ERROR
```

Log lines go to `stderr` and the results table to `stdout`, so appending `2>/dev/null` leaves only the table. Use `-t/--timeout` to change the per-request timeout (default: 5 s) and `-v/--verbose` for debug logs, including each request as it is made.

Each URL gets one of these statuses:

| Status | Meaning |
| --- | --- |
| `<code> OK` | The final response had a status code below 400 (redirects are followed). |
| `<code> <reason>` | The server answered with a 4xx or 5xx, e.g. `404 Not Found`. |
| `TIMEOUT` | Connecting, or waiting for data from the server, took longer than the timeout. |
| `CONNECTION_ERROR` | The DNS lookup failed, the connection was refused, or the TLS handshake failed. |
| `REQUEST_ERROR: <type>` | Any other `requests` error, e.g. `MissingSchema` for a URL without `https://`. Logged with a full traceback. |

## How the pipeline works

Two GitHub Actions workflows take every change from commit to PyPI with no manual steps.

```console
push to main
 └─ python-ci.yaml
     ├─ checks    ruff · black --check · mypy · bandit
     ├─ tests     pytest on Python 3.10, 3.11 and 3.12
     └─ release   runs only if both jobs above pass
                  python-semantic-release: version bump, CHANGELOG,
                  git tag, GitHub Release with wheel + sdist attached
                        │
                        │  release: published
                        ▼
    publish.yaml
     ├─ TestPyPI  uploads the wheel + sdist attached to the release
     └─ PyPI      runs only if the TestPyPI upload succeeds
```

Design decisions:

- **Versions come from commit messages.** Commits follow [Conventional Commits](https://www.conventionalcommits.org/). python-semantic-release reads them to pick the next version (`feat` → minor, `fix`/`perf` → patch), updates `pyproject.toml` and `CHANGELOG.md`, tags the commit and creates the GitHub Release. Release commits carry `[skip ci]` so they don't trigger another run.
- **Build once, publish the same files.** The wheel and sdist are built once, during the release, and attached to the GitHub Release. The publish workflow downloads those exact files instead of rebuilding, so what lands on PyPI is byte-identical to the release assets.
- **Staged promotion.** Packages go to TestPyPI first and to PyPI only after that succeeds. Each publish job runs in its own GitHub Environment (`development`, `production`).
- **No stored PyPI credentials.** Publishing uses [PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/): each job gets a short-lived OIDC token from GitHub instead of reading an API token from repository secrets.
- **A personal access token only where it is required.** Events created with the default `GITHUB_TOKEN` don't start new workflow runs, so the release job authenticates with a PAT. Otherwise `release: published` would never trigger `publish.yaml`.
- **Tests never touch the network.** `requests.get` is mocked with `pytest-mock` and the CLI is exercised through Click's `CliRunner`, so the suite is fast and deterministic. The version matrix runs with `fail-fast: false`, so a failure on one Python version doesn't hide the results of the others.

## Development

```bash
git clone https://github.com/mvpris/python-devops-cicd-project.git
cd python-devops-cicd-project
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Run the same checks CI runs:

```bash
ruff check .
black --check .
mypy src/
bandit -c pyproject.toml -r .
pytest
```

Commit messages must follow Conventional Commits (`feat:`, `fix:`, `docs:`, `ci:`, …) because the type decides whether a push to `main` publishes a new version.

Project layout:

```bash
.
├── .github/workflows/
│   ├── python-ci.yaml         # checks, tests, release
│   └── publish.yaml           # TestPyPI → PyPI
├── src/simple_http_checker/
│   ├── checker.py             # check_urls(): the HTTP logic
│   └── cli.py                 # Click entry point for check-urls
├── tests/
│   ├── test_checker.py
│   └── test_cli.py
├── CHANGELOG.md               # generated by python-semantic-release
├── PLAN.md                    # original requirements
└── pyproject.toml             # metadata, dependencies, tool configuration
```

The `src/` layout keeps the package off the import path until it is installed, so CI tests the package the way users receive it.

## Known limitations

- The exit status is always 0, even when some URLs fail, so the tool can't yet gate a script or CI job.
- URLs are checked sequentially, so slow hosts add up on long lists.

## License

[MIT](https://github.com/mvpris/python-devops-cicd-project/blob/main/LICENSE)

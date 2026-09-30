# CHANGELOG

<!-- version list -->

## v1.2.5 (2026-09-30)

### Bug Fixes

- **python-cicd**: Fix typo for bandit tool config in project metadata
  ([`198fe04`](https://github.com/mvpris/python-devops-cicd-project/commit/198fe04ca478c1ea3020d30d501bfa0cfb3be5c3))


## v1.2.4 (2026-09-29)

### Bug Fixes

- **python-cicd**: Configure logging in main() instead of at import time
  ([`951cf9a`](https://github.com/mvpris/python-devops-cicd-project/commit/951cf9abbf082753e9f1aefb2d0df9ed1b6bc4d1))

### Build System

- **python-cicd**: Declare MIT license in project metadata
  ([`c21fdda`](https://github.com/mvpris/python-devops-cicd-project/commit/c21fdda868642eaa8f283beeb11765c4e8e72823))

### Chores

- **python-cicd**: Update .gitignore to ignore practice dir
  ([`bd01479`](https://github.com/mvpris/python-devops-cicd-project/commit/bd014797fc6942b76e01e315dcc16a2787b9d9ea))

### Continuous Integration

- **python-cicd**: Remove unused id-token permission from release job
  ([`a27f73c`](https://github.com/mvpris/python-devops-cicd-project/commit/a27f73cb7dc5121e944e9878381e460146ed5396))

- **python-cicd**: Replace 3rd-party release-downloader action with gh CLI
  ([`741f25c`](https://github.com/mvpris/python-devops-cicd-project/commit/741f25c668fb1a682787fc5f0f952d6265589822))

- **python-cicd**: Skip existing files in PyPI publish job
  ([`dd93d2c`](https://github.com/mvpris/python-devops-cicd-project/commit/dd93d2c826584b5f1edbc8c27c3ea5b4d2a76248))

### Documentation

- **python-cicd**: Rewrite README with install, usage and pipeline docs
  ([`749e65c`](https://github.com/mvpris/python-devops-cicd-project/commit/749e65c55310a0bc0d94d9d2edc7d467650366f1))

- **python-cicd**: Update PLAN.md to show Python 3.10+ compatibility
  ([`8279839`](https://github.com/mvpris/python-devops-cicd-project/commit/8279839ffd3c41557b0a248d8ad1ba3dbf30936e))


## v1.2.3 (2026-09-27)

### Bug Fixes

- **python-cicd**: Force a patch release bump to publish updates to PyPI
  ([`4eae4c6`](https://github.com/mvpris/python-devops-cicd-project/commit/4eae4c684e46c6d47dce0e9a3cb0e57bb48a2865))

### Continuous Integration

- **python-cicd**: Rename job publish-pypi in workflow and update README
  ([`1ca08c9`](https://github.com/mvpris/python-devops-cicd-project/commit/1ca08c90cc378d056a807ff0fab075be03ce2c88))


## v1.2.2 (2026-09-27)

### Bug Fixes

- **python-cicd**: Update README.md with all project tasks completed
  ([`5be5d17`](https://github.com/mvpris/python-devops-cicd-project/commit/5be5d170a497e69338d13133489e39acf7aaf213))


## v1.2.1 (2026-09-27)

### Performance Improvements

- **python-cicd**: Dedup build logic and download artifacts from release
  ([`26a7ac1`](https://github.com/mvpris/python-devops-cicd-project/commit/26a7ac1a3d4481bbddc9a290fed25ee5fd3de17b))


## v1.2.0 (2026-09-27)

### Features

- **python-cicd**: Add publish to PyPI job to publish workflow
  ([`4470321`](https://github.com/mvpris/python-devops-cicd-project/commit/4470321f3024a5d2b5fbfd751a8f101b1ef6cec8))


## v1.1.5 (2026-09-26)

### Bug Fixes

- **python-cicd**: Try fixing publish to TestPyPI by renaming project 2
  ([`3803bd7`](https://github.com/mvpris/python-devops-cicd-project/commit/3803bd7c6a9814c271a4a1f9f595d151524d6cd8))


## v1.1.4 (2026-09-26)

### Bug Fixes

- **python-cicd**: Try fixing publish to TestPyPI by renaming project
  ([`1f34229`](https://github.com/mvpris/python-devops-cicd-project/commit/1f34229ba319984d2727103a348f887269348c0e))


## v1.1.3 (2026-09-26)

### Bug Fixes

- **python-cicd**: Try fixing publish workflow by matching package name
  ([`411c0e7`](https://github.com/mvpris/python-devops-cicd-project/commit/411c0e75b0388de3520fe8d5d518fc18626aa82d))


## v1.1.2 (2026-09-26)

### Bug Fixes

- **python-cicd**: Fix publish workflow by adding trailing slash to url
  ([`4f2b8c6`](https://github.com/mvpris/python-devops-cicd-project/commit/4f2b8c698158bb464ba7fb59a5003e5f95557bbe))


## v1.1.1 (2026-09-26)

### Bug Fixes

- **python-cicd**: Add correct environment
  ([`eca0c9a`](https://github.com/mvpris/python-devops-cicd-project/commit/eca0c9adc16b7055e6be2f7315be711e8ffa96e5))


## v1.1.0 (2026-09-26)

### Features

- **python-cicd**: Add publish workflow
  ([`15069c1`](https://github.com/mvpris/python-devops-cicd-project/commit/15069c161a36cb357f594506d76037345ec13749))


## v1.0.0 (2026-09-26)

- Initial Release

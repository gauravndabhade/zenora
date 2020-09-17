# Contributing to Zenora

When contributing to this repository, please first discuss the change you wish to make via issue,
messaging, or any other method with the owners of this repository before making a change.

Please note we have a code of conduct, please follow it in all your interactions with the project.

# Environment Setup

Make sure you have at least Python 3.6 already installed to continue setting up the development
environment for Zenora.

Once you have cloned the repo, open your terminal/console in that folder and type the following command

```bash
python setupproject.py
```

This script will download all requirements including development dependencies and also install the linters
and formatters, Flake8 and Black. Once it's finished running, you are all set up to develop Zenora.

## Pull Request Process

1. Ensure any install/build dependencies and test files are in the `.gitignore` file or removed before doing a
   pull request.
2. Update the documentation and changelog in the `docs/` folder with details of changes to the interface, this
   includes new environment variables, exposed ports, useful file locations and container parameters.

3. Increase the version numbers in any examples files, the README.md, setup.py and documentation to the new version that this pull request would represent.

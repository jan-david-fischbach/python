"""This module is called after project is created."""
from typing import List

import textwrap
from pathlib import Path
from shutil import move, rmtree
import subprocess

# Project root directory
PROJECT_DIRECTORY = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.package_name }}"
PROJECT_MODULE = (
    "{{ cookiecutter.package_name.lower().replace(' ', '_').replace('-', '_') }}"
)
CICD = "{{ cookiecutter.cicd }}"

# Values to generate github repository
GIT_REMOTE = "{{ cookiecutter.git_remote }}"


def remove_unused_files(
    directory: Path, module_name: str, cicd: str = "github"
) -> None:
    """Remove unused files.

    Args:
        directory: path to the project directory
        module_name: project module name
    """
    if cicd == "github":
        files_to_delete = [directory / ".gitlab-ci.yml"]

        for path in files_to_delete:
            path.unlink()
    else:
        dirpath = directory / ".github"
        rmtree(dirpath)


def print_futher_instuctions(package_name: str, remote: str) -> None:
    """Show user what to do next after project creation.

    Args:
        package_name: current project name
        github: GitHub username
    """
    message = f"""
    Your project {package_name} is created.

    1) Now you can start working on it:

        $ cd {package_name}

    2) install package in developer mode

        $ pip install -e .[dev]

    3) Upload initial code to GitHub:

        $ git init
        $ git add .
        $ git commit -m ":tada: Initial commit"
        $ git branch -M main
        $ git remote add origin {remote}
        $ git push -u origin main
    """
    print(textwrap.dedent(message))

def run_setup(package_name: str, remote: str) -> None:
    subprocess.call(['pip', 'install', "-e", ".[dev]"])

    subprocess.call(['git', 'init'])
    subprocess.call(['pre-commit', 'install'])

    subprocess.call(['git', 'add', '.'])
    subprocess.call(['git', 'commit', '-m', ':tada: Initial commit'])
    subprocess.call(['git', 'remote', 'add', 'origin', remote])
    subprocess.call(['git', 'push', '-u', 'origin', 'main'])


def main() -> None:
    remove_unused_files(
        directory=PROJECT_DIRECTORY,
        module_name=PROJECT_MODULE,
        cicd=CICD,
    )
    run_setup(package_name=PROJECT_NAME, remote=GIT_REMOTE)


if __name__ == "__main__":
    main()

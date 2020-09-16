import subprocess
import sys
import os
import zenora


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


print(
    f"\n\n \033[93m ✥ Setting up development environment Zenora {zenora.__version__} ✥ \033[0m\n\n"
)

subprocess.check_call(
    [
        sys.executable,
        "-m",
        "pip",
        "install",
        "-r",
        "requirements.txt",
        "-r",
        "dev-requirements.txt",
    ]
)

print(os.popen("pre-commit install").read())

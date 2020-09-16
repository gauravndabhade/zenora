import subprocess
import sys
import os
import zenora


print(
    f"\n\n \033[93m ✥ Setting up development environment for Zenora {zenora.__version__} ✥ \033[0m\n\n"
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


print(
    f"\n\n\n\033[93m ✥ Succesfully finished setting up development environment for Zenora {zenora.__version__} ✥ \033[0m\n\n"
)

# The idea of this file is to enable running the package with
# `python -m awslimitchecker` or `python -m awslimitchecker [args]`.
# This enables debugging the package when installed in editable mode
# (`pip install -e .`) and running the package from the command line.

import sys

from . import runner


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    # Parse arguments and run your package's main functionality
    print("Running awslimitchecker with arguments:", args)
    runner.console_entry_point()


if __name__ == "__main__":
    main()

import argparse
import os
import sys

from pathlib import Path

import pytest
import stackprinter


def main(test_file: Path, solution_file: Path):
    import importlib.util
    import stackprinter

    # Always use pretty printed output for errors, but only show errors in the test file.
    stackprinter.set_excepthook(style='darkbg2', add_summary=False, suppressed_paths=[
        f"^(?!.*{test_file}).*"
    ])

    # The string "solution" is purely documentation, it doesn't really change anything.
    spec = importlib.util.spec_from_file_location("solution", solution_file)
    solution_file = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_file)
    solution_file.run_test(test_file)


def file_path(string: str):
    if os.path.isfile(string):
        return Path(string)
    else:
        raise ValueError(f"{string} is not a file.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser('pifm_runner')
    parser.add_argument('test_file', type=file_path)
    parser.add_argument('solution_file', type=file_path)
    args = parser.parse_args()
    main(args.test_file, args.solution_file)

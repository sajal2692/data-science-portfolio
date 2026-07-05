"""Execute the CI-safe notebooks headlessly and fail if any cell errors.

Each notebook runs with its own directory as the working directory, so relative
data paths and local `visuals.py` imports resolve.

A few notebooks are skipped in CI because they are too slow on a CPU runner or
too network/download-heavy; they are validated locally instead:
  - the MNIST CNN (12 epochs of training),
  - finding_donors (a large grid search),
  - the sentiment notebook (full WordNet loop + a ~500MB transformer download),
  - CLIR (two IBM Model 1 trainings over the Europarl bitext).
"""
import glob
import os
import sys

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

SKIP = {
    "digit_recognition-mnist-sequence.ipynb",
    "finding_donors/finding_donors.ipynb",
    "3-Way Sentiment Analysis for Tweets.ipynb",
    "Cross Language Information Retrieval.ipynb",
}


def ci_notebooks():
    for path in sorted(glob.glob("**/*.ipynb", recursive=True)):
        if ".ipynb_checkpoints" in path or path in SKIP:
            continue
        yield path


def main():
    failures = []
    for path in ci_notebooks():
        print(f"::group::execute {path}")
        nb = nbformat.read(path, as_version=4)
        workdir = os.path.dirname(os.path.abspath(path))
        client = NotebookClient(
            nb, timeout=600, kernel_name="python3",
            resources={"metadata": {"path": workdir}},
        )
        try:
            client.execute()
            print(f"OK: {path}")
        except CellExecutionError as exc:
            print(f"FAILED: {path}\n{exc}")
            failures.append(path)
        print("::endgroup::")

    if failures:
        print(f"\n{len(failures)} notebook(s) failed: {failures}")
        sys.exit(1)
    print("\nAll CI notebooks executed cleanly.")


if __name__ == "__main__":
    main()

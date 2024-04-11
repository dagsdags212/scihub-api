from pathlib import Path
import sys

def extract_doi(filepath: Path, verbose: bool=False) -> list[str]:
    """Extracts a series of DOIs from a text file."""
    dois = []
    prefix = "https://doi.org/"
    try:
        with open(filepath, "r") as f:
            for line in f.readlines():
                if line.startswith(prefix):
                    line = line.replace(prefix, "")
                else:
                    dois.append(line.strip())
        f.close()
    except FileNotFoundError as err:
        print(err)
        sys.exit(1)
    if verbose:
        print(f"Detected {len(dois)} articles from file.")
    return dois

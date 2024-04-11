import argparse

arg_parser = argparse.ArgumentParser(
    prog="scihub-api",
    description="a CLI tool for downloading articles from Scihub",
)

arg_parser.add_argument("-d", "--doi", type=str)
arg_parser.add_argument("-i", "--input", type=str)
arg_parser.add_argument("-o", "--outdir", type=str)
arg_parser.add_argument("--citation", action="store_true")
arg_parser.add_argument("--verbose", action="store_true")

CLI_ARGS = arg_parser.parse_args()

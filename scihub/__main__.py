import os
import sys
import asyncio
from httpx import AsyncClient
from scihub.cli import CLI_ARGS
from scihub.helpers.client import fetch_article
from scihub.helpers.article_parser import extract_doi


def main() -> None:
    args = CLI_ARGS
    client = AsyncClient()
    # file that lists DOI is provided
    if args.input:
        assert os.path.isfile(args.input), "Invalid input file"
        doi_list = extract_doi(args.input, verbose=args.verbose)
        articles = asyncio.run(fetch_article(doi_list, client=client))
        print(f"Collection {len(articles)} articles.")
    else:
        # fetch a single article
        articles = asyncio.run(fetch_article(args.doi, client=client))

    if args.citation:
        # print out APA citation(s)
        for article in articles:
            print(article.citation)
        sys.exit(0)
    elif args.outdir:
        # download file
        pass

if __name__ == "__main__":
    main()

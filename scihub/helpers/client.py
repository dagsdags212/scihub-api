import os
from pathlib import Path
import asyncio
import httpx
from scihub.classes.Article import Article
from scihub.classes.Parser import ArticleParser
from scihub.env import DEFAULT_DOWNLOAD_DIR


async def _get(url: str, client: httpx.Client, params: dict[str, str]={}) -> httpx.Response:
    resp = await client.get(url, params=params)
    resp.raise_for_status()
    return resp

async def fetch_article(
        doi: [str, list[str]],
        client: httpx.Client,
        verbose: bool=False) -> list[Article]:
    """
    Uses an open TCP connection to send a request to Scihub in order to retrieve
    information on an article with the passed `doi`.
    """
    ROOT_URL = "https://sci-hub.se"
    if isinstance(doi, str):
        urls = [f"{ROOT_URL}/{doi}"]
    elif isinstance(doi, list):
        urls = [f"{ROOT_URL}/{d}" for d in doi]
    resp = await asyncio.gather(*[_get(url, client) for url in urls])
    parsers = [ArticleParser(r.text) for r in resp]
    articles = [p.parse() for p in parsers]
    return articles

async def download_article(article: Article, path: Path=None) -> None:
    """Fetches the article to be stored locally."""
    if not path:
        # download article to the default directory stored as env variable
        path = DEFAULT_DOWNLOAD_DIR
    assert os.path.isdir(path), "Invalid path"
    if article.download_url.startswith("//"):
        url = f"https:{article.download_url}"
    else:
        url = f"https://sci-hub.se{article.download_url}"
    resp = httpx.get(url, timeout=5.0)
    filename = article.doi.split("/")[0]
    with open(f"{path}/{filename}.pdf", "wb") as f:
        f.write(resp.content)
    f.close()
    print(f"Downloaded article with doi: {article.doi}")

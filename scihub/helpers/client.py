import asyncio
import httpx
from scihub.classes.Article import Article
from scihub.classes.Parser import ArticleParser


async def _get(url: str, client: httpx.Client, params: dict[str, str]={}) -> httpx.Response:
    resp = await client.get(url, params=params)
    resp.raise_for_status()
    return resp

async def fetch_article(doi: [str, list[str]], client: httpx.Client, verbose: bool=False) -> Article:
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
    if len(articles) == 1:
        return articles[0]
    return articles


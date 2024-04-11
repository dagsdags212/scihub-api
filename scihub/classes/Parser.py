import sys
from pathlib import Path
from bs4 import BeautifulSoup
from scihub.classes.SelectorTree import SelectorTree
from scihub.classes.Article import Article
from scihub.classes.CustomErrors import ArticleNotFoundError


class HTMLParser:
    """
    Base class for parsing HTML files.

    Parameters
    ==========
    >>> html (str)  : a string representing the text from a Response object
    >>> tree (dict) : a dictionary containing selectors for parsing field
    """

    def __init__(self, html: str, tree: dict[str, str]) -> None:
        # TODO
            # create an HTMLString type
            # create a Tree type
        self.tree = tree
        self.soup = self._generate_soup(html)

    def _generate_soup(self, html: str) -> BeautifulSoup:
        """Generate a BeautifulSoup object from an HTML string."""
        return BeautifulSoup(html, "html.parser")

    def parse(self) -> None:
        """To be implemented by subclasses."""
        raise NotImplementedError

class ArticleParser(HTMLParser):
    """Wrapper class for parsing article fields."""

    def __init__(self, html: str) -> None:
        super().__init__(html, SelectorTree.ARTICLE)

    def decompose_citation(self, citation: str) -> dict:
        # TODO
        raise NotImplementedError

    def parse(self) -> Article:
        """
        Extracts the `citation`, `doi`, `download_url` fields 
        of an HTML string.

        Returns an Article object.
        """
        soup = self.soup
        tree = self.tree
        error = soup.select(tree["404"])
        if len(error) > 0:
            raise ArticleNotFoundError
        citation = soup.select(tree["citation"])[0].text.strip()
        doi = soup.select(tree["doi"])[0].text.strip()
        download_url = soup.select(tree["download_path"])[0].get("src")

        return Article(citation=citation, download_url=download_url, doi=doi)

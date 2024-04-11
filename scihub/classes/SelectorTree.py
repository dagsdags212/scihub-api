URL_TREE = {
    "root": "https://sci-hub.se/",
}

ARTICLE_TREE = {
    "citation": "div#citation",
    "doi": "div#doi",
    "download_path": "div#article embed", 
    "404": "p#smile"
}

class SelectorTree:
    """
    Each tree represents a dictionary containing path selectors for parsing
    HTML files.
    """
    URL     = URL_TREE
    ARTICLE = ARTICLE_TREE


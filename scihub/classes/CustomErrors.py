class ArticleNotFoundError(Exception):
    """Raised when Scihub is unable to retrieve an article from a given doi."""
    def __init__(self, message="Article not found"):
        self.message = message
        super().__init__(message)


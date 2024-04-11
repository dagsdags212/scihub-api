from pydantic import BaseModel

class Author(BaseModel):
    """Contains fields for representing an author."""
    first_name: str
    surname: str

    def __repr__(self) -> str:
        return f"{self.first_name} {self.surname}"

    def __str__(self) -> str:
        return f"{self.first_name } {self.surname}"

class Citation(BaseModel):
    """Contains fields for citing an article."""
    title: str
    publication_year: int
    journal: str
    volume: int
    issue: int
    doi: str
    authors: list[Author]

class Article(BaseModel):
    """Contains article metadata."""
    citation: str
    download_url: str
    doi: str



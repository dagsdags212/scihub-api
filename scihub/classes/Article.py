from pydantic import BaseModel
from typing import Tuple

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
    raw: str
    title: str
    publication_year: int
    journal: str
    doi: str
    authors: list[str]

class Article(BaseModel):
    """Contains article metadata."""
    citation: Citation
    download_url: str
    doi: str



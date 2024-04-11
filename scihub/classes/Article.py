from typing import Optional
from pydantic import BaseModel, Field

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
    title: Optional[str | None]             = Field(default=None)
    publication_year: Optional[int | None]  = Field(default=None)
    journal: Optional[str | None]           = Field(default=None)
    doi: Optional[str | None]               = Field(default=None)
    authors: Optional[list[str]]            = Field(default_factor=list)

    def __str__(self) -> str:
        return self.raw

class Article(BaseModel):
    """Contains article metadata."""
    citation: Citation
    download_url: str
    doi: str



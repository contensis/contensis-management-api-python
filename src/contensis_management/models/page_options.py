"""Module for PageOptions model."""

from pydantic import Field

from contensis_management.models import camel_case


class PageOptions(camel_case.CamelModel):
    """Options for a paged list."""

    page: int = Field(0, ge=0, description="The current page number (starting from 0).")
    page_size: int = Field(
        20,
        gt=0,
        le=100,
        description="The number of items per page (default 20, maximum 100).",
    )

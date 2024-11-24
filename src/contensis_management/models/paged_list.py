"""A paged list for when a lot of stuff is coming back from the API."""

from typing import Generic, List, TypeVar

from pydantic import Field

from contensis_management.models import camel_case

T = TypeVar("T")  # Generic type for the items in the PagedList


class PagedList(camel_case.CamelModel, Generic[T]):
    """A paged list for when a lot of stuff is coming back from the API."""

    items: List[T] = Field(..., description="The list of items on the current page.")
    total_count: int = Field(..., ge=0, description="The total number of items.")
    page: int = Field(0, ge=0, description="The current page index (zero-based).")
    page_size: int = Field(20, gt=0, description="The number of items per page.")

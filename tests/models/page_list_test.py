"""Confirm that the PageList model works as expected."""

from contensis_management.models import paged_list


def test_page_list():
    """Test the PageList model."""
    # Arrange
    items = [1, 2, 3]
    total_count = 3
    page = 0
    page_size = 20
    # Act
    page_list = paged_list.PagedList[int](
        items=items, total_count=total_count, page=page, page_size=page_size
    )
    # Assert
    assert page_list.items == items
    assert page_list.total_count == total_count
    assert page_list.page == page
    assert page_list.page_size == page_size

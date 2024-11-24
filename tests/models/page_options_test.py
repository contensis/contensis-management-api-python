"""Confirm that the PageOptions model works as expected."""

from contensis_management.models import page_options


def test_page_options():
    """Test the PageOptions model."""
    # Arrange
    page = 0
    page_size = 20
    # Act
    the_page_options = page_options.PageOptions(page=page, page_size=page_size)
    # Assert
    assert the_page_options.page == page
    assert the_page_options.page_size == page_size

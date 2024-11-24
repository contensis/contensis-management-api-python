"""Just confirm that the mock api response works."""

import http

from tests.helpers import mock_api_response


def test_api_response():
    """Make sure the ApiResponse dataclass has the expected properties."""
    # Act
    response = mock_api_response.MockApiResponse(
        status_code=200,
        json_data={"key": "value"},
        headers={"header": "value"},
    )
    # Assert
    assert response.status_code == http.HTTPStatus.OK
    assert response.json_data == {"key": "value"}
    assert response.headers == {"header": "value"}

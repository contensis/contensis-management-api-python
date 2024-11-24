"""Confirm that the API client can authenticate and return a token."""

import pytest

from contensis_management import (
    api_client,
    request_handler_abc,
)
from tests.helpers import mock_api_response


class MockRequestHandlerSuccessful(request_handler_abc.RequestHandlerABC):
    """A mock implementation of the RequestHandler class."""

    def post(self, url, headers=None, data=None):
        """Return a dummy token that is a plausible length."""
        mock_token = "a" * 1100
        return mock_api_response.MockApiResponse(
            status_code=200, json_data={"access_token": mock_token}
        )

    def get(self, url, headers=None):
        """Do nothing."""
        raise NotImplementedError("This should not have been called.")

    def head(self, url, headers=None):
        """Return a list of users."""
        raise NotImplementedError("Not implemented")


def test_api_client_success() -> None:
    """Confirm that the class can authenticate."""
    # Arrange
    mock_request_handler = MockRequestHandlerSuccessful()
    # Act
    client = api_client.ApiClient(handler=mock_request_handler)
    # Assert
    token = client.token
    assert token is not None
    # and it should be huge.
    a_big_number = 1000  # Tokens seem to be about 1125 characters long.
    assert len(token) > a_big_number


def test_api_client_from_credentials() -> None:
    """Confirm that you can create a client from credentials."""
    # Arrange
    mock_request_handler = MockRequestHandlerSuccessful()
    # Act
    client = api_client.ApiClient.from_credentials(
        "dummy-alias", "dummy-user", "dummy-password", mock_request_handler
    )
    # Assert
    token = client.token
    assert token is not None


def test_api_client_from_token() -> None:
    """Confirm that you can create a client from a token."""
    # Arrange
    mock_request_handler = MockRequestHandlerSuccessful()
    dummy_token = "the-token-that-was-passed-in"
    # Act
    client = api_client.ApiClient.from_token(
        handler=mock_request_handler, alias="dummy-alias", token=dummy_token
    )
    # Assert
    token = client.token
    assert token == dummy_token


class MockRequestHandlerFailure(request_handler_abc.RequestHandlerABC):
    """A mock implementation of the RequestHandler class."""

    def post(self, url, headers=None, data=None):
        """Return a dummy token that is a plausible length."""
        return mock_api_response.MockApiResponse(
            json_data={"error": "IncorrectUsernameorPassword"}, status_code=400
        )

    def get(self, url, headers=None):
        """Do nothing."""
        raise NotImplementedError("This should not have been called.")

    def head(self, url, headers=None):
        """Return a list of users."""
        raise NotImplementedError("Not implemented")


def test_api_client_failure() -> None:
    """Confirm that the class can authenticate."""
    # Arrange
    mock_request_handler = MockRequestHandlerFailure()
    # Act
    with pytest.raises(PermissionError) as got_an_error:
        api_client.ApiClient(handler=mock_request_handler)
    # Assert
    assert got_an_error is not None

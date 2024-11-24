"""Confirm that the request handler base class has the correct methods."""

from contensis_management import request_handler_abc


def test_request_handler_abc() -> None:
    """Confirm that the class has the correct methods."""
    assert hasattr(request_handler_abc.RequestHandlerABC, "post")
    assert hasattr(request_handler_abc.RequestHandlerABC, "get")
    assert callable(request_handler_abc.RequestHandlerABC.post)
    assert callable(request_handler_abc.RequestHandlerABC.get)

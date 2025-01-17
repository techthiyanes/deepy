import pytest


def pytest_addoption(parser):
    parser.addoption("--uri", action="store", default="http://0.0.0.0")
    parser.addoption("--port", action="store", default=8103)
    parser.addoption("--handle", action="store", default="respond")


@pytest.fixture
def uri(request) -> str:
    return request.config.getoption("--uri")


@pytest.fixture
def port(request) -> int:
    return request.config.getoption("--port")


@pytest.fixture
def handle(request) -> str:
    return request.config.getoption("--handle")


@pytest.fixture
def url(uri, port, handle):
    return f"{uri}:{port}/{handle}"

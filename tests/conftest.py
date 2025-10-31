import pytest
from database import Database

@pytest.fixture(scope="session")
def setupteardownclass():
    print("set up class")
    yield
    print("tear down class")


@pytest.fixture()
def setupteardown():
    print("setup")
    yield
    print("tear down")

@pytest.fixture()
def database():
    return Database()
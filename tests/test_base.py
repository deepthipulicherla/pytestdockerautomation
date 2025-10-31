import pytest

from base import get_weather
from divadd import add, div
from dataprovider import prime

@pytest.mark.order(2)
@pytest.mark.parametrize("actual,expected",[(21,"HOT"),(13,"COLD")])
def test_weather(actual,expected,setupteardownclass, setupteardown):
    assert get_weather(actual) == expected

@pytest.mark.order(3)
@pytest.mark.sanity
def test_add(setupteardownclass, setupteardown):
    assert add(2, 3) == 5

@pytest.mark.order(1)
@pytest.mark.regression
def test_div(setupteardownclass, setupteardown):
    with pytest.raises(ValueError, match="division by zero"):
        div(3, 0)
@pytest.mark.order(5)
@pytest.mark.parametrize("num,expected",[(1,False),(2,True),(3,True),(4,False),(5,True),(6,False),(7,True),(8,False),(9,False),(10,False)])
def test_prime(setupteardownclass,setupteardown,num,expected):
    assert prime(num)==expected


@pytest.mark.order(4)
@pytest.mark.parametrize("actual,expected",[(1,False),(2,True),(3,True),(4,False),(5,True),(6,False),(7,True),(8,False),(9,False)])
def test_prime(actual,expected,setupteardownclass, setupteardown):
    assert prime(actual) == expected

@pytest.mark.order(5)
@pytest.mark.parametrize("user_id,name",[(1,"Alice"),(2,"Tom"),(3,"Tracy"),(4,"Tommy"),(5,"Albert")])
def test_add_user(database,user_id,name):
    database.add_user(user_id,name)
    assert database.get_user(user_id)==name

@pytest.mark.order(6)
def test_add_duplicate_user(database):
    database.add_user(1,"Alice")
    with pytest.raises(ValueError,match="user already existing"):
        database.add_user(1,"Bob")

@pytest.mark.order(7)
def test_delete_user(database):
    database.delete_user(2)
    assert database.get_user(2)==None



import requests
baseUrl="https://jsonplaceholder.typicode.com"

def test_get():
    response = requests.get(baseUrl+"/users/1")
    assert response.status_code==200
    assert response.json()["id"]==1
    assert response.json()["address"]["geo"]["lat"]=="-37.3159"
    assert response.json()["company"]["catchPhrase"]=="Multi-layered client-server neural-net"
    print(response.json())

def test_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response=requests.post(baseUrl+"/posts",json=payload)
    print(response.json())
    assert response.status_code==201
    assert response.json()["title"]=="foo"

def test_post_update():
    payload = {
        "title": "foo",
        "body": "jar",
        "userId": 1,
        "id": 101
    }
    response=requests.put(baseUrl+"/posts/1",json=payload)
    assert response.status_code==200
    assert response.json()["body"]=="jar"
    print(response.json())

def test_patch_update():
    payload = {
        "title": "patch_update"
    }
    response=requests.patch(baseUrl+"/posts/1",json=payload)
    assert response.status_code==200
    assert response.json()["title"]=="patch_update"
    print(response.json())

def test_delete():
    response=requests.delete(baseUrl+"/users/1")
    assert response.status_code==200
    print(response.json())

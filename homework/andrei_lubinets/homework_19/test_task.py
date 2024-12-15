import requests
import pytest

data_for_test = [
    {'data': {'color': 'yellow', 'size': 'large'}, "name": "My car"},
    {'data': {'color': 'red', 'size': 'small'}, "name": "My bike"},
    {'data': {'color': 'green', 'size': 'large'}, "name": "My car"}
]


@pytest.fixture()
def new_object():
    body = {'data': {'color': 'yellow', 'size': 'small'}, "name": "My item"}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'http://167.172.172.115:52353//object/{post_id}')
    print(f"Deleted post with id {post_id}")


@pytest.fixture(scope='session')
def info():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.mark.parametrize("body", data_for_test)
@pytest.mark.critical
def test_post_a_object(body, info):
    print("before test")
    print(body)
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
    print(f"Object created: {response.json()}")
    print(f"Status code: {response.status_code}")
    assert response.status_code == 200, "Invalid status code"
    print("after test")


def test_put_a_object(new_object):
    print("before test")
    body = {'data': {'color': 'yellow', 'size': 'small'}, "id": new_object, "name": "My plane"}
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'http://167.172.172.115:52353//object/{new_object}', json=body, headers=headers
                            ).json()
    print(f"Data: {response}")
    assert response['data']['color'] == 'yellow', 'Invalid value'
    assert response['data']['size'] == 'small', 'Invalid value'
    print("after test")


@pytest.mark.medium
def test_patch_a_object(new_object):
    print("before test")
    body = {'data': {'color': 'green', 'size': 'small'}, "name": "My car"}
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://167.172.172.115:52353//object/{new_object}', json=body, headers=headers)
    print(f"Object changed: {response.json()}")
    print("after test")


def test_delete_a_object(new_object):
    print("before test")
    response = requests.delete(f'http://167.172.172.115:52353//object/{new_object}')
    print(response.text)
    print(response.status_code)
    print("after test")

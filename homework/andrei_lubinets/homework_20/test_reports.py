import requests
import pytest
import allure

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
@allure.feature("Posts")
@allure.story("Manipulate with post")
@allure.title("Создание поста")
def test_post_a_object(body, info):
    print("before test")
    print(body)
    headers = {'Content-Type': 'application/json'}
    with allure.step(f"Crate a post with body {body}"):
        response = requests.post('http://167.172.172.115:52353/object', json=body, headers=headers)
        print(f"Object created: {response.json()}")
        print(f"Status code: {response.status_code}")
    with allure.step("Check that post is created and status code is 200"):
        assert response.status_code == 200, "Invalid status code"
    print("after test")


@allure.feature("Posts")
@allure.story("Manipulate with post")
@allure.title("Полное измнение данных поста")
def test_put_a_object(new_object):
    print("before test")
    with allure.step("Prepare test data"):
        body = {'data': {'color': 'yellow', 'size': 'small'}, "id": new_object, "name": "My plane"}
        headers = {'Content-Type': 'application/json'}
    with allure.step(f"Change data post with id {new_object} to {body}"):
        response = requests.put(f'http://167.172.172.115:52353//object/{new_object}', json=body, headers=headers
                                ).json()
        print(f"Data: {response}")
    with allure.step(f"Check that the data in the post with id {new_object} has been changed"):
        assert response['data']['color'] == 'yellow', 'Invalid value'
        assert response['data']['size'] == 'small', 'Invalid value'
    print("after test")


@pytest.mark.medium
@allure.feature("Posts")
@allure.story("Manipulate with post")
@allure.title("Частичное измнение данных поста")
def test_patch_a_object(new_object):
    print("before test")
    with allure.step("Prepare test data"):
        body = {'data': {'color': 'green', 'size': 'small'}, "name": "My car"}
        headers = {'Content-Type': 'application/json'}
    with allure.step(f"Change data post with id {new_object} to {body}"):
        response = requests.patch(f'http://167.172.172.115:52353//object/{new_object}', json=body, headers=headers)
        print(f"Object changed: {response.json()}")
    print("after test")


@allure.feature("Posts")
@allure.story("Manipulate with post")
@allure.title("Удадение поста")
def test_delete_a_object(new_object):
    print("before test")
    with allure.step(f"Post with id {new_object} has been deleted"):
        response = requests.delete(f'http://167.172.172.115:52353//object/{new_object}')
        print(response.text)
        print(response.status_code)
    print("after test")

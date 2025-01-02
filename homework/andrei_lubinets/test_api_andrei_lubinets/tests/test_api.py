import pytest
import allure

TEST_DATA = [
    {'data': {'color': 'yellow', 'size': 'large'}, "name": "My car"},
    {'data': {'color': 'red', 'size': 'small'}, "name": "My bike"},
    {'data': {'color': 'green', 'size': 'large'}, "name": "My car"}
]


@allure.title('Создание поста')
@pytest.mark.parametrize('data', TEST_DATA)
def test_post_a_post(create_post_endpoint, data):
    create_post_endpoint.create_new_post(payload=data)
    create_post_endpoint.check_that_status_is_200()
    create_post_endpoint.check_that_tittle_is_correct(data['name'])


@allure.title('Полное изменение данных в посте')
def test_patch_a_post(update_patch_endpoint, post_id):
    payload = {'data': {'color': 'yellow', 'size': 'large'}, "name": "My bike"}
    update_patch_endpoint.patch_a_post(post_id, payload)
    update_patch_endpoint.check_that_status_is_200()
    update_patch_endpoint.check_that_tittle_is_correct(payload['name'])


@allure.title('Частичное изменение данных в посте')
def test_put_a_post(update_put_endpoint, post_id):
    payload = {'data': {'color': 'red', 'size': 'compact'}, "name": "My plane"}
    update_put_endpoint.put_a_post(post_id, payload)
    update_put_endpoint.check_that_status_is_200()
    update_put_endpoint.check_that_tittle_is_correct(payload['name'])


@allure.title('Удаление поста по id')
def test_delete_a_post(delete_endpoint, post_id):
    delete_endpoint.delete_a_post(post_id)
    delete_endpoint.check_that_status_is_200()
    delete_endpoint.check_bad_request()


@allure.title('Отображение всех постов')
def test_get_all_posts(create_get_endpoint):
    create_get_endpoint.show_all_posts()
    create_get_endpoint.check_that_status_is_200()

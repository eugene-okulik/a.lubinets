import pytest
import allure

TEST_DATA = [
    {'data': {'color': 'yellow', 'size': 'large'}, "name": "My car"},
    {'data': {'color': 'red', 'size': 'small'}, "name": "My bike"},
    {'data': {'color': 'green', 'size': 'large'}, "name": "My car"}
]


@allure.title('Создание объекта')
@pytest.mark.parametrize('data', TEST_DATA)
def test_post_a_object(create_object_endpoint, data):
    create_object_endpoint.create_new_object(payload=data)
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.check_that_tittle_is_correct(data['name'])


@allure.title('Полное изменение данных в объекта')
def test_patch_a_object(update_patch_endpoint, object_id):
    payload = {'data': {'color': 'yellow', 'size': 'large'}, "name": "My bike"}
    update_patch_endpoint.patch_a_object(object_id, payload)
    update_patch_endpoint.check_that_status_is_200()
    update_patch_endpoint.check_that_tittle_is_correct(payload['name'])


@allure.title('Частичное изменение данных в объекта')
def test_put_a_object(update_put_endpoint, object_id):
    payload = {'data': {'color': 'red', 'size': 'compact'}, "name": "My plane"}
    update_put_endpoint.put_a_object(object_id, payload)
    update_put_endpoint.check_that_status_is_200()
    update_put_endpoint.check_that_tittle_is_correct(payload['name'])


@allure.title('Удаление объекта по id')
def test_delete_a_object(delete_endpoint, object_id):
    delete_endpoint.delete_a_object(object_id)
    delete_endpoint.check_that_status_is_200()


@allure.title('Отображение всех объектов')
def test_get_all_object(create_get_endpoint):
    create_get_endpoint.show_all_object()
    create_get_endpoint.check_that_status_is_200()

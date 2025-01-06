import pytest
from endpoits.api_post import ApiPost
from endpoits.api_patch import ApiPatch
from endpoits.api_put import ApiPut
from endpoits.api_delete import ApiDelete
from endpoits.api_get import ApiGet


@pytest.fixture()
def create_object_endpoint():
    return ApiPost()


@pytest.fixture()
def create_get_endpoint():
    return ApiGet()


@pytest.fixture()
def update_patch_endpoint():
    return ApiPatch()


@pytest.fixture()
def update_put_endpoint():
    return ApiPut()


@pytest.fixture()
def delete_endpoint():
    return ApiDelete()


@pytest.fixture()
def object_id(create_object_endpoint, delete_endpoint):
    payload = {'data': {'color': 'yellow', 'size': 'large'}, "name": "My car"}
    create_object_endpoint.create_new_object(payload)
    yield create_object_endpoint.object_id
    delete_endpoint.delete_a_object(object_id)

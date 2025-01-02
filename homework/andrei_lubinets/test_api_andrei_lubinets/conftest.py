import pytest
from endpoits.api_post import ApiPost
from endpoits.api_patch import ApiPatch
from endpoits.api_put import ApiPut
from endpoits.api_delete import ApiDelete
from endpoits.api_get import ApiGet


@pytest.fixture()
def create_post_endpoint():
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
def delete_endpoint(create_post_endpoint):
    return ApiDelete()


@pytest.fixture()
def post_id(create_post_endpoint):
    payload = {'data': {'color': 'yellow', 'size': 'large'}, "name": "My car"}
    create_post_endpoint.create_new_post(payload)
    yield create_post_endpoint.post_id

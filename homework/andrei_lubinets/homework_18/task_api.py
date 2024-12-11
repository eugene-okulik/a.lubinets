import requests


def new_object():
    body = {
        'data': {
            'color': 'green',
            'size': 'small'
        },
        "id": 333,
        "name": "My car"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://167.172.172.115:52353/object',
                             json=body,
                             headers=headers
                             )
    return response.json()["id"]


def post_a_object():
    body = {
        'data': {
            'color': 'green',
            'size': 'small'
        },
        "id": 730,
        "name": "My car"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f'http://167.172.172.115:52353/object',
                             json=body,
                             headers=headers
                             )
    print(f"Object created: {response.json()}")
    print(f"Status code: {response.status_code}")
    assert response.status_code == 200, "Invalid status code"


def put_a_object():
    post_id = new_object()
    body = {
        'data': {
            'color': 'yellow',
            'size': 'small'
        },
        "id": post_id,
        "name": "Object created at 7 pm"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'http://167.172.172.115:52353//object/{post_id}',
                            json=body,
                            headers=headers
                            ).json()
    assert response['data']['color'] == 'yellow', 'Invalid value'
    assert response['data']['size'] == 'small', 'Inavalid value'
    clear(post_id)


def clear(post_id):
    requests.delete(f'http://167.172.172.115:52353//object/{post_id}')


def patch_a_object():
    post_id = new_object()
    body = {
        'data': {
            'color': 'green',
            'size': 'small'
        },
        "name": "My car"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'http://167.172.172.115:52353//object/{post_id}',
                              json=body,
                              headers=headers
                              )
    print(f"Object changed: {response.json()}")
    clear(post_id)


def delete_a_object():
    post_id = new_object()
    response = requests.delete(f'http://167.172.172.115:52353//object/{post_id}')
    print(response.text)
    print(response.status_code)


post_a_object()
# new_object()
put_a_object()
patch_a_object()
delete_a_object()

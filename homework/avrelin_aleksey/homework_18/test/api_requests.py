import requests


def test_get_all():
    response = requests.get('http://167.172.172.115:52353/object')
    assert response.status_code == 200
    print(response.json())


def test_post():
    body = {"name": "Новый объект", "data": {"объект": "ВОЗДУХ"}}
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://167.172.172.115:52353/object',
                             json=body,
                             headers=headers)
    assert response.status_code == 200
    post_id = response.json()['id']
    print(response.json())
    clear(post_id)


def test_get_one():
    post_id = post_for_test()
    response = requests.get(f'http://167.172.172.115:52353/object/{post_id}')
    assert response.status_code == 200, "Сведения об объекте отсутствуют"
    print(response.json())
    clear(post_id)


def test_put():
    post_id = post_for_test()
    body = {"name": "Новые объекты", "data": {"стихия_1": "Вода", "стихия_2": "Земля" }}
    headers = {"Content-Type": "application/json"}
    response = requests.put(f'http://167.172.172.115:52353/object/{post_id}',
                            json=body,
                            headers=headers)
    assert response.status_code == 200, "Объект не изменен"
    print(response.json())
    clear(post_id)


def test_patch():
    post_id = post_for_test()
    body = {"name": "НАИМЕНОВАНИЕ"}
    headers = {"Content-Type": "application/json"}
    response = requests.patch(f'http://167.172.172.115:52353/object/{post_id}',
                              json=body,
                              headers=headers)
    assert response.status_code == 200, "Объект не изменен"
    print(response.json())
    clear(post_id)


def test_delete():
    post_id = post_for_test()
    response = requests.delete(f'http://167.172.172.115:52353/object/{post_id}')
    assert response.status_code == 200, "Объект не удален"


def post_for_test():
    body = {"name": "Новый объект", "data": {"объект": "ВОЗДУХ"}}
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://167.172.172.115:52353/object',
                             json=body,
                             headers=headers)
    assert response.status_code == 200
    return response.json()['id']


def clear(post_id_for_test):
    requests.delete(f'http://167.172.172.115:52353/object/{post_id_for_test}')

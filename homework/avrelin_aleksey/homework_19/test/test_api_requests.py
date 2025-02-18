import requests
import pytest


@pytest.fixture(scope="session")
def start_end_message():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture()
def print_before_after():
    print("\nbefore test")
    yield
    print("\nafter test")


@pytest.fixture()
def up_down_for_test():
    body = {"name": "Новый объект", "data": {"объект": "ВОЗДУХ"}}
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://167.172.172.115:52353/object',
                             json=body,
                             headers=headers)
    post_id_for_test = response.json()['id']
    yield post_id_for_test
    requests.delete(f'http://167.172.172.115:52353/object/{post_id_for_test}')


@pytest.fixture()
def post_for_test():
    body = {"name": "Новый объект", "data": {"объект": "ВОЗДУХ"}}
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://167.172.172.115:52353/object',
                             json=body,
                             headers=headers)
    post_id_for_test = response.json()['id']
    return post_id_for_test


def test_get_all(start_end_message, print_before_after):
    response = requests.get('http://167.172.172.115:52353/object')
    assert response.status_code == 200
    print(response.json())

@pytest.mark.parametrize('body', [
    {"name":"Важное", "data": {"объект": "ВОЗДУХ"}},
    {"name": "Техника", "data": {"Машина1": "БМВ", "Машина2": "Мерседес" }},
    {"name":"Нужное", "data": {"Деньги": "наличные"}}
])
def test_post(body):
    headers = {"Content-Type": "application/json"}
    response = requests.post('http://167.172.172.115:52353/object',
                             json=body,
                             headers=headers)
    assert response.status_code == 200
    post_id = response.json()['id']
    requests.delete(f'http://167.172.172.115:52353/object/{post_id}')


def test_get_one(print_before_after, up_down_for_test):
    response = requests.get(f'http://167.172.172.115:52353/object/{up_down_for_test}')
    assert response.status_code == 200, "Сведения об объекте отсутствуют"
    print(response.json())


@pytest.mark.medium
def test_put(print_before_after, up_down_for_test):
    body = {"name": "Новые объекты", "data": {"стихия_1": "Вода", "стихия_2": "Земля"}}
    headers = {"Content-Type": "application/json"}
    response = requests.put(f'http://167.172.172.115:52353/object/{up_down_for_test}',
                            json=body,
                            headers=headers)
    assert response.status_code == 200, "Объект не изменен"
    print(response.json())


@pytest.mark.critical
def test_patch(print_before_after, up_down_for_test):
    body = {"name": "НАИМЕНОВАНИЕ"}
    headers = {"Content-Type": "application/json"}
    response = requests.patch(f'http://167.172.172.115:52353/object/{up_down_for_test}',
                              json=body,
                              headers=headers)
    assert response.status_code == 200, "Объект не изменен"
    print(response.json())


def test_delete(print_before_after, post_for_test):
    response = requests.delete(f'http://167.172.172.115:52353/object/{post_for_test}')
    assert response.status_code == 200, "Объект не удален"

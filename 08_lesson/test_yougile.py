import pytest
from yougile import Yougile

api = Yougile()
my_token = api.get_auth_key()


def test_get_list_projects_positive():
    resp = api.get_list_of_projects(my_token)
    assert resp.status_code == 200


def test_list_projects_positive():
    project_list = api.get_list_of_projects(my_token).json()
    assert len(project_list) > 0


def test_get_project_list_negative():
    project = api.get_list_of_projects("")
    assert project.status_code == 401


@pytest.mark.parametrize("title", [
    "Project 1",
    "Project 2"
])
def test_create_project_positive(title):
    resp = api.create_project(my_token, title)
    assert resp.status_code == 201


@pytest.mark.parametrize("title", [
    ""
])
def test_create_project_negative(title):
    resp = api.create_project(my_token, title)
    assert resp.status_code == 400


@pytest.mark.parametrize("title", [
    "Project 3",
    "Project 4"
])
def test_get_project_positive(title):
    resp = api.create_project(my_token, title)
    assert resp.status_code == 201
    project_id = resp.json()['id']
    resp_project = api.get_project(my_token, project_id)
    assert resp_project.status_code == 200
    assert resp_project.json()['title'] == title


def test_get_project_negative():
    project_info = api.get_project(my_token, '1')
    assert project_info.status_code == 404


def test_change_project_positive():
    resp = api.create_project(my_token, 'Name project')
    assert resp.status_code == 201
    project_id = resp.json()['id']
    resp_project = api.change_project(my_token, project_id, 'New Name')
    assert resp_project.status_code == 200


def test_change_project_negative():
    resp = api.create_project(my_token, 'Name project')
    assert resp.status_code == 201
    project_id = resp.json()['id']
    resp_project = api.change_project(my_token, project_id, '')
    assert resp_project.status_code == 400

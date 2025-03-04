import requests
from settings import LOGIN, PASSWORD, COMPANY_ID


class Yougile:

    def __init__(self):
        self.login = LOGIN
        self.password = PASSWORD
        self.company_id = COMPANY_ID
        self.url = "https://ru.yougile.com/api-v2"

    def get_auth_key(self):
        payload = {
            "login": self.login,
            "password": self.password,
            "companyId": self.company_id
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(
            f"{self.url}/auth/keys/get", json=payload, headers=headers
        )
        response.raise_for_status()
        resp = response.json()
        first_key = resp[0]
        my_key = first_key.get('key')

        return my_key

    def get_list_of_projects(self, my_token):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {my_token}'
        }
        response = requests.get(
            f"{self.url}/projects", headers=headers
        )
        return response

    def create_project(self, my_token, my_title):
        payload = {
            'title': my_title
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {my_token}'
        }
        response = requests.post(
            f"{self.url}/projects", headers=headers, json=payload
        )
        return response

    def get_project(self, my_token, project_id):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {my_token}'
        }
        response = requests.get(
            f"{self.url}/projects/{project_id}", headers=headers
        )
        return response

    def change_project(self, my_token, project_id, my_title):
        payload = {
            'title': my_title
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {my_token}'
        }
        response = requests.put(
            f"{self.url}/projects/{project_id}", headers=headers, json=payload
        )
        return response

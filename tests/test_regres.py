import json

import requests
import pytest

from schemas.regres import users, morpheus
from utils.sessions import regres
from voluptuous import Schema
from pytest_voluptuous import S


def test_users_per_page_count():
	per_page = 6
	response = regres().get('/users?page=2', params={'per_page': per_page})

	assert len(response.json()['data']) == per_page


def test_create_user_morpheus():
	payload = json.dumps({
		"name": 'morpheus',
		"job": 'leader'
	})
	response = regres().post('/users', data=payload, allow_redirects=False)
	assert response.status_code == 201
	assert 'id' and 'createdAt' in response.json()


def test_update_job_user_morpheus():
	payload = json.dumps({
		'name': 'morpheus',
		'job': 'zion resident'
	})
	response = regres().put('/users/2', data=payload, allow_redirects=False)
	assert response.status_code == 200
	assert 'zion resident' and 'updatedAt' in response.json()


def test_single_user_not_found():
	response = regres().get('/users/23')
	assert response.status_code == 404


def test_get_single_resource():
	response = regres().get('/unknown/2')
	print(response.json())
	assert response.status_code == 200
	assert 'data' in response.json()


def test_delete_users():
	response = regres().delete('/users/2')
	print(response.json())
	assert response.status_code == 204




def test_register_user():
	payload = json.dumps({
		"email": "eve.holt@reqres.in",
		"password": "pistol"
})
	response = regres().post('/register', data=payload, allow_redirects=False)
	print(response.json())
	assert response.status_code == 200
	assert 'id' and 'token' in response.json()


def test_fact_fields_validation11():
    response = regres().get("/users/2")
    assert response.status_code == 200
    assert isinstance(response.json()['first_name'], str)
    assert isinstance(response.json()['last_name'], str)


def test_fact_fields_validation():
	response = regres().get('/users/2')
	# valid schemas
	assert S(users) == response.json()



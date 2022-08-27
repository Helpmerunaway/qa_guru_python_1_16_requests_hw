from voluptuous import ALLOW_EXTRA
from voluptuous import Schema


single_user = Schema({
	'id': int,
	'email': str,
	'first_name': str,
	'last_name': str,
	'avatar': str,
})

users = Schema(
    {
		"data": [single_user]
    },
    extra=ALLOW_EXTRA,
    required=True
)

morpheus = Schema({
    "name": "morpheus",
    "job": "leader"
})
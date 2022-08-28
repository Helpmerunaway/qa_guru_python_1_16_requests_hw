from voluptuous import ALLOW_EXTRA
from voluptuous import Schema


single_user_exact = Schema({
	'id': 2,
	'email': "janet.weaver@reqres.in",
	'first_name': "Janet",
	'last_name': "Weaver",
	'avatar': "https://reqres.in/img/faces/2-image.jpg"
})

exact_users = Schema(
    {
		"data": single_user_exact,
	    "support": {
		    "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
	    }
    },
    extra=ALLOW_EXTRA,
    required=True
)

single_user = Schema({
	'id': int,
	'email': str,
	'first_name': str,
	'last_name': str,
	'avatar': str
})

support_user = Schema({
	'url': str,
	'text': str
})


users = Schema(
    {
		"data": single_user,
	    "support": support_user
    },
    extra=ALLOW_EXTRA,
    required=True
)


morpheus = Schema({
    "name": "morpheus",
    "job": "leader"
})
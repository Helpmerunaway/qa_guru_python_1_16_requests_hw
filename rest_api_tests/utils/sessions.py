import os

from rest_api_tests.utils.requests_helper import BaseSession

# оборачиваем без бейс юрл
def regres() -> BaseSession:
	regres_url = os.getenv('regres_url')
	return BaseSession(base_url=regres_url)
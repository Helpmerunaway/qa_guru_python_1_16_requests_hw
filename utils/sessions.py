from utils.requests_helper import BaseSession

# оборачиваем без бейс юрл
def regres() -> BaseSession:
	regres_url = 'https://reqres.in/api'
	return BaseSession(base_url=regres_url)
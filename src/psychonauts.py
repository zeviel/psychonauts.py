from requests import get


class Psychonauts:
	def __init__(self):
		self.api = "https://psychonauts-api.herokuapp.com/api"
		self.headers = {
			"User-Agent": "Mozilla/5.0 (Linux; Android 11; RMX2086 Build/RKQ1.200928.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36"
		}
	
	def get_all_characters(self, limit: int = 10):
		return get(
			f"{self.api}/characters?limit={limit}",
			headers=self.headers).json()
		
	def get_character_by_name(self, name: str):
		return get(
			f"{self.api}/characters?name={name}",
			headers=self.headers).json()
	
	def get_character_by_gender(self, gender: str):
		return get(
			f"{self.api}/characters?gender={gender}",
			headers=self.headers).json()
		
	def get_all_psi_powers(self, limit: int = 10):
		return get(
			f"{self.api}/powers?limit={limit}",
			headers=self.headers).json()
	
	def get_psi_power_by_name(self, name: str):
		return get(
			f"{self.api}/powers?name={name}",
			headers=self.headers).json()
			

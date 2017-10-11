import json

class Config:
	def __init__(self):
		with open('data.json') as data_file:
			self.__data = json.load(data_file)

	def get_phone(self):
		return self.__data['phone']

	def get_api_id(self):
		return self.__data['api_id']

	def get_api_hash(self):
		return self.__data['api_hash']

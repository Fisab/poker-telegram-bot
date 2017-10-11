from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import config

user_poker = '@PokerBot'

class Main:
	def __init__(self):
		self.config = config.Config()
		self.user_phone = self.config.get_phone()

		print('Connecting to Telegram servers...')

		self.client = TelegramClient('session_name', self.config.get_api_id(), self.config.get_api_hash())

		if not self.client.connect():
			print('Initial connection failed. Retrying...')
			if not self.client.connect():
				print('Could not connect to Telegram servers.')
				return

		if not self.client.is_user_authorized():
			print('First run. Sending code request...')

			try:
				self.me = self.client.sign_in(phone=self.user_phone)
				code = input('Enter the code: ')
				self.me = self.client.sign_in(code=code)
			except SessionPasswordNeededError:
				pw = getpass('Please enter your password: ')
				self_user = self.sign_in(password=pw)

	def test(self):
		print(self.me.stringify())

		client.send_message(user_poker, 'Hello! Talking to you from Telethon')

if __name__ == '__main__':
	m = Main()
	m.test()


from Crypto.Cipher import DES
from django.conf import settings


def encrypt(phone):
	print settings.SECRET, settings.IV
	cipher = DES.new(settings.SECRET, DES.MODE_CFB, settings.IV)
	return cipher.encrypt(phone)


if __name__ == '__main__':
	print encrypt('18628290813')
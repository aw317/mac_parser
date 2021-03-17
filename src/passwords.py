from cryptography.fernet import Fernet

key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='


def encode_token(token):
    cipher_suite = Fernet(key)
    ciphered_text = cipher_suite.encrypt(token.encode('utf-8'))
    return ciphered_text


def decode_token(encoded_token):
    cipher_suite = Fernet(key)
    unciphered_text = (cipher_suite.decrypt(encoded_token))
    return unciphered_text

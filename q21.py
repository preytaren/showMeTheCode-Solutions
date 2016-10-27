from hashlib import sha256
from hmac import HMAC
import os


def encrypt_password(password, salt=None):
    if not salt:
        salt = os.urandom(8)
    password = password.encode()
    return HMAC(password, salt, sha256).digest(), salt


def check(password, hash, salt):
    checked_hash, _ = encrypt_password(password, salt)
    return hash == checked_hash


if __name__ == '__main__':
    password = 'preyta'
    hash, salt = encrypt_password(password)
    assert check(password, hash, salt)


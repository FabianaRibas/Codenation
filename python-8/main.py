import jwt
from jwt.exceptions import (InvalidSignatureError, DecodeError)


def create_token(data, secret):
    encoded_token = jwt.encode(data, secret, algorithm='HS256')

    return encoded_token


def verify_signature(token):
    try:
        secret = 'acelera'

        return jwt.decode(token, secret, algorithms='HS256')

    except (InvalidSignatureError, DecodeError):
        invalid_signature = {
            'error': 2
        }
        return invalid_signature

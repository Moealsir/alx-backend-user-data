#!/usr/bin/env python3
""" Returns a salted, hashed password, byte in string """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Return byte string password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def is_valid(hash_password: bytes, password: str) -> bool:
    """ Check and match password """

    return bcrypt.checkpw(password.encode("utf-8"), hash_password)

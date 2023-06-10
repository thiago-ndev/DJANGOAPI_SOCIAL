import hashlib
import sys
import _sha3

def cripty_senha(senha):
    encoded_senha = senha.encode()
    senha_sha3 = hashlib.sha3_256(encoded_senha)
    return senha_sha3.hexdigest()


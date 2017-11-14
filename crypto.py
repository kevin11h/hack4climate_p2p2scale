from hashlib import sha256


def create_hash(s: str)->str:
    return sha256(s.encode('utf-8')).hexdigest()

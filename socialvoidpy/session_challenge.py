import hashlib
import base64
import hmac
import struct
import time


def hotp(key: str, counter: int, digits: int = 6, digest: str = "sha1") -> str:
    key = base64.b32decode(key.upper() + "=" * ((8 - len(key)) % 8))
    counter = struct.pack(">Q", counter)
    mac = hmac.new(key, counter, digest).digest()
    offset = mac[-1] & 0x0F
    binary = struct.unpack(">L", mac[offset : offset + 4])[0] & 0x7FFFFFFF
    return str(binary)[-digits:].zfill(digits)


def totp(key: str, time_step: int = 30, digits: int = 6, digest: str = "sha1") -> str:
    return hotp(key, int(time.time() / time_step), digits, digest)


def answer_challenge(client_private_hash: str, challenge: str) -> str:
    totp_code = totp(challenge)
    return hashlib.sha1((totp_code + client_private_hash).encode()).hexdigest()

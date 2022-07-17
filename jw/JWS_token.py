# https://jwcrypto.readthedocs.io/en/latest/jws.html
from jwcrypto import jwk, jws
from jwcrypto.common import json_encode

CHAPTER_PREFIX = '=' * 50 + '> '

print(CHAPTER_PREFIX + 'Sign a JWS token')
key = jwk.JWK.generate(kty='oct', size=256)
payload = "My Integrity protected message"
jwstoken = jws.JWS(payload.encode('utf-8'))
jwstoken.add_signature(key, None,
                       json_encode({"alg": "HS256"}),
                       json_encode({"kid": key.thumbprint()}))
sig = jwstoken.serialize()
print(sig)

print(CHAPTER_PREFIX + 'Verify a JWS token')
jwstoken = jws.JWS()
jwstoken.deserialize(sig)
jwstoken.verify(key)
payload = jwstoken.payload
print(payload)

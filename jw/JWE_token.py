# https://jwcrypto.readthedocs.io/en/latest/jwe.html
from jwcrypto import jwk, jwe
from jwcrypto.common import json_encode, json_decode

CHAPTER_PREFIX = '=' * 50 + '> '

print(CHAPTER_PREFIX + 'Symmetric keys: Encrypt a JWE token')
key = jwk.JWK.generate(kty='oct', size=256)
payload = "My Encrypted message"
jwetoken = jwe.JWE(payload.encode('utf-8'),
                   json_encode({"alg": "A256KW",
                                "enc": "A256CBC-HS512"}))
jwetoken.add_recipient(key)
enc = jwetoken.serialize()
print(enc)

print(CHAPTER_PREFIX + 'Symmetric keys: Decrypt a JWE token')
jwetoken = jwe.JWE()
jwetoken.deserialize(enc)
jwetoken.decrypt(key)
payload = jwetoken.payload
print(payload)

print(CHAPTER_PREFIX + 'Asymmetric keys: Encrypt a JWE token')
public_key = jwk.JWK()
private_key = jwk.JWK.generate(kty='RSA', size=2048)
public_key.import_key(**json_decode(private_key.export_public()))
payload = "My Encrypted message"
protected_header = {
    "alg": "RSA-OAEP-256",
    "enc": "A256CBC-HS512",
    "typ": "JWE",
    "kid": public_key.thumbprint(),
}
jwetoken = jwe.JWE(payload.encode('utf-8'),
                   recipient=public_key,
                   protected=protected_header)
enc = jwetoken.serialize()
print(enc)

print(CHAPTER_PREFIX + 'Asymmetric keys: Decrypt a JWE token')
jwetoken = jwe.JWE()
jwetoken.deserialize(enc, key=private_key)
payload = jwetoken.payload
print(payload)

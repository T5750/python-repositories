# https://jwcrypto.readthedocs.io/en/latest/jwk.html
from jwcrypto import jwk

CHAPTER_PREFIX = '=' * 50 + '> '

print(CHAPTER_PREFIX + 'Create a 256bit symmetric key')
key = jwk.JWK.generate(kty='oct', size=256)
print(key)

print(CHAPTER_PREFIX + 'Export the key with')
key.export()

print(CHAPTER_PREFIX + 'Create a 2048bit RSA key pair')
jwk.JWK.generate(kty='RSA', size=2048)

print(CHAPTER_PREFIX + 'Create a P-256 EC key pair and export the public key')
key = jwk.JWK.generate(kty='EC', crv='P-256')
key.export(private_key=False)
print(key)

print(CHAPTER_PREFIX + 'Import a P-256 Public Key')
expkey = {"y": "VYlYwBfOTIICojCPfdUjnmkpN-g-lzZKxzjAoFmDRm8",
          "x": "3mdE0rODWRju6qqU01Kw5oPYdNxBOMisFvJFH1vEu9Q",
          "crv": "P-256", "kty": "EC"}
key = jwk.JWK(**expkey)
print(key)

print(CHAPTER_PREFIX + 'Import a Key from a PEM file')
# with open("public.pem", "rb") as pemfile:
#     key = jwk.JWK.from_pem(pemfile.read())

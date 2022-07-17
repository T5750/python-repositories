# https://jwcrypto.readthedocs.io/en/latest/jwt.html
from jwcrypto import jwt, jwk

CHAPTER_PREFIX = '=' * 50 + '> '

print(CHAPTER_PREFIX + 'Create a symmetric key')
key = jwk.JWK(generate='oct', size=256)
key.export()
print(key)

print(CHAPTER_PREFIX + 'Create a signed token with the generated key')
token = jwt.JWT(header={"alg": "HS256"},
                claims={"info": "I'm a signed token"})
token.make_signed_token(key)
token.serialize()
print(token)

print(CHAPTER_PREFIX + 'Further encrypt the token with the same key')
etoken = jwt.JWT(header={"alg": "A256KW", "enc": "A256CBC-HS512"},
                 claims=token.serialize())
etoken.make_encrypted_token(key)
etoken.serialize()
print(etoken)

print(CHAPTER_PREFIX + 'Now decrypt and verify')
k = {"k": "Wal4ZHCBsml0Al_Y8faoNTKsXCkw8eefKXYFuwTBOpA", "kty": "oct"}
key = jwk.JWK(**k)
e = 'eyJhbGciOiJBMjU2S1ciLCJlbmMiOiJBMjU2Q0JDLUhTNTEyIn0.ST5RmjqDLj696xo7YFTFuKUhcd3naCrm6yMjBM3cqWiFD6U8j2JIsbclsF7ryNg8Ktmt1kQJRKavV6DaTl1T840tP3sIs1qz.wSxVhZH5GyzbJnPBAUMdzQ.6uiVYwrRBzAm7Uge9rEUjExPWGbgerF177A7tMuQurJAqBhgk3_5vee5DRH84kHSapFOxcEuDdMBEQLI7V2E0F57-d01TFStHzwtgtSmeZRQ6JSIL5XlgJouwHfSxn9Z_TGl5xxq4TksORHED1vnRA.5jPyPWanJVqlOohApEbHmxi3JHp1MXbmvQe2_dVd8FI'
ET = jwt.JWT(key=key, jwt=e)
ST = jwt.JWT(key=key, jwt=ET.claims)
print(ST.claims)

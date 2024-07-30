import hashlib, binascii

SHA3_256_Hash = hashlib.sha3_256(b'hello world').digest()
print("SHA3-256('hello world') = ", binascii.hexlify(SHA3_256_Hash))
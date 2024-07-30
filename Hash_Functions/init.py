import hashlib, binascii

SHA3_256_Hash = hashlib.sha3_256(b'hello world').digest()
print("SHA3-256('hello world') = ", binascii.hexlify(SHA3_256_Hash)) # b'644bcc7e564373040999aac89e7622f3ca71fba1d972fd94a31c3bfbf24e3938'

# 
sha3_256_hash1 = hashlib.sha3_256(b'hello').digest()
print("SHA3-256('hello') = ", binascii.hexlify(sha3_256_hash1))

sha3_256_hash2 = hashlib.sha3_256(b'hello').digest()
print("SHA3-256('ehllo') = ", binascii.hexlify(sha3_256_hash2))

if sha3_256_hash1 == sha3_256_hash2:
    print('same hash')
else:
    print('different hash')
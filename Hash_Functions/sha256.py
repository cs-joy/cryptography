import hashlib, binascii

SHA256_Hash = hashlib.sha256(b'hello').digest()

print('SHA256(\'hello\') = ', binascii.hexlify(SHA256_Hash)) # 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
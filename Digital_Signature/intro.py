'''
Digital signatures are a cryptographic tool to sign messages and verify message signatures in order to 
provide proof of authenticity for digital messages or electronic documents. Digital signatures provide:

    1. Message authentication - a proof that certain known sender (secret key owner) have created and 
                                signed the message.

    2. Мessage integrity - a proof that the message was not altered after the signing.

    3. Non-repudiation - the signer cannot deny the signing of the document after the signature is once
                         created.
'''

from Crypto.PublicKey import RSA

# generate 1024-bits RSA keypairs
keyPair = RSA.generate(bits=1024)
print(f'Public key: (n={hex(keyPair.n)}, e={hex(keyPair.e)})')
print(f'Private key: (n={hex(keyPair.n)}, d={keyPair.d})')

# let's sign a message, using the RSA private key {n, d}. 
# calculate it's hash and raise the hash to the power d modulo n (encryt the hash by the private key).
# we shall use SHA-512 hash.


# RSA sign message
msg = b'A message for signing'
from hashlib import sha512

hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
signature = pow(hash, keyPair.d, keyPair.n)
print('hash: ', hash)
print('Signature: ', hex(signature))




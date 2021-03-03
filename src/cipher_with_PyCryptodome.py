#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes



data = b"1111111111111111"
key = get_random_bytes(16)

# CBC
print("CBCモード")
cipher_cbc = AES.new(key, AES.MODE_CBC)
ct_bytes_cbc = cipher_cbc.encrypt(pad(data, AES.block_size))
iv = b64encode(cipher_cbc.iv).decode('utf-8')
ct_cbc = b64encode(ct_bytes_cbc).decode('utf-8')
result = json.dumps({'iv':iv, 'ciphertext':ct_cbc})
print(result)

# ECBモード
print("ECBモード")
cipher_ecb = AES.new(key, AES.MODE_ECB)
ct_bytes_ecb = cipher_ecb.encrypt(pad(data, AES.block_size))
ct_ecb = b64encode(ct_bytes_ecb).decode('utf-8')
result = json.dumps({'ciphertext':ct_ecb})
print(result)

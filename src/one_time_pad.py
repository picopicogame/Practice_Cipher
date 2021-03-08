#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

"""
参考にするqiita記事
文字列を数値に変換してxorする処理が載っている
pythonでは文字列同士で
str1 ^ str2
とやってもエラーになる ので参考になる
https://qiita.com/magiclib/items/fe2c4b2c4a07e039b905

"""

"""自分で作ってみる"""
# 文字列から16進バイト列へ
bytes_abcd = "abcd".encode()
print(bytes_abcd)
print(bytes_abcd.hex())


bin_str = ""
# バイト列から取り出すと10進int型
for bstr in bytes_abcd:
    temp_str = ""
    temp_str += str(bin(bstr))
    # 先頭の0bを除去
    temp_str = temp_str[2:]
    bin_str += temp_str

print(bin_str)
print(len(bin_str))

# 使い捨てパッドを作る
# 本来は暗号用乱数生成器を使うべきだが、標準ライブラリで代用
one_time_pad = ""
for i in range(len(bin_str)):
    one_time_pad += str(randint(0, 1))

print(one_time_pad)

# 2進数へ変換
bi_one_time_pad = int(one_time_pad, 2)
bi_str = int(bin_str, 2)

# 使い捨てパッドとxorを取って暗号化
crypt = bi_one_time_pad ^ bi_str
# 比較用に結果を並べる
print(bin(bi_str))
print(bin(bi_one_time_pad))
print(bin(crypt))

# 復号化
decrypt = bi_one_time_pad ^ crypt

print(decrypt)
print(bin(decrypt))
bin_decrypt = bin(decrypt)
bin_decrypt = bin_decrypt[2:]

decrypt_bytes = bytes()
str_decrypt = ""
for i, s in enumerate(bin_decrypt):
    str_decrypt += s
    if (i+1) % 7 == 0:
        temp = hex(int(str_decrypt, 2))
        temp = temp[2:]
        decrypt_bytes += bytes.fromhex(temp)
        str_decrypt = ""

print(decrypt_bytes.decode())



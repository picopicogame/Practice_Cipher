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


class OneTimePad:
    """使い捨てパッドクラス"""
    def __init__(self, plain_text: str):
        self.plain_text = plain_text
        self.bi_plain_text = self._make_bi_plain_text()
        self.one_time_pad = self._make_one_time_pad()
        self._check_input()

    def _make_bi_plain_text(self):
        bytes_plain = self.plain_text.encode()

        bin_str = ""

        # バイト列から取り出すと10進int型
        for bstr in bytes_plain:
            temp_str = ""
            temp_str += str(bin(bstr))
            # 先頭の0bを除去
            temp_str = temp_str[2:]
            bin_str += temp_str

        return bin_str

    def _make_one_time_pad(self):
        """ 使い捨てパッドを作る
            本来は暗号用乱数生成器を使うべきだが、標準ライブラリで代用"""
        otp = ""
        for i in range(len(self.bi_plain_text)):
            otp += str(randint(0, 1))
        return int(otp, 2)

    def _check_input(self):
        if len(self.plain_text) == 0:
            print("入力エラー。英字小文字a-zを入力してください")
            exit()

        for s in self.plain_text:
            if 'a' <= s <= 'z':
                pass
            else:
                print("入力エラー。英字小文字a-zを入力してください")
                exit()

    def encrypt(self):
        """暗号化する"""
        # 使い捨てパッドを使って暗号化
        return int(self.bi_plain_text, 2) ^ self.one_time_pad

    def decrypt(self, crypt):
        """復号化する"""
        # 使い捨てパッドで復号化
        decrypt = crypt ^ self.one_time_pad

        # 2進数へ変換
        bin_decrypt = bin(decrypt)
        # 先頭の0bを除去
        bin_decrypt = bin_decrypt[2:]

        decrypt_bytes = bytes()
        str_decrypt = ""
        # 2進数を8bitごとに分割して16進数に変換
        for i, s in enumerate(bin_decrypt):
            str_decrypt += s
            if (i+1) % 7 == 0:
                temp = hex(int(str_decrypt, 2)) # 16進数に変換
                temp = temp[2:]
                decrypt_bytes += bytes.fromhex(temp)  # バイト型に変換
                str_decrypt = ""

        # bytes型をデコードして文字列に戻す
        return decrypt_bytes.decode()

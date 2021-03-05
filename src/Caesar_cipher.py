#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CaesarCipher:
    def __init__(self, plain_text, key=3):
        self.plain_text = plain_text
        self.key = key
        self._check_input()

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
        crypted_str = ""

        for s in self.plain_text:
            shift_key = self.key % 26
            shift_s = ord(s) + shift_key
            if shift_s > ord('z'):
                shift_s = (shift_s - ord('z') + (ord('a')-1))
            crypted_str += chr(shift_s)

        return crypted_str

    def decrypt(self, crypted):
        plain_txt = ""
        for s in crypted:
            shift_key = self.key % 26
            shift_s = ord(s) - shift_key
            if shift_s < ord('a'):
                # aよりもいくつ前にあるか計算する
                sub_a_s = ord('a') - shift_s
                # zから差を引く
                shift_s = ord('z') - sub_a_s + 1
            plain_txt += chr(shift_s)

        return plain_txt


if __name__ == '__main__':
    cci = CaesarCipher("abcmnxyz", 4)
    print(cci.decrypt(cci.encrypt()))

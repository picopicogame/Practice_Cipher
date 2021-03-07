#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SimpleSubstitutionCipher:
    """単一換字暗号"""
    def __init__(self, plain_text):
        self.substitution_dic = {"a": "W",
                                 "b": "Y",
                                 "c": "H",
                                 "d": "F",
                                 "e": "X",
                                 "f": "U",
                                 "g": "M",
                                 "h": "T",
                                 "i": "J",
                                 "j": "V",
                                 "k": "S",
                                 "l": "G",
                                 "m": "E",
                                 "n": "N",
                                 "o": "B",
                                 "p": "R",
                                 "q": "D",
                                 "r": "Z",
                                 "s": "L",
                                 "t": "Q",
                                 "u": "A",
                                 "v": "P",
                                 "w": "C",
                                 "x": "O",
                                 "y": "K",
                                 "z": "I",
                                 }
        self.plain_text = plain_text
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
        crypt = ""
        for s in self.plain_text:
            crypt += self.substitution_dic[s]
        return crypt

    def decrypt(self, crypt):
        ret = ""
        for c in crypt:
            for k, v in self.substitution_dic.items():
                if c == v:
                    ret += k

        return ret

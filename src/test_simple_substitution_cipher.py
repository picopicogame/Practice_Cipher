#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simple_substitution_cipher import SimpleSubstitutionCipher


def test_isinstance():
    ssc = SimpleSubstitutionCipher("aaa")

    assert isinstance(ssc, SimpleSubstitutionCipher)


def test_substitution_dic_data():
    ssc = SimpleSubstitutionCipher("aaa")

    test_str = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for s in test_str:
        result += ssc.substitution_dic[s]

    expected = "WYHFXUMTJVSGENBRDZLQAPCOKI"
    assert result == expected


def test_encrypt():
    ssc = SimpleSubstitutionCipher("yoshiko")

    result = ssc.encrypt()
    expected = "KBLTJSB"
    assert result == expected

def test_decrypt():
    ssc = SimpleSubstitutionCipher("yoshiko")
    crypt = ssc.encrypt()
    plain_text = ssc.decrypt(crypt)
    expected = "yoshiko"

    assert plain_text == expected

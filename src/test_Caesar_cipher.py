#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Caesar_cipher import CaesarCipher
import pytest


def test_isinstance():
    cci = CaesarCipher("aaa")

    assert isinstance(cci, CaesarCipher)


def test_check_input(capsys):
    with pytest.raises(SystemExit) as excinfo:
        cci = CaesarCipher("abcあいうえお")
    out, _ = capsys.readouterr()

    assert out == "入力エラー。英字小文字a-zを入力してください\n"


def test_check_no_input(capsys):
    with pytest.raises(SystemExit) as excinfo:
        cci = CaesarCipher("")
    out, _ = capsys.readouterr()

    assert out == "入力エラー。英字小文字a-zを入力してください\n"


class TestEncrypt:

    def test_encrypt_chr3(self):
        """平文を3文字ずらすテスト"""
        cci = CaesarCipher("abc")

        expected = "def"
        assert cci.encrypt() == expected

    def test_encrypt_chr0(self):
        """平文を0文字ずらすテスト"""
        cci = CaesarCipher("abc", key=0)
        expected = "abc"
        assert cci.encrypt() == expected

    def test_encrypt_chr23(self):
        """平文を24文字ずらすテスト"""
        cci = CaesarCipher("abc", key=23)
        expected = "xyz"

        assert cci.encrypt() == expected

    def test_encrypt_chr24(self):
        """平文を24文字ずらすテスト"""
        cci = CaesarCipher("abc", key=24)
        expected = "yza"

        assert cci.encrypt() == expected

    def test_encrypt_chr25(self):
        """平文を25文字ずらすテスト"""
        cci = CaesarCipher("abc", key=25)
        expected = "zab"

        assert cci.encrypt() == expected

    def test_encrypt_chr26(self):
        """平文を26文字ずらすテスト"""
        cci = CaesarCipher("abc", key=26)
        expected = "abc"

        assert cci.encrypt() == expected

    def test_encrypt_chr100000(self):
        """平文をものすごく大きい数ずらす"""
        cci = CaesarCipher("abc", key=100000)
        expected = "efg"

        assert cci.encrypt() == expected


class TestDecrypt:
    def test_decrypt_chr3(self):
        """key=3で復号化する"""
        cci = CaesarCipher("abc", key=3)
        crypted_txt = cci.encrypt()
        plain_text = cci.decrypt(crypted_txt)
        assert crypted_txt == "def"
        assert plain_text == "abc"

    def test_decrypt_chr24(self):
        """key=25で復号化する"""
        cci = CaesarCipher("abc", key=24)
        crypted_txt = cci.encrypt()
        plain_text = cci.decrypt(crypted_txt)
        assert crypted_txt == "yza"
        assert plain_text == "abc"

    def test_decrypt_chr25(self):
        """key=25で復号化する"""
        cci = CaesarCipher("abc", key=25)
        crypted_txt = cci.encrypt()
        plain_text = cci.decrypt(crypted_txt)
        assert crypted_txt == "zab"
        assert plain_text == "abc"

    def test_decrypt_chr26(self):
        """key=26で復号化する"""
        cci = CaesarCipher("abc", key=26)
        crypted_txt = cci.encrypt()
        plain_text = cci.decrypt(crypted_txt)
        assert crypted_txt == "abc"
        assert plain_text == "abc"

    def test_decrypt_chr100000(self):
        """key=3で復号化する"""
        cci = CaesarCipher("abc", key=100000)
        crypted_txt = cci.encrypt()
        plain_text = cci.decrypt(crypted_txt)
        assert plain_text == "abc"

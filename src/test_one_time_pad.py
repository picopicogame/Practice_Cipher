#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from one_time_pad import OneTimePad


def test_isinstance():
    otp = OneTimePad("abcd")

    assert isinstance(otp, OneTimePad)


def test_one_time_pad():
    opt = OneTimePad("abcd")

    crypt = opt.encrypt()
    decrypt = opt.decrypt(crypt)
    print(opt.bi_plain_text)
    print(bin(opt.one_time_pad)[2:])
    print(bin(crypt)[2:])

    expected = "abcd"

    assert decrypt == expected



